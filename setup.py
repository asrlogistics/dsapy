from importlib.resources import Package
from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='stlpy',
    version='0.0.1',
    description="A Helpful and easy to use library",
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Rudransh & Shashwat',
    author_email='aarti19830@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='dsa',
    packages=find_packages,
    install_requires=['math','numpy','itertools','collections']
)
