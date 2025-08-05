from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()  #It will read the file and split it into a list of requirements

setup(
    name="Australia_weather_rain_prediction",
    version="0.1",
    author="Sachit",
    packages = find_packages(),
    install_requires = requirements,
)