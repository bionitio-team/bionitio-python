#!/usr/bin/env python

from setuptools import setup, find_packages

# Remember to change when making a new release
version = '0.1.0.0'

with open("README.md") as f:
    readme = f.read()

setup(
    name='bionitio',
    version=version,
    description='A prototypical bioinformatics command line tool',
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords=['bionitio','bioinformatics','fasta'],
    author='BIONITIO_AUTHOR',
    author_email='BIONITIO_EMAIL',
    url='https://github.com/BIONITIO_GITHUB_USERNAME/bionitio',
    download_url = 'https://github.com/BIONITIO_GITHUB_USERNAME/bionitio/tarball/{}'.format(version),
    license='MIT',
    package_dir={'bionitio': 'bionitio'},
    entry_points={
        'console_scripts': ['bionitio = bionitio.bionitio:main']
    },
    install_requires=["biopython"],
    setup_requires=["twine>=1.11.0", "setuptools>=38.6."],
    packages=find_packages(exclude=("readme_includes", "functional_tests")),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ]
)
