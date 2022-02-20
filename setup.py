from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Get real ip if you are in cgn pool'
LONG_DESCRIPTION = 'Provides port forwarding for ip addresses in the cgn pool'

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="cgn_realip",                    
    version=VERSION,                        
    author="Sinan Kanidagli",                     
    description=DESCRIPTION,
    long_description=long_description,     
    long_description_content_type="text/markdown",
    packages=find_packages(),   
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      
    python_requires='>=3.6',               
    py_modules=["cgn_realip"],            
    package_dir={'':'cgn_realip/src'},     
    install_requires=['netifaces', 'js2py', 'requests']                    
)
