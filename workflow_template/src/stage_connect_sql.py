"""Stage for connecting to the sql server.
"""
from base_stage import BaseStage
from configuration import run_configuration

import constants

import argparse
import logging
import sqlite3


class ConnectSqlStage(BaseStage):
    """Stage for connecting to sql servers.
    """
    name = "connect_sql"
    logger = logging.getLogger("pipeline").getChild("sql")

    def pre_run(self, args):
        """The function that is executed before the stage is run.

        Args:
            args: command line arguments that are passed to the stage.
        """
        self.logger.info("=" * 40)
        self.logger.info("Executing connect SQL stage")
        self.logger.info("-" * 40)

    def run(self, args):
        """Connects with provided sql server and adds the connection to the parent stage.

        Args:
            args: arguments that are passed to the stage.

        Returns:
            True if the stage execution succeded, False otherwise.
        """
        self.logger.info("Initiating connection")

        connection = sqlite3.connect(constants.DATABASE_FILE)
        cursor = connection.cursor()

        self.logger.info("Connection established")

        if not self.parent:
            self.logger.warning("This stage should not be executed on its own.")
            connection.close()
        else:
            self.parent.sql_connection = connection
            self.parent.sql_cursor = cursor


        return True

    def post_run(self, args):
        """The function that is executed after the stage is run successfully.

        Args:
            args: command line arguments that are passed to the stage.
        """
        self.logger.info("-" * 40)
        self.logger.info("Finished connect SQL stage")
        self.logger.info("=" * 40)

    def get_argument_parser(self, use_shared_parser=False, add_help=False):
        """Returns Argument Parser to use for the stage.

        Args:
            use_shared_parser: whether to use shared parser as parent.
            add_help: whether to add help.
        """
        parser = self.get_base_argument_parser(use_shared_parser, add_help,
                                               "Connect to SQL stage.")
        return parser
