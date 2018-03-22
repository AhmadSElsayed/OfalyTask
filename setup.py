from setuptools import setup

setup(
	name = 'Facebook User Scrapper',
	version='0.1',
    long_description=__doc__,
    packages=['src'],
	include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
