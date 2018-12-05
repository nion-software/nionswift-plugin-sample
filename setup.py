# -*- coding: utf-8 -*-

"""
To upload to PyPI, PyPI test, or a local server:
python setup.py bdist_wheel upload -r <server_identifier>
"""

import setuptools

setuptools.setup(
    name="nionswift-plugin-sample",
    version="0.1.0",
    author="Your Name",
    author_email="your@email.com",
    description="Description.",
    long_description=open("README.rst").read(),
    url="https://github.com/your-organization/your-project",
    packages=["nionswift_plugin.sample", "nionswift_plugin.sample.test"],
    license='GPLv3',
    include_package_data=True,
    python_requires='~=3.5',
    zip_safe=False,
)
