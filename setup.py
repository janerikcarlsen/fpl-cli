import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
        "requests",
        "future",
        "click",
        "pyfiglet",   
        "six", 
        "Prettytable",
        "termcolor", 
        "colorama",
        "configparser"
    ]

setuptools.setup(
    name="fplcli",
    version="0.1.9",
    author="Jan-Erik Carlsen",
    author_email="jan.erik.carlsen@gmail.com",
    description="A CLI tool for Fantasy Premier League",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/janerikcarlsen/fpl-cli",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'fpl=fplcli.cli:main',
        ],
    }, 
    project_urls={
        "Docs": "https://pypi.org/project/fplcli/",
        "Source": "https://github.com/janerikcarlsen/fpl-cli"
    },
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment",
    ],
    install_requires=install_requires,
)