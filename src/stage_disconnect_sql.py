"""Stage for disconnecting from the sql server.
"""
from base_stage import BaseStage
from configuration import run_configuration

import argparse
import logging


class DisconnectSqlStage(BaseStage):
    """Stage for disconnecting from the sql server.
    """
    name = "disconnect_sql"
    logger = logging.getLogger("pipeline").getChild("sql")

    def pre_run(self, args):
        """The function that is executed before the stage is run.

        Args:
            args: command line arguments that are passed to the stage.
        """
        self.logger.info("=" * 40)
        self.logger.info("Executing disconnect SQL stage")
        self.logger.info("-" * 40)

    def run(self, args):
        """Connects with provided sql server and adds the connection to the parent stage.

        Args:
            args: arguments that are passed to the stage.

        Returns:
            True if the stage execution succeded, False otherwise.
        """
        if not self.parent:
            self.logger.warning("This stage should not be executed on its own.")
            self.logger.info("Since this stage was run on its own, there is nothing to disconnect.")
            return True

        self.parent.sql_connection.close()
        self.logger.info("Disconnection successfull")

        return True

    def post_run(self, args):
        """The function that is executed after the stage is run successfully.

        Args:
            args: command line arguments that are passed to the stage.
        """
        self.logger.info("-" * 40)
        self.logger.info("Finished disconnecting SQL stage")
        self.logger.info("=" * 40)

    def get_argument_parser(self, use_shared_parser=False, add_help=False):
        """Returns Argument Parser to use for the stage.

        Args:
            use_shared_parser: whether to use shared parser as parent.
            add_help: whether to add help.
        """
        parser = self.get_base_argument_parser(use_shared_parser, add_help,
                                               "Disconnect from the SQL stage.")
        return parser
