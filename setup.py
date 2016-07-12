from setuptools import setup, find_packages

setup(
    name="nbgen",
    version="0.1",
    packages=find_packages(exclude=["sample.py"]),
    entry_points={
        'console_scripts': [
            'nbgen = nbgen:main',
        ],
    },
    install_requires=['jupyter', 'docopt'],
)
