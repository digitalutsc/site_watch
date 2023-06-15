from setuptools import setup, find_packages

setup(
    name='SiteWatch',
    author='Hassan El-Sheikha',
    description='An Islandora site monitoring tool',
    url='https://github.com/digitalutsc/site_watch',
    install_requires=[
        'colorama',
        'openpyxl',
        'requests',
        'rich',
        "ruamel.yaml<=0.17.21",
        'selenium',
    ],
    packages=find_packages(),
)
