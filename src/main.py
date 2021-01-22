"""Creating and executing a pipeline.
"""
from configuration import run_configuration
from stage_factory import create_pipeline_from_config

pipeline = create_pipeline_from_config("pipeline_config.yaml")
argument_parser = pipeline.get_argument_parser()

args = argument_parser.parse_args()
run_configuration(args)
pipeline.execute(args)
