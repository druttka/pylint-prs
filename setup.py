#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
import atexit
from subprocess import check_call
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop


def _execute():
    return #check_call("pip install pylintprs --no-deps".split())

class PostInstall(install):
    def run(self):
        atexit.register(_execute)
        install.run(self)

class PostDevelop(develop):
    def run(self):
        atexit.register(_execute)
        develop.run(self)

# with open('README.rst') as readme_file:
#    readme = readme_file.read()

#with open('HISTORY.rst') as history_file:
#    history = history_file.read()

requirements = [
]

setup_requirements = [
]

test_requirements = [
]


setup(
    name='pylintprs',
    version='0.0.1',
    description="Test Travis integration for python PRs.",
    long_description="See https://github.com/druttka/pylint-prs for usage instructions.",
    author="David Ruttka",
    author_email='david.ruttka@microsoft.com',
    url='https://github.com/druttka/pylint-prs',
    packages=find_packages(include=['pylintprs']),
    entry_points={
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    cmdclass={'install': PostInstall, 'develop': PostDevelop}
)
