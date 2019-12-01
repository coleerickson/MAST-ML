########################################################################
# This is the setup script for the MAterials Simulation Toolkit
#   machine-learning module (MASTML)
# Creator: Tam Mayeshiba
# Maintainer: Robert Max Williams
# Last updated: 2018-06-20
#  _________________________________
# / No one knows where the original \
# \ setup.py came from.             /
#  ---------------------------------
#         \   ^__^
#          \  (oo)\_______
#             (__)\       )\/\
#                 ||----w |
#                 ||     ||
########################################################################

from __future__ import print_function
import sys
from setuptools import setup, find_packages

###Python version check
#print "Python version detected: %s" % sys.version_info
if sys.version_info[0] < 3:
    print('Python Version %d.%d.%d found' % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))
    print('Python version >= 3 needed!')
    sys.exit(0)

#print("Python version 3.6.6 is REQUIRED")
#print("Check with `python --version`")

# One of the techniques from https://packaging.python.org/guides/single-sourcing-package-version/
verstr = "unknown"
try:
    verstr = open("VERSION", "rt").read().strip()
except EnvironmentError:
    pass # Okay, there is no version file.

setup(
    name="mastml", # TODO  should this be MAST-ML?
    packages=find_packages(),
    package_data={'mastml.magpie': ["*.*"], 'mastml.tests': ["*.*"], 'mastml.tests.conf' : ["example_input.conf", "MASTML_fullinputfile.conf"], 'mastml.tests.csv' : ["example_data.csv"]},
    include_package_data = True,
    version=verstr,
    install_requires=[
        "aflow",
        "atomicwrites",
        "attrs",
        "certifi",
        "chardet",
        "citeproc-py",
        "cycler",
        "Cython",
        "decorator",
        "dominate",
        "forestci",
        "globus_nexus_client",
        "globus_sdk",
        "httplib2",
        "idna",
        "importlib-metadata",
        "ipython-genutils",
        "jdcal",
        "jsonschema",
        "keras",
        "kiwisolver",
        "matminer",
        "matplotlib",
        "mdf_forge",
        "mdf-toolbox",
        "mlxtend",
        "monty",
        "nbformat",
        "networkx",
        "nose",
        "numpy",
        "openpyxl",
        "packaging",
        "palettable",
        "pandas",
        "pint",
        "plotly",
        "pluggy",
        "py",
        "PyDispatcher",
        "pymatgen",
        "pymongo",
        "pyparsing",
        "pypif",
        "pytest",
        "python-dateutil",
        "pytz",
        "pyyaml",
        "requests",
        "retrying",
        "ruamel.yaml",
        "scikit-learn",
        "scikit-optimize",
        "scipy",
        "six",
        "spglib",
        "sympy",
        "tabulate",
        "tensorflow",
        "tqdm",
        "traitlets",
        "urllib3",
        "wcwidth",
        "xgboost",
        "xlrd",
        "zipp"],
    author="MAST Development Team, University of Wisconsin-Madison Computational Materials Group",
    author_email="ddmorgan@wisc.edu",
    url="https://github.com/uw-cmg/MAST-ML",
    license="MIT",
    description="MAterials Simulation Toolkit - Machine Learning",
    long_description="MAterials Simulation Toolkit for Machine Learning (MASTML)",
    keywords=["MAST","materials","simulation","MASTML","machine learning"],
)
