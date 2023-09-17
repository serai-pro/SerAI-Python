from setuptools import setup, find_packages

long_description = "A Python package for sending requests to the Thunderbird API."

setup(
    name="SerAI",
    version="1.0",
    description=long_description,
    author="Sergiu",
    author_email="support@serai.pro",
    packages=find_packages(),
    install_requires=[
        "requests",  
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
