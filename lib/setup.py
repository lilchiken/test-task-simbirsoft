from setuptools import find_packages, setup

with open('.version') as f:
    version = f.read().strip()

setup(
    name='src_lib',
    description='Library using in src',
    version=version,
    packages=find_packages(),
    python_requires=">=3.8",
    zip_safe=False
)
