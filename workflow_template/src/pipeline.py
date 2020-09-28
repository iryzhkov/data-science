"""Data pipeline / workflow.
"""
from base_stage import BaseStage
from configuration import run_configuration
from stage_download import DownloadStage
from stage_sql_script import SqlScriptStage
from stage_connect_sql import ConnectSqlStage
from stage_disconnect_sql import DisconnectSqlStage

import constants
import shared_argument_parser

from os.path import join

import logging
import argparse


class Pipeline(BaseStage):
    """A class for the whole data pipeline / workflow
    """
    logger = logging.getLogger("pipeline")

    def __init__(self, parent=None):
        """Init function for the pipeline.

        Args:
            parent: parent stage.
        """
        self.parent = parent
        self.stages = [
            ConnectSqlStage(self),
            #DownloadStage(self),
            SqlScriptStage(self, "demo_script"),
            DisconnectSqlStage(self),
        ]
        self.stages_dict = {stage.name:stage for stage in self.stages}
        self.stages_executed = {stage.name:False for stage in self.stages}

    def get_argument_parser(self):
        """Returns argument parser for the pipeline / workflow.
        """
        parents = [stage.get_argument_parser() for stage in self.stages]
        parents.append(shared_argument_parser.get_argument_parser(False))
        parser = argparse.ArgumentParser(parents=parents, description="Data workflow / pipeline")

        stage_names = [stage.name for stage in self.stages]
        parser.add_argument("--stage", help="list of stages to execute in the workflow / pipeline",
                            choices=stage_names, nargs="+", default=stage_names)
        return parser

    def pre_run(self, args):
        """The function that is executed before the pipeline / workflow is run.

        Args:
            args: command line arguments that are passed to the workflow.
        """
        self.logger.info("=" * 40)
        self.logger.info("-" * 40)
        self.logger.info("Starting data pipeline / workflow")
        self.logger.info("Stages to execute: {}".format(args.stage))
        self.logger.info("-" * 40)
        self.logger.info("=" * 40)

    def run(self, args):
        """Run the stages specified in the stage argument.

        Args:
            args: arguments that are passed to the workflow / pipeline.

        Returns:
            True if the workflow / pipeline execution succeded, False otherwise.
        """
        for stage in args.stage:
            self.logger.info("Executing stage '{}'".format(stage))
            if self.stages_executed[stage]:
                self.logger.warning("Executing stage '{}' more than once".format(stage))
            if not self.stages_dict[stage].execute(args):
                return False
            self.stages_executed[stage] = True

        return True

if __name__ == "__main__":
    pipeline = Pipeline()
    argument_parser = pipeline.get_argument_parser()

    args = argument_parser.parse_args()
    run_configuration(args)
    pipeline.execute(args)
