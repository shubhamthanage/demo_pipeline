"""
thi file shows how to create the packge from the specific foloder
pre-requisite- make __init__.py file in the folder whhich we want to make a package
"""

from setuptools import setup, find_packages

setup(name="cesus-income1",
      version="0.0.1",
      author="shubham",
      author_email="shubhamthanage1@gmail.com",
      packages=find_packages(),
      insall_requires=["pandas", "numpy", "flask"]
      )