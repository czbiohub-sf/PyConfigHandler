"""Utilities for validating and extracting configuration file settings."""

import configparser
import logging
from logging import NullHandler
from enum import Enum
from os import path

LOG = logging.getLogger(__name__)
LOG.addHandler(NullHandler())


def validateConfig(path_to_config: str, required_config_fields: Enum):
    """Parse and validate a configuration file.

    Method enforces configuration files to abide to a specified format. If
    required fields are not present in the DEFAULT section of the config file,
    no further processing will be possible. If required fields are present,
    the file is converted into a config object that can be processed further in
    the main program and non-default configuration modes are returned to the
    caller, if present.

    Parameters
    ----------
    path_to_config : str
        Path to configuration file to be validated
    required_config_fields : Enum
        Evaluate config file for the presence of required default fields

    Returns
    -------
    config
        Configuration object to be parsed in main program
    config_options : list
        A list of section names that are identified in the config file

    """
    LOG.info('Validating config file: %s', path_to_config)
    if not path.isfile(path_to_config):
        raise ValueError('Input `%s` is not a file.' % path_to_config)
    interp = configparser.ExtendedInterpolation()
    config = configparser.ConfigParser(interpolation=interp)
    config.read(path_to_config)
    for field in required_config_fields:
        if field.name not in config['DEFAULT']:
            raise KeyError('Field `%s` not found in config file.' % field)

    config_options = config.sections()
    LOG.info('Config file `%s` validated.', path_to_config)
    LOG.info('Config options found: %s', str(config_options))

    return config, config_options
