# -*- coding: utf-8 -*-

"""Top-level package for cheese_shop."""

import os
import logging.config
import yaml

__author__ = """Herbert Beemster"""
__email__ = 'herbert@example.com'
__version__ = '0.1.0'


def setup_logging(filename='logging.yaml', default_level=logging.INFO):
    """setup logging configuration"""
    if os.path.exists(filename):
        with open(filename, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

    logger = logging.getLogger(__name__)
    logger.info(75 * '-')
    logger.info('Logging started')
    logger.info(75 * '-')
