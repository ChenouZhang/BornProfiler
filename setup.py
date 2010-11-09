# setuptools installation of APBS BornProfiler
# Copyright (c) 2005-2010 Oliver Beckstein <orbeckst@gmail.com>
#                         Kaihsu Tai <k@kauha.eu>
# Released under the GNU Public License 3 (or higher, your choice)
# See the file COPYING for details.

from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name="APBS-BornProfiler",
      version="0.1",
      description="Setting up of Born profile calculations for APBS",
      long_description="""
""",
      author="Oliver Beckstein",
      author_email="orbeckst@gmail.com",
      license="GPLv3",
      url="http://sbcb.bioch.ox.ac.uk/oliver/software/",
      keywords="science",
      packages=find_packages(exclude=[]),
      package_data = {},
      scripts = ["scripts/apbs-bornprofile-analyze.py",
                 "scripts/apbs-bornprofile-placeion.py",
                 "scripts/apbs-mem-setup.py",
                 ],
      install_requires=['numpy>=1.0.3',
                        ], 
      zip_safe=True,
)
