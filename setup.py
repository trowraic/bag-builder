from setuptools import setup

setup(name='bag-builder',
      version='0.1',
      description='build BagIt container',
      author='LZV.nrw',
      install_requires=[
          'bagit',
      ],
      packages=['bag-builder'])