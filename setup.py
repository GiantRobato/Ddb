from setuptools import setup, find_packages

setup(
    name="ddb",
    version="0.0.1",
    packages=find_packages(exclude=['tests']),
    # metadata for upload to PyPI
    author="Dustin Mendoza",
    author_email="dmendoza64@gmail.com",
    description="DDB is a database made by Dustin and stands for Dustins DataBase",
    license="MIT",
    keywords="database nosql",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Topic :: Database",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent"
    ],
    tests_require=['pytest-cov']
)