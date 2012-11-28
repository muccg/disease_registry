import setuptools
import os
from setuptools import setup



data_files = {}
start_dir = os.getcwd()
for package in ('patients', 'genetic', 'groups'):
    data_files['registry.' + package] = []
    os.chdir(os.path.join('registry', package))
    for data_dir in ('templates', 'static', 'migrations', 'fixtures'):
	data_files['registry.' + package].extend(
	    [os.path.join(subdir,f) for (subdir, dirs, files) in os.walk(data_dir) for f in files]) 
    os.chdir(start_dir)

setup(name='django-diseaseregistry',
    version='1.4',
    description='Django Disease Registry',
    long_description='Collection Django applications implementing various disease registries',
    author='Centre for Comparative Genomics',
    author_email='web@ccg.murdoch.edu.au',
    packages=[
        'registry',
        'registry.patients',
        'registry.genetic',
        'registry.groups',
        'registry.utils',
        'registry.forms',
        'registry.mako',
    ],
    package_data=data_files,
    zip_safe=False,
    install_requires=[
        'Mango-py==1.3.1-ccg1-3',
        'django-picklefield==0.1.9',
        'django-templatetag-sugar==0.1',
        'pyparsing==1.5.6',
        'wsgiref==0.1.2',
        'python-memcached==1.48',
        'Mako>=0.5.0',
        'South>=0.7.3',
        'django-extensions>=0.7.1',
        'ccg-auth==0.3.2',
        'ccg-extras==0.1.5',
        'ccg-makoloader==0.2.4',
        'django-userlog==0.2.1',
    ],
)


