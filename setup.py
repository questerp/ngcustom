from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ngcustom/__init__.py
from ngcustom import __version__ as version

setup(
	name="ngcustom",
	version=version,
	description="NG Custom",
	author="https://twitter.com/LarryDevops",
	author_email="me@larrydevops.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
