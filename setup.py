import re
import os
from setuptools import find_packages, setup

# reading package version (same way sqlalchemy does)
with open(os.path.join(os.path.dirname(__file__), 'deylami_calendar', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)


setup(
    name="deylami_calendar",
    version=package_version,
    author="Jangal",
    install_requires=[
        'khayyam~=3.0.17'
    ],
    packages=find_packages()
)
