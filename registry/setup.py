import setuptools
import os
from setuptools import setup

data_files = {}
start_dir = os.getcwd()
for package in ('common', 'patients', 'genetic', 'groups', 'humangenome'):
    data_files['registry.' + package] = []
    os.chdir(os.path.join('registry', package))
    for data_dir in ('templates', 'static', 'migrations', 'fixtures', 'templatetags'):
	data_files['registry.' + package].extend(
	    [os.path.join(subdir,f) for (subdir, dirs, files) in os.walk(data_dir) for f in files]) 
    os.chdir(start_dir)

setup(name='django-diseaseregistry',
    version='1.4',
    description='Django Disease Registry',
    long_description='Collection of Django applications implementing various aspects for disease registries',
    author='Centre for Comparative Genomics',
    author_email='web@ccg.murdoch.edu.au',
    url="http://ccg.murdoch.edu.au",
    packages=[
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
        'South>=0.7.3',
    ],
)


