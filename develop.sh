#!/bin/sh
#

# break on error
set -e

ACTION="$1"
REGISTRY="$2"
PARAM="$3"

DATE=`date +%Y.%m.%d`
PROJECT_NAME='disease_registry'
AWS_STAGING_INSTANCE='aws-syd-registry-staging'
TARGET_DIR="/usr/local/src/${PROJECT_NAME}"
CLOSURE="/usr/local/closure/compiler.jar"
TESTING_MODULES="pyvirtualdisplay nose selenium"
MODULES="Werkzeug flake8 docker-compose ${TESTING_MODULES}"
PIP_OPTS='--download-cache ~/.pip/cache'
PIP5_OPTS="${PIP_OPTS} --process-dependency-links"


usage() {
    echo 'Usage ./develop.sh (test|lint|jslint)'
    echo '                   (start|install|clean|purge)'
    echo '                   (pipfreeze|pythonversion)'
    echo '                   (dropdb|loaddata)'
    echo '                   (rpmbuild|rpm_publish)'
    echo '                   (dockerbuild)'
    echo '                   (ci_staging|ci_staging_selenium|ci_staging_tests) (dd|dmd|sma|fshd)'
    exit 1
}


registry_needed() {
    if ! test ${REGISTRY}; then
        usage
    fi
}


settings() {
    registry_needed
    export DJANGO_SETTINGS_MODULE="${REGISTRY}.settings"
}


# ssh setup, make sure our ccg commands can run in an automated environment
ci_ssh_agent() {
    ssh-agent > /tmp/agent.env.sh
    source /tmp/agent.env.sh
    ssh-add ~/.ssh/ccg-syd-staging-2014.pem
}


# docker build and push in CI
dockerbuild() {
    make_virtualenv

    image="muccg/disease-registry:${REGISTRY}"
    hgtag=`hg log -r "." --template "{latesttag}\n" 2> /dev/null`
    template="$(cat docker/Dockerfile.in)"

    # log the Dockerfile
    echo "########################################"
    sed -e "s/TAG/${hgtag}/g" -e "s/REGISTRY/${REGISTRY}/g" docker/Dockerfile.in
    echo "########################################"

    # attempt to warm up docker cache
    docker pull ${image} || true

    sed -e "s/TAG/${hgtag}/g" -e "s/REGISTRY/${REGISTRY}/g" docker/Dockerfile.in | docker build --pull=true -t ${image} -
    sed -e "s/TAG/${hgtag}/g" -e "s/REGISTRY/${REGISTRY}/g" docker/Dockerfile.in | docker build -t ${image}-${DATE} -

    if [ -z ${hgtag+x} ]; then
        echo "No tag set"
    else
        echo "hg tag ${hgtag}"
        sed -e "s/TAG/${hgtag}/g" -e "s/REGISTRY/${REGISTRY}/g" docker/Dockerfile.in | docker build -t ${image}-${hgtag} -
        docker push ${image}-${hgtag}
    fi

    docker push ${image}
    docker push ${image}-${DATE}
}


# build RPM
rpmbuild() {
    mkdir -p data/rpmbuild
    chmod o+rwx data/rpmbuild

    make_virtualenv

    docker-compose --project-name ${PROJECT_NAME} -f fig-rpmbuild-${REGISTRY}.yml up
}


# publish rpms 
rpm_publish() {
    registry_needed
    time ccg publish_testing_rpm:data/rpmbuild/RPMS/x86_64/${REGISTRY}*.rpm,release=6
}


# puppet up staging which will install the latest rpm for each registry
ci_staging() {
    ccg ${AWS_STAGING_INSTANCE} boot
    ccg ${AWS_STAGING_INSTANCE} puppet
    ccg ${AWS_STAGING_INSTANCE} shutdown:120
}


# staging seleinium test
ci_staging_selenium() {
    ccg ${AWS_STAGING_INSTANCE} dsudo:'dbus-uuidgen --ensure'
    ccg ${AWS_STAGING_INSTANCE} dsudo:'chown apache:apache /var/www'


    ccg ${AWS_STAGING_INSTANCE} dsudo:'yum remove dmd sma -y'
    ccg ${AWS_STAGING_INSTANCE} dsudo:'yum --enablerepo\=ccg-testing clean all'

    ccg ${AWS_STAGING_INSTANCE} dsudo:'yum install dmd -y'
    ccg ${AWS_STAGING_INSTANCE} dsudo:'killall httpd || true'
    ccg ${AWS_STAGING_INSTANCE} dsudo:'service httpd start'
    ccg ${AWS_STAGING_INSTANCE} dsudo:'echo http://localhost/dmd > /tmp/dmd_site_url'
    ccg ${AWS_STAGING_INSTANCE} dsudo:'dmd run_lettuce --app-name dmd --with-xunit --xunit-file\=/tmp/tests-dmd.xml || true'
    ccg ${AWS_STAGING_INSTANCE} dsudo:'yum remove dmd -y'
    ccg ${AWS_STAGING_INSTANCE} dsudo:'rm /tmp/dmd_site_url'
    
    ccg ${AWS_STAGING_INSTANCE} dsudo:'yum install sma -y'
    ccg ${AWS_STAGING_INSTANCE} dsudo:'killall httpd || true'
    ccg ${AWS_STAGING_INSTANCE} dsudo:'service httpd start'
    ccg ${AWS_STAGING_INSTANCE} dsudo:'echo http://localhost/sma > /tmp/sma_site_url'
    ccg ${AWS_STAGING_INSTANCE} dsudo:'sma run_lettuce --app-name sma --with-xunit --xunit-file\=/tmp/tests-sma.xml || true'
    ccg ${AWS_STAGING_INSTANCE} dsudo:'yum remove sma -y'
    ccg ${AWS_STAGING_INSTANCE} dsudo:'rm /tmp/sma_site_url'
    
    ccg ${AWS_STAGING_INSTANCE} getfile:/tmp/tests-dd.xml,./
}

# gets the manage.py command for a registry
django_admin() {
    case $1 in
        dd)
            echo "registrydd"
            ;;
        *)
            echo $1
            ;;
    esac
}

# run tests on staging
ci_staging_tests() {
    registry_needed

    # /tmp is used for test results because the apache user has
    # permission to write there.
    REMOTE_TEST_DIR=/tmp
    REMOTE_TEST_RESULTS=${REMOTE_TEST_DIR}/tests.xml

    # Grant permission to create a test database.
    DATABASE_USER=registryapp
    ccg ${AWS_STAGING_INSTANCE} dsudo:"su postgres -c \"psql -c 'ALTER ROLE ${DATABASE_USER} CREATEDB;'\""

    # This is the command which runs manage.py with the correct environment
    DJANGO_ADMIN=$(django_admin ${REGISTRY})

    # Run tests, collect results
    TEST_LIST="${REGISTRY}.${REGISTRY}.tests"
    ccg ${AWS_STAGING_INSTANCE} drunbg:"Xvfb \:0"
    ccg ${AWS_STAGING_INSTANCE} dsudo:"cd ${REMOTE_TEST_DIR} && env DISPLAY\=\:0 dbus-launch ${DJANGO_ADMIN} test --noinput --with-xunit --xunit-file\=${REMOTE_TEST_RESULTS} --liveserver\=localhost\:8082\,8090-8100\,9000\-9200\,7041 ${TEST_LIST} || true"
    ccg ${AWS_STAGING_INSTANCE} getfile:${REMOTE_TEST_RESULTS},./
}


# lint using flake8
lint() {
    make_virtualenv
    flake8 ${REGISTRY} --ignore=E501 --count 
}


# lint js, assumes closure compiler
jslint() {
    make_virtualenv
    pip install 'closure-linter==2.3.13'
    JSFILES="${REGISTRY}/${REGISTRY}/${REGISTRY}/static/js/*.js"
    EXCLUDES='-x digitalspaghetti.password.js,json2.js'
    for JS in $JSFILES
    do
        gjslint ${EXCLUDES} --disable 0131,0110 --nojsdoc $JS
    done
}


# some db commands I use
dropdb() {
    registry_needed
    # assumes postgres, user registryapp exists, appropriate pg_hba.conf
    echo "Drop the dev database manually:"
    echo "psql -aeE -U postgres -c \"SELECT pg_terminate_backend(pg_stat_activity.procpid) FROM pg_stat_activity where pg_stat_activity.datname = '${REGISTRY}'\" && psql -aeE -U postgres -c \"alter user registryapp createdb;\" template1 && psql -aeE -U registryapp -c \"drop database ${REGISTRY}\" template1 && psql -aeE -U registryapp -c \"create database ${REGISTRY};\" template1"
}


# run the tests using nose
nosetests() {
    registry_needed
    source virt_${REGISTRY}/bin/activate
    virt_${REGISTRY}/bin/nosetests --with-xunit --xunit-file=tests.xml -v -w ${REGISTRY}
}


# run the tests using django-admin.py
djangotests() {
    registry_needed
    source virt_${REGISTRY}/bin/activate
    virt_${REGISTRY}/bin/django-admin.py test ${REGISTRY} --noinput
}

# nose collect, untested
nose_collect() {
    registry_needed
    source virt_${REGISTRY}/bin/activate
    virt_${REGISTRY}/bin/nosetests -v -w ${REGISTRY} --collect-only
}


make_virtualenv() {
    registry_needed
    # check requirements
    which virtualenv > /dev/null
    if [ ! -e virt_${REGISTRY} ]; then
        virtualenv virt_${REGISTRY}
    fi
    . virt_${REGISTRY}/bin/activate
    which pip
    pip --version
    pip install ${MODULES}
}


# install virt for project
installapp() {
    registry_needed
    make_virtualenv

    docker-compose -f fig-${REGISTRY}.yml build
}


loaddata() {
    registry_needed
    echo "loaddata"
    virt_${REGISTRY}/bin/django-admin.py loaddata ${PARAM} --settings=${DJANGO_SETTINGS_MODULE} 1> loaddata-develop.log
}

# chooses a tcp port number for the debug server
port() {
    # this could be an associative array, but they aren't compatible
    # with bash3
    case $1 in
        dmd)
            echo "8001"
            ;;
        sma)
            echo "8002"
            ;;
        dd)
            echo "8004"
            ;;
        fshd)
            echo "8005"
            ;;
    esac
}

# start runserver
startserver() {
    registry_needed
    make_virtualenv

    docker-compose -f fig-${REGISTRY}.yml up
}


# debug for ci
pythonversion() {
    registry_needed
    virt_${REGISTRY}/bin/python -V
}


# debug for ci
pipfreeze() {
    registry_needed
    virt_${REGISTRY}/bin/pip freeze
}


# remove pyc
clean() {
    registry_needed
    find ${REGISTRY} -name "*.pyc" -exec rm -rf {} \;
}


# clean, delete virts and logs
purge() {
    registry_needed
    clean
    rm -rf virt_${REGISTRY}
    rm *.log
}


# tests
runtest() {
    #nosetests
    djangotests
}


case ${ACTION} in
pythonversion)
    pythonversion
    ;;
pipfreeze)
    pipfreeze
    ;;
test)
    settings
    runtest
    ;;
lint)
    lint
    ;;
jslint)
    jslint
    ;;
syncmigrate)
    settings
    syncmigrate
    ;;
loaddata)
    settings
    loaddata
    ;;
start)
    settings
    startserver
    ;;
install)
    settings
    installapp
    ;;
dockerbuild)
    dockerbuild
    ;;
rpmbuild)
    rpmbuild
    ;;
ci_remote_destroy)
    ci_ssh_agent
    ci_remote_destroy
    ;;
rpm_publish)
    ci_ssh_agent
    rpm_publish
    ;;
ci_staging)
    ci_ssh_agent
    ci_staging
    ;;
ci_staging_selenium)
    ci_ssh_agent
    ci_staging_selenium
    ;;
ci_staging_tests)
    ci_ssh_agent
    ci_staging_tests
    ;;
dropdb)
    dropdb
    ;;
clean)
    settings
    clean 
    ;;
purge)
    settings
    clean
    purge
    ;;
*)
    usage
esac
