from setuptools import setup, find_packages
#Python library that helps us package and distribute Python projects
#setup() - provides information about your Python package and configures its installation
#find_packages() - automatically discovers Python packages inside your project

setup(
    name="vehicle-insurance",
    version="0.0.1",
    author="Vishal Harti",
    packages=find_packages(),
    install_requires=[]
)

#folder containing __init__ will be called as package
#__init__.py helps Python treat the directory as a regular package
