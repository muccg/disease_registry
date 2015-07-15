import setuptools
import os
from setuptools import setup
from dmd import VERSION

data_files = {}
start_dir = os.getcwd()
for package in ['dmd']:
    data_files['dmd.' + package] = []
    os.chdir(os.path.join('dmd', package))
    for data_dir in ('templates', 'static', 'migrations', 'fixtures', 'features', 'templatetags', 'management'):
        data_files['dmd.' + package].extend(
            [os.path.join(subdir, f) for (subdir, dirs, files) in os.walk(data_dir) for f in files])
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
os.chdir('../dmd')

setup(name='django-dmdregistry',
    version=VERSION,
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
        'django-messages-ui==0.2.6',
        'ccg-auth==0.3.3',
        'ccg-extras==0.1.9',
        'django-userlog==2.1.0',
        'django-nose',
        'django-admin-views==0.1.3',
        'django-reversion==1.8.0',
        'sure==1.2.1',
        'django-templatetag-handlebars==1.2.0',
        'django-iprestrict==0.2',
        'django-sql-explorer==0.5.0',
        'six',
        'psycopg2==2.5.5',
        'werkzeug'
    ],
    dependency_links = [
        'https://bitbucket.org/ccgmurdoch/ccg-django-extras/downloads/ccg-extras-0.1.9.tar.gz',
        'https://bitbucket.org/ccgmurdoch/ccg-django-extras/downloads/ccg-auth-0.3.3.tar.gz',
        'https://pypi.python.org/packages/source/d/django-templatetag-handlebars/django-templatetag-handlebars-1.2.0.zip',
        'https://github.com/muccg/django-userlog/archive/2.1.0.tar.gz#egg=django-userlog-2.1.0',
        'https://bitbucket.org/ccgmurdoch/ccg-django-extras/downloads/django-iprestrict-0.2.tar.gz'
    ],
)
