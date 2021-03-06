"""A list of constants used for the workflow.
"""

from os.path import dirname, join

WORKFLOW_ROOT = dirname(dirname(__file__))
LOGGING_PATH = join(WORKFLOW_ROOT, "logs")
OUTPUT_PATH = join(WORKFLOW_ROOT, "output")
DATA_PATH = join(WORKFLOW_ROOT, "data")
TMP_PATH = join(WORKFLOW_ROOT, "tmp")
SQL_SCRIPTS_PATH = join(WORKFLOW_ROOT, "sql_scripts")
CONFIG_PATH = join(WORKFLOW_ROOT, "configs")
