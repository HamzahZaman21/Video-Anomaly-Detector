#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Hamzah Zaman",
    author_email='hamzahzaman21@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Project",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='video_anomaly_detector',
    name='video_anomaly_detector',
    packages=find_packages(include=['video_anomaly_detector', 'video_anomaly_detector.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/HamzahZaman21/video_anomaly_detector',
    version='1.0',
    zip_safe=False,
)
