"""Stage that executes sql script.
"""
from base_stage import BaseStage
from configuration import run_configuration

import constants

from os.path import join

import argparse
import csv
import logging
import sqlite3


class SqlScriptStage(BaseStage):
    """Stage executing SQL.
    """
    name = "sql_script"
    logger = logging.getLogger("pipeline").getChild("sql_script")

    def __init__(self, parent=None, sql_script=None):
        """Initializer for SQL script stage

        Args:
            parent: the parent stage
            sql_script: name of the sql script to execute
        """
        self.parent = parent
        self.sql_script = sql_script

    def pre_run(self, args):
        """The function that is executed before the stage is run.

        Args:
            args: command line arguments that are passed to the stage.
        """
        self.logger.info("=" * 40)
        self.logger.info("Executing SQL script {}".format(self.sql_script))
        self.logger.info("-" * 40)

    def run(self, args):
        """Connects with provided sql server and adds the connection to the parent stage.

        Args:
            args: arguments that are passed to the stage.

        Returns:
            True if the stage execution succeded, False otherwise.
        """
        if not self.parent:
            self.logger.warning("This stage cannot be executed on its own.")
            return False

        script_filepath = join(constants.SQL_SCRIPTS_PATH, "{}.sql".format(self.sql_script))
        output_filepath = join(constants.OUTPUT_PATH, "{}.csv".format(self.sql_script))
        self.logger.info("Lodaing the sql script")
        with open(script_filepath, "r") as script_file:
            scripts = "".join(script_file.readlines()).split(";")[:-1]
            self.logger.info("Executing the sql script")
            for script in scripts:
                self.parent.sql_cursor.execute(script)
                results = self.parent.sql_cursor.fetchall()

                if results:
                    self.logger.info("Saving execution result to the file.")
                    with open(output_filepath, "w") as output_file:
                        csv.writer(output_file).writerows(results)

        return True

    def post_run(self, args):
        """The function that is executed after the stage is run successfully.

        Args:
            args: command line arguments that are passed to the stage.
        """
        self.logger.info("-" * 40)
        self.logger.info("Finished SQL script {}".format(self.sql_script))
        self.logger.info("=" * 40)

    def get_argument_parser(self, use_shared_parser=False, add_help=False):
        """Returns Argument Parser to use for the stage.

        Args:
            use_shared_parser: whether to use shared parser as parent.
            add_help: whether to add help.
        """
        parser = self.get_base_argument_parser(use_shared_parser, add_help,
                                               "Execute {} SQL script.".format(self.sql_script))
        return parser
