# A template for creating python based pipeline / workflows

This is a template I created for python-based pipelines and workflows.

## Instructions

### Creating new stage

To create a new stage in your pipeline, you have to create a new class that inherits from BaseStage and define the run function. (See stage_download for reference).

### Command line arguments

This template uses argparse library for command line argument parsing. See [argparse](https://docs.python.org/3/library/argparse.html#nargs) for documentation.

### Executing pipeline / workflow

The pipeline can be executed in 2 ways:
 - Execute each stage manually
 - Execute with workflow, which executes all stages

### Logging

This template uses logging library. The workflow generates log files that can be found in logs folder. Use logger.info / debug / error / warning instead of print for proper logging when creating new stages. 
