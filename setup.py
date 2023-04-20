#!/usr/bin/python3
# -*- coding:utf-8 -*-
# run via  python3 setup.py upload

import io, os, sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'python-whitebit-sdk'
DESCRIPTION = 'Clients and methods to interact with the Whitebit exchange.'
URL = 'https://github.com/whitebit-exchange/python-sdk'
EMAIL = 'support@whitebit.com'
AUTHOR = 'UAB Clear White Technologies'
REQUIRES_PYTHON = '>=3.10.0'
VERSION = None

# What packages are required for this module to be executed?
REQUIRED = [
    'websockets>=10.4.0', 'asyncio>=3.4', 'requests>=2.28.1', 'responses>=0.23.1',
    'urllib3==1.26.15'
]


# What packages are optional?
EXTRAS = {
    'testing': ['pytest', 'tqdm']
}

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f'\n{f.read()}'
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}
if not VERSION:
    project_slug = 'whitebit'
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    raise ValueError('Version not found!')

class UploadCommand(Command):
    '''Support setup.py upload.'''

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        print(f'\033[1m{s}\033[0m')

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system(f'{sys.executable} setup.py sdist bdist_wheel --universal')

        self.status('Testing the build using flake8')
        if os.system('flake8 . --select=E9,F63,F7,F82 --show-source --statistics') != 0:
            self.status('Testing failed, build has some errors in it!')
            exit(1)

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        # self.status('Pushing git tags…')
        # os.system(f'git tag v{about['__version__']}')
        # os.system('git push --tags')

        sys.exit()

class TestUploadCommand(Command):
    '''Support setup.py test upload.'''

    description = 'Build and test publishing the package.'
    user_options = []

    @staticmethod
    def status(s):
        print(f'\033[1m{s}\033[0m')

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system(f'{sys.executable} setup.py sdist bdist_wheel --universal')

        self.status('Testing the build using flake8')
        if os.system('flake8 . --select=E9,F63,F7,F82 --show-source --statistics') != 0:
            self.status('Testing failed, build has some errors in it!')
            sys.exit(1)

        self.status('Uploading the package to test PyPI via Twine…')
        os.system('twine upload -r testpypi dist/*')#--repository-url https://test.pypi.org/legacy/ dist/*')

        sys.exit()

class TestCommand(Command):

    description = 'Build and test the package.'
    user_options = []

    @staticmethod
    def status(s):
        print(f'\033[1m{s}\033[0m')

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system(f'{sys.executable} setup.py sdist bdist_wheel --universal')

        self.status('Testing the build')
        if os.system('flake8 . --select=E9,F63,F7,F82 --show-source --statistics') != 0: exit(1)
        print('Success')
        sys.exit()

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*', 'tests.*', '*.env*']),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Development Status :: 5 - Production/Stable',
        'Framework :: AsyncIO',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows'
    ],
    cmdclass={
        'upload': UploadCommand,
        'test': TestCommand,
        'testupload': TestUploadCommand,
    },
)
