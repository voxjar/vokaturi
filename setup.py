#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name='vokaturi',
    version='0.0.2',
    description='Linux Vokaturi emotion detection',
    long_description=readme,
    author='Curtis Brown',
    author_email='curtis@voxjar.com',
    url='https://source.developers.google.com/p/platoaiinc/r/vokaturi',
    packages=find_packages(),
    package_data={'vokaturi': ['*.so']},
    # entry_points={
    # 'console_scripts': ['windcreek=windcreek:main'],
    # },
    # install_requires=['voxjar>=0.4.5'],
    license='UNLICENSED',
    keywords='voxjar',
    python_requires='>=2.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ])
