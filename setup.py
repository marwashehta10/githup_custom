from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in app_custom/__init__.py
from app_custom import __version__ as version

setup(
	name="app_custom",
	version=version,
	description="It is a custom app",
	author="marwa",
	author_email="marwa@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
