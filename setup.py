from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name = "Economic Decision-Making",
    description = "A data wrangling and transformation pipeline for a series of studies of economic decision-making.",
    version = "0.4.2",
    install_requires = required
    # ...
)