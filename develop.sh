#!/bin/bash
#

# break on error
set -e 

PROJECT="$1"
ACTION="$2"

declare -A port
port[dmd]='8001'
port[sma]='8002'
port[dm1]='8003'
port[dd]='8004'

function settings() {
    export DJANGO_SETTINGS_MODULE="${PROJECT}.settings"
}


# ssh setup, make sure our ccg commands can run in an automated environment
function ci_ssh_agent() {
    ssh-agent > /tmp/agent.env.sh
    source /tmp/agent.env.sh
    ssh-add ~/.ssh/ccg-syd-staging.pem
}


# build RPMs on a remote host from ci environment
function ci_remote_build() {
    EXCLUDES="('bootstrap'\, '.hg*'\, 'virt*'\, '*.log'\, '*.rpm')"
    time ccg rpmbuild-centos6-aws puppet
    ccg rpmbuild-centos6-aws dsudo:"chown ec2-user:ec2-user /usr/local/src"
    time ccg rpmbuild-centos6-aws rsync_project:local_dir=./,remote_dir=/usr/local/src/,ssh_opts="-o StrictHostKeyChecking\=no",extra_opts="-l",exclude="${EXCLUDES}",delete=True
    time ccg rpmbuild-centos6-aws build_rpm:centos/${PROJECT}/${PROJECT}.spec

    rm -rf build/${PROJECT}*
    mkdir -p build
    ccg rpmbuild-centos6-aws getfile:rpmbuild/RPMS/x86_64/${PROJECT}*.rpm,build/
}


# publish rpms 
function ci_rpm_publish() {
    time ccg rpmbuild-centos6-aws publish_rpm:build/${PROJECT}*.rpm,release=6
}


# destroy our ci build server
function ci_remote_destroy() {
    ccg rpmbuild-centos6-aws destroy
}


# lint js, assumes closure compiler
function jslint() {
    JSFILES="${PROJECT}/${PROJECT}/${PROJECT}/static/js/*.js"
    for JS in $JSFILES
    do
        java -jar /usr/local/closure/compiler.jar --js $JS --js_output_file output.js --warning_level DEFAULT --summary_detail_level 3
    done
}


# some db commands I use
function dropdb() {
    # assumes postgres, user registryapp exists, appropriate pg_hba.conf
    echo "Drop the dev database manually:"
    echo "psql -aeE -U postgres -c \"SELECT pg_terminate_backend(pg_stat_activity.procpid) FROM pg_stat_activity where pg_stat_activity.datname = '${PROJECT}'\" && psql -aeE -U postgres -c \"alter user registryapp createdb;\" template1 && psql -aeE -U registryapp -c \"drop database ${PROJECT}\" template1 && psql -aeE -U registryapp -c \"create database ${PROJECT};\" template1"
}


# run the nose tests
function nosetests() {
    source virt_${PROJECT}/bin/activate
    virt_${PROJECT}/bin/nosetests --with-xunit --xunit-file=tests.xml -v -w ${PROJECT}
}


# nose collect, untested
function nose_collect() {
    source virt_${PROJECT}/bin/activate
    virt_${PROJECT}/bin/nosetests -v -w ${PROJECT} --collect-only
}


# install virt for project
function installapp() {
    # check requirements
    which virtualenv >/dev/null

    echo "Install ${PROJECT}"
    virtualenv --system-site-packages virt_${PROJECT}
    pushd ${PROJECT}
    ../virt_${PROJECT}/bin/python setup.py develop
    popd
    #virt_${PROJECT}/bin/easy_install MySQL-python==1.2.3
    virt_${PROJECT}/bin/easy_install psycopg2==2.4.6
    virt_${PROJECT}/bin/easy_install Werkzeug
}


# django syncdb, migrate and collect static
function syncmigrate() {
    echo "syncdb"
    virt_${PROJECT}/bin/django-admin.py syncdb --noinput --settings=$DJANGO_SETTINGS_MODULE 1> syncdb-develop.log
    echo "migrate"
    virt_${PROJECT}/bin/django-admin.py migrate --settings=$DJANGO_SETTINGS_MODULE 1> migrate-develop.log
    echo "collectstatic"
    virt_${PROJECT}/bin/django-admin.py collectstatic --noinput --settings=$DJANGO_SETTINGS_MODULE 1> collectstatic-develop.log
}


# start runserver
function startserver() {
    virt_${PROJECT}/bin/django-admin.py runserver_plus ${port[${PROJECT}]}
}


# debug for ci
function pythonversion() {
    virt_${PROJECT}/bin/python -V
}


# debug for ci
function pipfreeze() {
    virt_${PROJECT}/bin/pip freeze
}


# remove pyc
function clean() {
    find ${PROJECT} -name "*.pyc" -exec rm -rf {} \;
}


# clean, delete virts and logs
function purge() {
    clean
    rm -rf virt_${PROJECT}
    rm *.log
}


# tests
function runtest() {
    nosetests
}


case $ACTION in
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
jslint)
    jslint
    ;;
syncmigrate)
    settings
    syncmigrate
    ;;
start)
    settings
    startserver
    ;;
install)
    settings
    installapp
    ;;
ci_remote_build)
    ci_ssh_agent
    ci_remote_build
    ;;
ci_remote_destroy)
    ci_ssh_agent
    ci_remote_destroy
    ;;
ci_rpm_publish)
    ci_ssh_agent
    ci_rpm_publish
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
    echo "Usage ./develop.sh (dd|dmd|dm1|sma) (test|jslint|start|install|clean|purge|pipfreeze|pipfreeze|pythonversion|dropdb|ci_remote_build|ci_remote_destroy|ci_rpm_publish)"
esac
