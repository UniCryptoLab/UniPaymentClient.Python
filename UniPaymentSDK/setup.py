from setuptools import setup, find_packages

NAME = "unipayment"
VERSION = "2.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools


REQUIRES = ["urllib3 >= 2.2.2", "six >= 1.16.0", "certifi >= 2024.7.4", "python-dateutil >= 2.9.0",
            "setuptools >= 71.1.0", "dataclasses-json ~= 0.6.7"]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    description="UniPayment Python SDK",
    auther="UniPayment.io",
    auther_email="develop@unipayment.io",
    install_requires=REQUIRES,
    packages=find_packages(exclude=("test",)),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UniCryptoLab/UniPaymentClient.Python"
)
