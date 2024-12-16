import os
from setuptools import setup

CURRENT_VERSION = '0.0.1'


def read_file(filename):
    """Open a file, read it and return its contents."""
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path) as f:
        return f.read()


setup(
    name='python_sleep_bridge',
    version=CURRENT_VERSION,
    description='This project is "bridge" between the sleep and python language. It allows the control of a Cobalt Strike teamserver through python without the need for the standard GUI client.',

    # Get the long description from the README file
    long_description=read_file('README.md'),

    url='https://github.com/rkbennett/sleep_python_bridge',
    download_url='https://github.com/rkbennett/sleep_python_bridge'
                 '/archive/{}.tar.gz'.format(CURRENT_VERSION),

    author='Cobalt-Strike',
    author_email='rdidyk@tmgtop.com',
    license='Apache version 2.0',

    classifiers=[
        'Intended Audience :: Developers',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='sleep python bridge',
    packages=['sleep_python_bridge'],

    install_requires=[
        'python-magic>=0.4.18',
        'libmagic>=1.0',
        'python-magic-bin>=0.4.14; sys_platform=="win32"',
        'javaobj-py3>=0.4.1',
        'pepy>=1.2.0',
        'ptyprocess>=0.5',
        'pexpect'
    ],

)
