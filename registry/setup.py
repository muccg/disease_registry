import setuptools
from glob import glob
from setuptools import setup


setup(name='django-diseaseregistry',
    version='1.4',
    description='Django Disease Registry',
    long_description='Collection Django applications implementing various disease registries',
    author='Centre for Comparative Genomics',
    author_email='web@ccg.murdoch.edu.au',
    namespace_packages=['ccg', 'ccg.djangoapps'],
    packages=[
        'ccg.djangoapps.dm1',
        'ccg.djangoapps.dm1_questionnaire',
        'ccg.djangoapps.dmd',
        'ccg.djangoapps.sma',
        'ccg.djangoapps.patients',
        'ccg.djangoapps.genetic',
        'ccg.djangoapps.groups',
    ],
    package_data={
        '': [
            'templates/*/*',
            'static/*/*/*/*',
            'migrations/*'
        ] 
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


