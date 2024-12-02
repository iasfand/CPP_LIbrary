from setuptools import setup, find_packages

setup(
    name="airport_processor",
    version="0.1.0",
    description="A library for processing airport data and checking favorite status using Flask and DynamoDB",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Asfand",
    author_email="x23358530@student.ncirl.ie",
    url="https://github.com/iasfand/CPP_LIbrary",
    packages=find_packages(),
    install_requires=[
        "boto3",
        "flask",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
