"""Stage for downloading the data from the internet.
"""
from base_stage import BaseStage
from configuration import run_configuration

import argparse
import logging
import time


class DownloadStage(BaseStage):
    """Stage for downloading the data from the internet.
    """
    name = "download"
    logger = logging.getLogger("workflow").getChild("download_stage")

    def pre_run(self, args):
        """The function that is executed before the stage is run.

        Args:
            args: command line arguments that are passed to the stage.
        """
        self.logger.info("=" * 40)
        self.logger.info("Executing download stage")
        self.logger.info("Using following arguments:")
        self.logger.info("\tURL for data downloading: {}".format(args.url))
        self.logger.info("-" * 40)

    def run(self, args):
        """Downloads the csv file from the url.

        Args:
            args: arguments that are passed to the stage.

        Returns:
            True if the stage execution succeded, False otherwise.
        """
        self.logger.info("Starting download")
        time.sleep(1)
        self.logger.info("Download finished")
        return True

    def post_run(self, args):
        """The function that is executed after the stage is run successfully.

        Args:
            args: command line arguments that are passed to the stage.
        """
        self.logger.info("-" * 40)
        self.logger.info("Finished download stage")
        self.logger.info("=" * 40)

    def get_argument_parser(self, use_shared_parser=False, add_help=False):
        """Returns Argument Parser to use for the stage.

        Args:
            use_shared_parser: whether to use shared parser as parent.
            add_help: whether to add help.
        """
        parser = self.get_base_argument_parser(use_shared_parser, add_help,
                                               "Download stage of the pipeline / workflow")
        parser.add_argument("--url", help="url for data downloading.", default="www.google.com")
        return parser


if __name__ == "__main__":
    download_stage = DownloadStage()
    argument_parser = download_stage.get_argument_parser(True, True)

    args = argument_parser.parse_args()
    run_configuration(args)
    download_stage.execute(args)
