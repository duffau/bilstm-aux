import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="bilstm_aux",
    version="1.0.0",
    description="Bidirectional Long-Short Term Memory sequence tagger.",
    url="https://github.com/bplank/bilstm-aux",
    packages=['bilstm_aux', 'bilstm_aux.lib'],
    install_requires=['dyNET>=2.1', 'numpy>=1.16.0', 'scipy>=1.2.0', 'dill>=0.2.8.2'],
    long_description=read('README.md'),
)
