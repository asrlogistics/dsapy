from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.3'
DESCRIPTION = 'A Standard Template Library in Python (for c++ developers)'
LONG_DESCRIPTION = 'A library with almost all data structure and helpful functions for working with python , it will reduce your 50 lines of code and 1 hr for a big project into 1 liner code. we will also provide the documentation for your help. Thankyou team dsapy.'

# Setting up
setup(
    name="dsapy",
    version=VERSION,
    author="Rudransh Bhardwaj",
    author_email="aarti19830@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy1.23.5'],
    keywords=['python', 'dsa','stl','c++','best for me 😁!'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
