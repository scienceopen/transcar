#!/usr/bin/env python3

from setuptools import setup
import subprocess

with open('README.rst','r') as f:
    long_description = f.read()

setup(name='transcar',
      version='0.1',
	  description='Transcar 1-D flux tube model',
	  long_description=long_description,
	  author='Michael Hirsch',
	  url='https://github.com/scienceopen/transcar',
      dependency_links = ['https://github.com/scienceopen/histutils/tarball/master#egg=histutils',
                          'https://github.com/scienceopen/transcarread/tarball/master#egg=transcarread'],
	  install_requires=['histutils','transcarread'],
      packages=['transcar'],
	  )
	  
try:
    subprocess.run(['conda','install','--yes','--quiet','--file','requirements.txt'])
except Exception as e:
    print('you will need to install packages in requirements.txt  {}'.format(e))
    with open('requirements.txt','r') as f:
        print(f.read())	  
