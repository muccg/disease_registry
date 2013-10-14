from setuptools import setup

setup(name='django-ccg-cdes',
    version='0.1',
    description='CCG CDEs',
    long_description='CCG Common Data Elements',
    author='Centre for Comparative Genomics',
    author_email='web@ccg.murdoch.edu.au',
    packages=[
        'ccg_cdes',
    ],
    install_requires=[
        'Django==1.5.4',
    ],
)

