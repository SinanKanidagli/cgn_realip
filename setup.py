from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Get real ip if you are in cgn pool'
LONG_DESCRIPTION = 'Provides port forwarding for ip addresses in the cgn pool'

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="cgn_realip",                    # This is the name of the package
    version=VERSION,                        # The initial release version
    author="Sinan Kanidagli",                     # Full name of the author
    description=DESCRIPTION,
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["cgn_realip"],             # Name of the python package
    package_dir={'':'cgn_realip/src'},     # Directory of the source code of the package
    install_requires=['netifaces', 'js2py', 'requests']                     # Install other dependencies if any
)