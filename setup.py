#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    README = f.read()
# with open('HISTORY.md', 'r', 'utf-8') as f:
#     history = f.read()

setup(
    name='yah2j',
    version='0.1',
    description='Yet another HAR to JMX',
    long_description=README,
    author='Alexey Svetlov',
    author_email='alexeysvetlov92@gmail.com',
    url='https://github.com/lanitgithub/yah2j',
    # license='MIT',
    include_package_data=True,
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        # 'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    project_urls={
        # 'Documentation': 'https://requests.readthedocs.io',
        'Source': 'https://github.com/lanitgithub/yah2j',
    },
)
