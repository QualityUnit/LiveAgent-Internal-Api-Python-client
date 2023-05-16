# coding: utf-8

"""
    LiveAgent Async Event API

    This API is for async event communication  # noqa: E501

    The version of the OpenAPI document: 1.0.8
    Contact: mcivan@qualityunit.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "qu.la-internal"
VERSION = "1.0.8"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3",
    "python-dateutil",
    "aiohttp >= 3.0.0",
    "pydantic >= 1.10.5, < 2",
    "aenum"
]

setup(
    name=NAME,
    version=VERSION,
    description="LiveAgent Async Event API",
    author="OpenAPI Generator community",
    author_email="mcivan@qualityunit.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "LiveAgent Async Event API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    This API is for async event communication  # noqa: E501
    """
)
