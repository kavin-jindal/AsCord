from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.5'
DESCRIPTION = 'Generating Python Discord bots'
LONG_DESCRIPTION = '# Helps is generating ready-made discord bots in python easily.'

# Setting up
setup(
    name="ascord",
    version=VERSION,
    author="Kavin Jindal",
    author_email="kavinsjindal@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description= long_description,
    packages=find_packages(),
    install_requires=['discord'],
    keywords=['python','discord', 'discord.py', 'discord bots', 'discord python', 'bots'],
    classifiers=[
        "Development Status :: 7 - Inactive",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)