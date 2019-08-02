import re
import os
from setuptools import find_packages, setup

# reading package version (same way sqlalchemy does)
with open(os.path.join(os.path.dirname(__file__), 'deylami_calendar', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)


setup(
    name="deylami_calendar",
    version=package_version,
    description='Deylami (Gilaki) calendar for python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/jangal/python-deylami-calendar',
    author="Jangal",
    install_requires=[
        'khayyam~=3.0.17'
    ],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Localization"
    ],
    packages=find_packages()
)
