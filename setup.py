from setuptools import find_packages, setup


def read_version(module_name):
    from re import match, S
    from os.path import join, dirname

    with open(join(dirname(__file__), module_name, "__init__.py")) as f:
        return match(r".*__version__.*('|\")(.*?)('|\")", f.read(), S).group(2)


setup(
    name="dilami_calendar",
    version=read_version("dilami_calendar"),
    description="Dilami (Gilaki) calendar for python",
    keywords=(
        "dilami deylami daylami gilaki calendar datetime date time conversion"
    ),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="http://github.com/jangal/python-dilami-calendar",
    author="Jangal",
    install_requires=["khayyam~=3.0.17"],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Localization",
    ],
    packages=find_packages(),
)
