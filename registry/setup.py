import setuptools
import os
from setuptools import setup


setup(name='django-diseaseregistry',
    version='1.4',
    description='Django Disease Registry',
    long_description='Collection Django applications implementing various disease registries',
    author='Centre for Comparative Genomics',
    author_email='web@ccg.murdoch.edu.au',
    namespace_packages=['ccg', 'ccg.django', 'ccg.django.app'],
    packages=[
        'ccg',
        'ccg.django',
        'ccg.django.registryutils',
        'ccg.django.app',
        'ccg.django.app.dm1',
        'ccg.django.app.dm1_questionnaire',
        'ccg.django.app.dmd',
        'ccg.django.app.sma',
        'ccg.django.app.patients',
        'ccg.django.app.genetic',
        'ccg.django.app.groups',
    ],
    package_data={
        '': [os.path.join(subdir,f) for (subdir, dirs, files) in os.walk('templates') for f in files] +
            [os.path.join(subdir,f) for (subdir, dirs, files) in os.walk('static') for f in files] +
            [os.path.join(subdir,f) for (subdir, dirs, files) in os.walk('migrations') for f in files]
    },
    zip_safe=True,
    install_requires=[
        'Mango-py==1.3.1-ccg1-3',
        'django-picklefield==0.1.9',
        'django-templatetag-sugar==0.1',
        'pyparsing==1.5.6',
        'virtualenv==1.6.4',
        'wsgiref==0.1.2',
        'python-memcached==1.48',
        'Mako>=0.5.0',
        'South>=0.7.3',
        'django-extensions>=0.7.1',
        'ccg-auth==0.3.2',
        'ccg-extras==0.1.5',
        'ccg-makoloader==0.2.4'
    ],
)


