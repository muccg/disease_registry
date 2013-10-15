from setuptools import setup

setup(name='django-ccg-cdes',
    version='0.1',
    packages=['ccg_cdes'],
    description='CCG CDEs',
    long_description='CCG Common Data Elements',
    author='Centre for Comparative Genomics',
    author_email='web@ccg.murdoch.edu.au',
    package_dir= {'ccg_cdes': 'src/ccg_cdes'},
    package_data= {'ccg_cdes': ['templates/ccg_cdes/cde.html']},
    install_requires=[
        'Django==1.5.4',
    ],
)

