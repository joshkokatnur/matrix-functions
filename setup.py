from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="matrixfunctions",
    version="0.0.4",
    author="Josh Kokatnur",
    author_email="jkokatnur@gmail.com",
    description="A package that adds matrix functions.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/joshkokatnur/matrixfunctions",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
)
