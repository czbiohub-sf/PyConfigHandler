import unittest
from enum import Enum, auto
from pyconfighandler import validateConfig

class REQUIRED_DEFAULT_FIELDS(Enum):
    TEST_BOOL       = auto()
    TEST_BOOL2      = auto()
    TEST_INT        = auto()
    TEST_FLOAT      = auto()
    TEST_STRING     = auto()
    TEST_BASE       = auto()


class MISSING_FIELD(Enum):
    TEST_BOOL       = auto()
    TEST_BOOL2      = auto()
    TEST_INT        = auto()
    TEST_FLOAT      = auto()
    TEST_STRING     = auto()
    TEST_BASE       = auto()
    TEST_MISSING    = auto()


class ConfigurationParser(unittest.TestCase):

    def setUp(self):
        self.config_path = 'ExampleConfigFiles/testing_configfile.config'

    def test_keys_present(self):
        config, opts = validateConfig(self.config_path,
                                      REQUIRED_DEFAULT_FIELDS)

    def test_key_not_present(self):
        caught_error = False
        try:
            validateConfig(self.config_path, MISSING_FIELD)
        except KeyError:
            caught_error = True
        self.assertTrue(caught_error)

    def test_file_not_found(self):
        caught_error = False
        fake_file = 'fake_file.123'
        self.config_path = fake_file
        try:
            validateConfig(self.config_path, REQUIRED_DEFAULT_FIELDS)
        except ValueError:
            caught_error = True
        self.assertTrue(caught_error)

    def test_extended_interpolation(self):
        config, opts = validateConfig(self.config_path,
                                      REQUIRED_DEFAULT_FIELDS)
        test_string = config[opts[-1]]['TEST_EXTENDED']
        self.assertEqual(test_string, '/home/fake.py')

    def test_type_conversions(self):
        config, opts = validateConfig(self.config_path,
                                      REQUIRED_DEFAULT_FIELDS)
        bl1 = config['DEFAULT'].getboolean('TEST_BOOL')
        self.assertEqual(bool, type(bl1))

        bl2 = config['DEFAULT'].getboolean('TEST_BOOL2')
        self.assertEqual(bool, type(bl2))

        int1 = config['DEFAULT'].getint('TEST_INT')
        self.assertEqual(int, type(int1))

        float1 = config['DEFAULT'].getfloat('TEST_FLOAT')
        self.assertEqual(float, type(float1))

        str1 = config['DEFAULT']['TEST_STRING']
        self.assertEqual(str, type(str1))

    def test_section_override_default(self):
        config, opts = validateConfig(self.config_path,
                                      REQUIRED_DEFAULT_FIELDS)
        orig = config['DEFAULT']['TEST_INT']
        ovrrd = config['TEST1']['TEST_INT']
        self.assertNotEqual(orig, ovrrd)

    def test_find_field_not_in_default(self):
        new_item = []
        item_found = False
        config, opts = validateConfig(self.config_path,
                                      REQUIRED_DEFAULT_FIELDS)

        new_item = config[opts[0]]['TEST_NEW']
        if new_item != []:
            item_found = True
        self.assertTrue(item_found)
