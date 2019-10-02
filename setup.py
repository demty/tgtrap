from os.path import dirname, join

from setuptools import find_packages, setup

raise NotImplementedError

setup(
    name='example_package',
    packages=find_packages(),
    version='1.0.1',
    description='some text',
    author='author_creds',
    author_email='author@email.com',
    long_description=open(join(dirname(__file__), 'README.md'), encoding='utf-8').read(),
    keywords='template',
    url="template_url",
    install_requires=[

    ],
)
