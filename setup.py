from setuptools import find_packages, setup

NAME = "seeder"
PACKAGES = find_packages(where="src")

setup(
    name=NAME,
    install_requires=[
        'falcon',
        'jsonschema',
    ],
    packages=PACKAGES,
    package_dir={"": "src"},
    package_data={'': ['*.json']},
)
