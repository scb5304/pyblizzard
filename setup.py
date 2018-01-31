try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from setuptools import find_packages

setup(
    name='pyblizzard',
    packages=find_packages(exclude=['tests']),
    version='v1.1',
    description='Python3 wrapper for the Battle.net Community APIs.',
    author='Steven Brown',
    author_email='scb5304@gmail.com',
    url='https://github.com/scb5304/pyblizzard',
    download_url='https://github.com/scb5304/pyblizzard/archive/v1.1.tar.gz',
    keywords=['python', 'python3', 'blizzard', 'api', 'wrapper', 'battle', 'battle.net'],
    install_requires=['jsonpickle', 'requests'],
    setup_requires=['jsonpickle', 'requests'],
    classifiers=[],
)
