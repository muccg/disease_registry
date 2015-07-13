import setuptools
import os
from setuptools import setup
from dm1 import VERSION


data_files = {}
start_dir = os.getcwd()
for package in ('dm1', 'dm1_questionnaire'):
    data_files['dm1.' + package] = []
    os.chdir(os.path.join('dm1', package))
    for data_dir in ('templates', 'static', 'migrations', 'fixtures', 'templatetags', 'features', 'management'):
        data_files['dm1.' + package].extend(
            [os.path.join(subdir,f) for (subdir, dirs, files) in os.walk(data_dir) for f in files])
    os.chdir(start_dir)

# Include common disease registry modules from registry sibling directory
# This isn't what we want to be doing because we need to do this in the other
# registry apps too. Instead there should be a single setup.py for all the registries (IMO)
for package in ('common', 'patients', 'genetic', 'groups', 'humangenome', 'configuration'):
    data_files['registry.' + package] = []
    os.chdir(os.path.join('registry', package))
    for data_dir in ('templates', 'static', 'migrations', 'fixtures', 'templatetags', 'features', 'management'):
       data_files['registry.' + package].extend(
           [os.path.join(subdir,f) for (subdir, dirs, files) in os.walk(data_dir) for f in files])
    os.chdir('../..')
os.chdir('../dm1')

setup(name='django-dm1registry',
    version=VERSION,
    description='Django Disease Registry - DM1',
    long_description='Django Disease registry for DM1',
    author='Centre for Comparative Genomics',
    author_email='web@ccg.murdoch.edu.au',
    packages=[
        'dm1',
        'dm1.dm1',
        'dm1.dm1_questionnaire',
        'registry',
        'registry.common',
        'registry.patients',
        'registry.genetic',
        'registry.groups',
        'registry.forms',
        'registry.humangenome',
        'registry.configuration'
    ],
    package_data=data_files,
    zip_safe=False,
    install_requires=[
        'Django==1.5.12',
        'django-picklefield==0.1.9',
        'django-templatetag-sugar==0.1',
        'pyparsing==1.5.6',
        'wsgiref==0.1.2',
        'python-memcached==1.48',
        'South==0.8.4',
        'django-extensions>=0.7.1',
        'ccg-auth==0.3.3',
        'ccg-extras==0.1.9',
        'django-userlog==2.1.0',
        'django-messages-ui==0.2.6',
        'django-nose',
        'sure==1.2.1',
        'django-admin-views',
        'django-iprestrict==0.2',
        'six'
    ],
    dependency_links = [
        'https://bitbucket.org/ccgmurdoch/ccg-django-extras/downloads/ccg-extras-0.1.9.tar.gz',
        'https://bitbucket.org/ccgmurdoch/ccg-django-extras/downloads/ccg-auth-0.3.3.tar.gz',
        'https://github.com/muccg/django-userlog/archive/2.1.0.tar.gz#egg=django-userlog-2.1.0',
        'https://bitbucket.org/ccgmurdoch/ccg-django-extras/downloads/django-iprestrict-0.2.tar.gz'
    ],
)
