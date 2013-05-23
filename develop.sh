#!/bin/bash
#

# break on error
set -e 

ACTION="$1"
REGISTRY="$2"

declare -A port
port[dmd]='8001'
port[sma]='8002'
port[dm1]='8003'
port[dd]='8004'

PROJECT_NAME='disease_registry'
AWS_BUILD_INSTANCE='rpmbuild-centos6-aws'
TARGET_DIR="/usr/local/src/${PROJECT_NAME}"
CLOSURE="/usr/local/closure/compiler.jar"
MODULES="psycopg2==2.4.6 Werkzeug flake8"


function usage() {
    echo 'Usage ./develop.sh (test|lint|jslint|start|install|clean|purge|pipfreeze|pythonversion|dropdb|ci_remote_build|ci_remote_destroy|ci_rpm_publish) (dd|dmd|dm1|sma)'
}


function registry_needed() {
    if ! test ${REGISTRY}; then
        usage
        exit 1
    fi
}


function settings() {
    registry_needed
    export DJANGO_SETTINGS_MODULE="${REGISTRY}.settings"
}


# ssh setup, make sure our ccg commands can run in an automated environment
function ci_ssh_agent() {
    ssh-agent > /tmp/agent.env.sh
    source /tmp/agent.env.sh
    ssh-add ~/.ssh/ccg-syd-staging.pem
}


# build RPMs on a remote host from ci environment
function ci_remote_build() {
    registry_needed

    time ccg ${AWS_BUILD_INSTANCE} puppet
    time ccg ${AWS_BUILD_INSTANCE} shutdown:50

    EXCLUDES="('bootstrap'\, '.hg*'\, 'virt*'\, '*.log'\, '*.rpm')"
    SSH_OPTS="-o StrictHostKeyChecking\=no"
    RSYNC_OPTS="-l"
    time ccg ${AWS_BUILD_INSTANCE} rsync_project:local_dir=./,remote_dir=${TARGET_DIR}/,ssh_opts="${SSH_OPTS}",extra_opts="${RSYNC_OPTS}",exclude="${EXCLUDES}",delete=True
    time ccg ${AWS_BUILD_INSTANCE} build_rpm:centos/${REGISTRY}/${REGISTRY}.spec,src=${TARGET_DIR}

    mkdir -p build
    ccg ${AWS_BUILD_INSTANCE} getfile:rpmbuild/RPMS/x86_64/${REGISTRY}*.rpm,build/
}


# publish rpms 
function ci_rpm_publish() {
    registry_needed
    time ccg ${AWS_BUILD_INSTANCE} publish_rpm:build/${REGISTRY}*.rpm,release=6
}


# destroy our ci build server
function ci_remote_destroy() {
    ccg ${AWS_BUILD_INSTANCE} destroy
}


# lint using flake8
function lint() {
    registry_needed
    virt_${REGISTRY}/bin/flake8 ${REGISTRY} --ignore=E501 --count 
}


# lint js, assumes closure compiler
function jslint() {
    registry_needed
    JSFILES="${REGISTRY}/${REGISTRY}/${REGISTRY}/static/js/*.js"
    for JS in $JSFILES
    do
        java -jar ${CLOSURE} --js $JS --js_output_file output.js --warning_level DEFAULT --summary_detail_level 3
    done
}


# some db commands I use
function dropdb() {
    registry_needed
    # assumes postgres, user registryapp exists, appropriate pg_hba.conf
    echo "Drop the dev database manually:"
    echo "psql -aeE -U postgres -c \"SELECT pg_terminate_backend(pg_stat_activity.procpid) FROM pg_stat_activity where pg_stat_activity.datname = '${REGISTRY}'\" && psql -aeE -U postgres -c \"alter user registryapp createdb;\" template1 && psql -aeE -U registryapp -c \"drop database ${REGISTRY}\" template1 && psql -aeE -U registryapp -c \"create database ${REGISTRY};\" template1"
}


# run the tests using nose
function nosetests() {
    registry_needed
    source virt_${REGISTRY}/bin/activate
    virt_${REGISTRY}/bin/nosetests --with-xunit --xunit-file=tests.xml -v -w ${REGISTRY}
}


# run the tests using django-admin.py
function djangotests() {
    registry_needed
    source virt_${REGISTRY}/bin/activate
    virt_${REGISTRY}/bin/django-admin.py test ${REGISTRY} --noinput
}

# nose collect, untested
function nose_collect() {
    registry_needed
    source virt_${REGISTRY}/bin/activate
    virt_${REGISTRY}/bin/nosetests -v -w ${REGISTRY} --collect-only
}


# install virt for project
function installapp() {
    registry_needed
    # check requirements
    which virtualenv >/dev/null

    echo "Install ${REGISTRY}"
    virtualenv --system-site-packages virt_${REGISTRY}
    pushd ${REGISTRY}
    ../virt_${REGISTRY}/bin/python setup.py develop
    popd
    virt_${REGISTRY}/bin/easy_install ${MODULES}
}


# django syncdb, migrate and collect static
function syncmigrate() {
    registry_needed
    echo "syncdb"
    virt_${REGISTRY}/bin/django-admin.py syncdb --noinput --settings=${DJANGO_SETTINGS_MODULE} 1> syncdb-develop.log
    echo "migrate"
    virt_${REGISTRY}/bin/django-admin.py migrate --settings=${DJANGO_SETTINGS_MODULE} 1> migrate-develop.log
    echo "collectstatic"
    virt_${REGISTRY}/bin/django-admin.py collectstatic --noinput --settings=${DJANGO_SETTINGS_MODULE} 1> collectstatic-develop.log
}


# start runserver
function startserver() {
    registry_needed
    virt_${REGISTRY}/bin/django-admin.py runserver_plus ${port[${REGISTRY}]}
}


# debug for ci
function pythonversion() {
    registry_needed
    virt_${REGISTRY}/bin/python -V
}


# debug for ci
function pipfreeze() {
    registry_needed
    virt_${REGISTRY}/bin/pip freeze
}


# remove pyc
function clean() {
    registry_needed
    find ${REGISTRY} -name "*.pyc" -exec rm -rf {} \;
}


# clean, delete virts and logs
function purge() {
    registry_needed
    clean
    rm -rf virt_${REGISTRY}
    rm *.log
}


# tests
function runtest() {
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
    usage
esac