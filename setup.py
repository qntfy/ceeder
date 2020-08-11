from setuptools import find_packages, setup

NAME = "seeder"
PACKAGES = find_packages(where="src")


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name=NAME,
    version="0.0.1",
    author="max thomas",
    author_email="max@qntfy.com",
    description="Utility library for working with the CDR document format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qntfy/ceeder",
    install_requires=[
        'falcon',
        'jsonschema',
    ],
    packages=PACKAGES,
    package_dir={"": "src"},
    package_data={'': ['*.json']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
