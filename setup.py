# setup.py
from setuptools import setup, find_packages

setup(
    name='tokviz',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'transformers',
        'IPython'
    ],
    author='Deepak Gupta',
    author_email='deepak.gupta.h401@gmail.com',
    description='Library for visualizing tokenization patterns across different language models',
    url='https://github.com/Mr-DG-Wick/tokviz',
)
