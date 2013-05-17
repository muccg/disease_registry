import setuptools
import os
from setuptools import setup

data_files = {}
start_dir = os.getcwd()
for package in ['dmd']:
    data_files['dmd.' + package] = []
    os.chdir(os.path.join('dmd', package))
    for data_dir in ('templates', 'static', 'migrations', 'fixtures'):
	    data_files['dmd.' + package].extend(
	        [os.path.join(subdir, f) for (subdir, dirs, files) in os.walk(data_dir) for f in files])
    os.chdir(start_dir)

# Include common disease registry modules from registry sibling directory
# This isn't what we want to be doing because we need to do this in the other
# registry apps too. Instead there should be a single setup.py for all the registries (IMO)
for package in ('common', 'patients', 'genetic', 'groups', 'humangenome'):
    data_files['registry.' + package] = []
    os.chdir(os.path.join('registry', package))
    for data_dir in ('templates', 'static', 'migrations', 'fixtures', 'templatetags'):
       data_files['registry.' + package].extend(
           [os.path.join(subdir,f) for (subdir, dirs, files) in os.walk(data_dir) for f in files])
    os.chdir('../..')
os.chdir('../dmd')

setup(name='django-dmdregistry',
    version='1.0.14',
    description='Django Disease Registry - DMD',
    long_description='Django Disease registry for Duchenne Muscular Dystrophy',
    author='Centre for Comparative Genomics',
    author_email='web@ccg.murdoch.edu.au',
    packages=[
        'dmd',
        'dmd.dmd',
        'registry',
        'registry.common',
        'registry.patients',
        'registry.genetic',
        'registry.groups',
        'registry.forms',
        'registry.humangenome'
    ],
    package_data=data_files,
    zip_safe=False,
    install_requires=[
        'Django==1.4.5',
        'django-picklefield==0.1.9',
        'django-templatetag-sugar==0.1',
        'pyparsing==1.5.6',
        'wsgiref==0.1.2',
        'python-memcached==1.48',
        'South>=0.7.3',
        'django-extensions>=0.7.1',
        'ccg-auth==0.3.2',
        'ccg-extras==0.1.5',
        'django-userlog==0.2.1',
        'django_qbe',
        'django-nose'
    ],
    dependency_links = [
        "http://repo.ccgapps.com.au",
        "https://bitbucket.org/ccgmurdoch/django-userlog/downloads/django_userlog-0.2.1.tar.gz",
    ],
)
