import unittest
import os
import sys
import shutil
import warnings

""" 
Like the smoke tests in unit_tests.py but without the testing lib
so that pycallgraph makes a pretty graph. Run:
`pycallgraph graphviz -- example_run.py`
to make a cool graph after you install those with pip and a package mngr
"""

# so we can find MASTML package
sys.path.append('../')

import MASTML
import MASTMLInitializer

class SmokeTest(object):

    def setUp(self):
        self.folders = list()

    def test_full_run(self):
        configfile = 'full_run.conf'
        warnings.simplefilter('ignore')
        MASTML.MASTMLDriver(configfile=configfile).run_MASTML()
        self.folders.append('results/full_run')

    def test_basic_example(self):
        configfile = 'example_input.conf'
        warnings.simplefilter('ignore')
        MASTMLDriver(configfile=configfile).run_MASTML()
        self.folders.append('results/example_results')

    def test_classifiers(self):
        configfile = 'classifiers.conf'
        warnings.simplefilter('ignore')
        MASTMLDriver(configfile=configfile).run_MASTML()
        self.folders.append('results/classifiers')

    def tearDown(self):
        for f in self.folders:
            pass
            # uncomment for no leftover folders:
            #shutil.rmtree(f)
def leaves_of_dict(dictt):
    """ 
    Returns non-dict elements of dict recursively, as a generator
    """
    for key, val in dictt.items():
        if isinstance(val, dict):
            yield from leaves_of_dict(val)
        else:
            yield val

class ParseTemplate():

    def setUp(self):
        template_folder  = '../MASTML_input_file_template/'
        template_file = 'MASTML_input_file_template.conf'
        self.parser = MASTMLInitializer.ConfigFileParser(template_file)
        self.config_dict = self.parser.get_config_dict(template_folder)

    def test_dict_is_not_empty(self):
        self.assertTrue(0 < len(self.config_dict.keys()))

    def test_dict_values_are_lists_or_strings(self):
        for leaf in leaves_of_dict(self.config_dict):
             # leaf is leaf in the dict way, not in the list way.
             # check if leaf is string or every member of leaf is string
             self.assertTrue(isinstance(leaf, str) or
                             all(isinstance(x, str) for x in leaf))

    def tearDown(self):
        pass

class TestConfigKeys(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

if __name__=='__main__':
    s = SmokeTest()
    s.setUp()
    s.test_full_run()
