# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

NAME = "unipayment"
VERSION = "1.1.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    description="UniPayment python api",
    auther="UniPayment.io",
    auther_email="develop@unipayment.io",
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UniCryptoLab/UniPaymentClient.Python"
)
