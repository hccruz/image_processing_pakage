from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Heraldo",
    author_email="hccruz@gmail.com",
    description=" ",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.9"
)
