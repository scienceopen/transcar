#!/usr/bin/env python
install_requires=['python-dateutil','pytz','pandas','transcarread']
tests_require=['pytest','nose','coveralls']
# %%
from setuptools import setup,find_packages
import subprocess

setup(name='transcar',
      packages=find_packages(),
      version='0.2.0',
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/transcar',
      classifiers=[
      'Intended Audience :: Science/Research',
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: MIT License',
      'Topic :: Scientific/Engineering :: Atmospheric Science',
      'Programming Language :: Python :: 3',
      ],
      python_requires='>=3.6',
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'tests':tests_require,},
      scripts=['RunTranscar.py'],
	  )

subprocess.check_call(['cmake','..'],cwd='dir.source/dir.obj')
subprocess.check_call(['make'],cwd='dir.source/dir.obj')
