from setuptools import setup

setup(
    name='SiteWatch',
    version='1.0',
    author='Hassan El-Sheikha',
    description='An Islandora site monitoring tool',
    url='https://github.com/digitalutsc/site_watch',
    install_requires=[
        'colorama',
        'openpyxl',
        'requests',
        'rich',
        'ruamel.base',
        'selenium',
    ],
)