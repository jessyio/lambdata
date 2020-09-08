'''lambdata: a collection of data science helper functions
'''
import setuptools

REQUIRED = [
    'numpy'
    'pandas'
]

with open("README.md", 'r') as fh:
    LONG_DESCRIPTION = fh.read()

#how to setup a python package
setuptools.setup(
    name='lambdata-jessyio',
    version='0.0.1',
    author='jessyio',
    description="A collection of Data Science helper functions",
    long_description=LONG_DESCRIPTION,
    long_description_content="text/markdown",
    url="https://github.com/jessyio/lambdata",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
