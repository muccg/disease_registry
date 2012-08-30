# -*- coding: utf-8 -*-
import os
from fabric.api import env, local
from ccgfab.base import *

env.username = os.environ["USER"]
env.app_root = '/usr/local/python/ccgapps/'
env.app_name = 'registry'
env.app_install_names = ['dmd','sma','dm1']
env.vc = 'mercurial'
env.git_trunk_url = ""
env.svn_trunk_url = ""
env.svn_tags_url = ""

env.writeable_dirs.extend([]) # add directories you wish to have created and made writeable
env.content_excludes.extend([]) # add quoted patterns here for extra rsync excludes
env.content_includes.extend([]) # add quoted patterns here for extra rsync includes

class LocalPaths():

    def getSettings(self,target):
        assert target in env.app_install_names
        return os.path.join(env.app_root, target, env.username, env.app_name, "settings.py")

    def getProjectDir(self, target):
        assert target in env.app_install_names
        return os.path.join(env.app_root, target, env.username, env.app_name)

    def getParentDir(self,target):
        assert target in env.app_install_names
        return os.path.join(env.app_root, target, env.username)

    def getVirtualPython(self, target):
        assert target in env.app_install_names
        return os.path.join(self.getProjectDir(target), 'virtualpython/bin/python')

localPaths = LocalPaths()

def deploy():
    """User deployment"""
    release = _ccg_deploy_user()

def snapshot():
    """Snapshot deployment"""
    release = _ccg_deploy_snapshot()

def release(*args, **kwargs):
    """
    Make a release deployment
    """
    migration = kwargs.get("migration", True)
    requirements = kwargs.get("requirements", "requirements.txt")
    tag = kwargs.get("tag", None)
    env.ccg_requirements = requirements
    env.auto_confirm=False
    release = _ccg_deploy_release(tag=tag,migration=migration,mungeInstallName=True)

def make_live(tag=env.user):
    _make_live_symlinks(tag)

def testrelease():
    """Release deployment with dev settings"""
    release = _ccg_deploy_release(devrelease=True)

def purge():
    """Purge a user deployment"""
    _ccg_purge_user()

def purge_snapshot():
    """Purge a snapshot deployment"""
    _ccg_purge_snapshot()

def manage(*args):
    _django_env(args[0])
    print local(localPaths.getVirtualPython(args[0]) + " " + localPaths.getProjectDir(args[0]) + "/manage.py " + " ".join(args[1:]), capture=False)

def _django_env(target):
    os.environ["DJANGO_SETTINGS_MODULE"]="settings"
    os.environ["DJANGO_PROJECT_DIR"]=localPaths.getProjectDir(target)
    os.environ["PYTHONPATH"] = "/usr/local/etc/ccgapps/:" + localPaths.getProjectDir(target) + ":" + localPaths.getParentDir(target)
    os.environ["PROJECT_DIRECTORY"] = localPaths.getProjectDir(target)
