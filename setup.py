# from importlib.resources import Package
# from setuptools import setup, find_packages

# classifiers = [
#     'Development Status :: 5 - Production/Stable',
#     'Intended Audience :: Education',
#     'Operating System :: Microsoft :: Windows :: Windows 10',
#     'License :: OSI Approved :: MIT License',
#     'Programming Language :: Python :: 3'
# ]

# setup(
#     name='stlpy',
#     version='0.0.1',
#     description="A Helpful and easy to use library",
#     long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
#     url='',
#     author='Rudransh & Shashwat',
#     author_email='aarti19830@gmail.com',
#     license='MIT',
#     classifiers=classifiers,
#     keywords='dsa',
#     packages=find_packages,
#     install_requires=['']
# )

from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="stlpy",
    version="0.0.1",
    description=" Standard Template Library in Python and easy to use for C++ developers",
    long_description=readme(),
    #long_description_content_type="text/markdown",
    url="https://github.com/asrlogistics/stlpy",
    author="Rudransh Bhardwaj",
    author_email="aarti19830@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["stlpy"],
    include_package_data=True,
    install_requires=["math","numpy","itertools","collections"],
    entry_points={
        "console_scripts": [
            "stl=doc.stlpy:main",
        ]
    },
)