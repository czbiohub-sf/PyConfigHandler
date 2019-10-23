"""TEST SCRIPT TO EVALUATE LOGGING BEHAVIOR

Do not call script from an outside directory.
"""

import logging
from enum import Enum
from pyconfighandler import validateConfig

logging.basicConfig(level=logging.DEBUG)

class REQUIRED_FIELD(Enum):
    TEST_BOOL = 0

config_path = '../ExampleConfigFiles/testing_configfile.config'

config, opts = validateConfig(config_path, REQUIRED_FIELD)
