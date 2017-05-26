#!/usr/bin/env python
from setuptools import setup, find_packages


install_requires = [
    'requests',
]


tests_requires = [
    'responses',
]


setup(
    name='python-freeipa',
    version='0.1.2',
    author='OpenNode Team',
    author_email='info@opennodecloud.com',
    url='http://waldur.com',
    description='Lightweight FreeIPA client',
    long_description=open('README.rst').read(),
    install_requires=install_requires,
    extras_require={
        'tests': tests_requires,
    },
    package_dir={'': 'src'},
    packages=find_packages('src', exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    test_suite='python_freeipa.tests.suite',
    classifiers=(
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Systems Administration :: Authentication/Directory'
    )
)
