from setuptools import setup, find_packages


setup(
    name='darksouls',
    version='0.0',
    packages=find_packages(),
    install_requires=[
        'aiohttp>=3.2.1',
        'lxml>=4.2.1',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
