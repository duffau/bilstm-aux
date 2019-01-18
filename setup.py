import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="bilstm_aux",
    version="1.0.0",
    description="Bidirectional Long-Short Term Memory sequence tagger.",
    url="https://github.com/bplank/bilstm-aux",
    packages=['src'],
    install_requires=['dyNET>=2.1', 'numpy>=1.16.0', 'scipy>=1.2.0'],
    long_description=read('README.md'),
)
