"""Base argument parser for the workflow.
"""
from enum import Enum

import argparse
import logging

def get_argument_parser(add_help=False):
    """Creates base argument parser for the workflow.

    Args:
        use_shared_parser: whether to use shared parser as parent.
        add_help: whether to add help.
    """
    parser = argparse.ArgumentParser(add_help=add_help)
    parser.add_argument("--debug", action="store_true",
                        help="run the workflow in the debug mode")
    return parser
