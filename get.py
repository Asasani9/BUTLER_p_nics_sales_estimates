# get.py
import os
import logging
import redivis

logger = logging.getLogger(__name__)

REDIVIS_API_TOKEN = os.environ["REDIVIS_API_TOKEN"]

if not REDIVIS_API_TOKEN:
    raise RuntimeError("Missing REDIVIS_API_TOKEN environment variable.")

def get():
    
    logger.info('Getting notebooks from Redivis...')
    username = "asasani"  # Replace with your Redivis username
    workflow_name = "gun sales:v49p"  # Replace with your workflow name
    notebook_name = "nics_sales_estimates:x2ma"  # Replace with your notebook name
    
    notebook = redivis.notebook(f"{username}.{workflow_name}.{notebook_name}")
    
    logger.info(f'Running {notebook_name} notebook...')
    notebook.run(wait_for_finish=True)  # Wait for the notebook to finish running
    logger.info(f'Running {notebook_name} notebook finished.')
    # Wordpress triggers here or in Redivis notebook itself.
