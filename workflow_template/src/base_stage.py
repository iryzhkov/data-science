"""Base class for stage template
"""
import shared_argument_parser

import abc
import argparse
import logging

class BaseStage(metaclass=abc.ABCMeta):
    """Base class for stage in the pipeline / workflow
    """
    logger = logging.getLogger("pipeline").getChild("base_stage")
    name = "base"

    def __init__(self, parent=None):
        """The init function.

        Args:
            parent: parent stage.
        """
        self.parent = parent

    def execute(self, args):
        """The function that is called from the outside to execute the stage.

        Args:
            args: command line arguments that are passed to the stage.

        Returns:
            True if the stage execution succeded, False otherwise.
        """
        self.pre_run(args)
        if self.run(args):
            self.post_run(args)
            return True
        else:
            self.on_failure(args)
            return False

    def pre_run(self, args):
        """The function that is executed before the stage is run.

        Args:
            args: command line arguments that are passed to the stage.
        """
        pass

    @abc.abstractmethod
    def run(self, args):
        """Runs the stage.

        Args:
            args: command line arguments that are passed to the stage.

        Returns:
            True if the stage execution succeded, False otherwise.
        """

    def post_run(self, args):
        """The function that is executed after the stage is run successfully.

        Args:
            args: command line arguments that are passed to the stage.
        """
        pass

    def on_failure(self, args):
        """The function that is executed after the stage run failed.

        Args:
            args: command line arguments that are passed to the stage.
        """
        pass

    def get_base_argument_parser(self, use_shared_parser=False, add_help=False, description=""):
        """Returns Argument Parser to use for the stage.

        Args:
            use_shared_parser: whether to use shared parser as parent.
            add_help: whether to add help.
            description: description to use for the parser.
        """
        if use_shared_parser:
            parents = [shared_argument_parser.get_argument_parser(True)]
            return argparse.ArgumentParser(parents=parents, add_help=False, description=description)
        return argparse.ArgumentParser(add_help=add_help, description=description)

    def get_argument_parser(self, use_shared_parser=False, add_help=False):
        """Returns Argument Parser to use for the stage.

        Args:
            use_shared_parser: whether to use shared parser as parent.
            add_help: whether to add help.
        """
        return self.get_base_argument_parser(use_shared_parser, add_help, "A base for stage")
