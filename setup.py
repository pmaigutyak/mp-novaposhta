
from setuptools import setup, find_packages

from novaposhta import __version__


setup(
    name='django-novaposhta',
    version=__version__,
    description='',
    long_description=open('README.md').read(),
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url='https://github.com/pmaigutyak/mp-novaposhta',
    download_url='https://github.com/pmaigutyak/mp-novaposhta/archive/%s.tar.gz' % __version__,
    packages=find_packages(),
    license='MIT',
    install_requires=[
        'django-model-search'
    ]
)
