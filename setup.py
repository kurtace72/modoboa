#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
"""

from __future__ import unicode_literals

import io
from os import path

from packaging.requirements import Requirement
from setuptools import find_packages, setup


def get_requirements(requirements_file):
    """Parse requirements file."""
    requirements = []
    if path.isfile(requirements_file):
        with io.open(requirements_file, encoding="utf-8") as fp:
            for line in fp:
                if line.startswith("#") or line.strip() == "":
                    continue
                req = Requirement(line)
                if req.marker is None or req.marker.evaluate():
                    requirements.append('%s%s' % (req.name, req.specifier))
    return requirements


if __name__ == "__main__":
    HERE = path.abspath(path.dirname(__file__))
    INSTALL_REQUIRES = get_requirements(path.join(HERE, "requirements.txt"))
    MYSQL_REQUIRES = get_requirements(path.join(HERE, "mysql-requirements.txt"))
    POSTGRESQL_REQUIRES = get_requirements(
        path.join(HERE, "postgresql-requirements.txt"))
    LDAP_REQUIRES = get_requirements(path.join(HERE, "ldap-requirements.txt"))

    with io.open(path.join(HERE, "README.rst"), encoding="utf-8") as readme:
        LONG_DESCRIPTION = readme.read()

    setup(
        name="modoboa",
        description="Mail hosting made simple",
        long_description=LONG_DESCRIPTION,
        license="ISC",
        url="http://modoboa.org/",
        author="Antoine Nguyen",
        author_email="tonio@ngyn.org",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Web Environment",
            "Framework :: Django :: 1.11",
            "Intended Audience :: System Administrators",
            "License :: OSI Approved :: ISC License (ISCL)",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Topic :: Communications :: Email",
            "Topic :: Internet :: WWW/HTTP",
        ],
        keywords="email",
        packages=find_packages(exclude=["doc", "test_data", "test_project"]),
        include_package_data=True,
        zip_safe=False,
        scripts=["bin/modoboa-admin.py"],
        install_requires=INSTALL_REQUIRES,
        use_scm_version=True,
        setup_requires=["setuptools_scm"],
        extras_require={
            "ldap": LDAP_REQUIRES,
            "mysql": MYSQL_REQUIRES,
            "postgresql": POSTGRESQL_REQUIRES,
        },
    )
