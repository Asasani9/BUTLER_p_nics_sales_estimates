# get.py
import os
import logging
import redivis

logger = logging.getLogger(__name__)

REDIVIS_API_TOKEN = os.environ["REDIVIS_API_TOKEN"]

if not REDIVIS_API_TOKEN:
    raise RuntimeError("Missing REDIVIS_API_TOKEN environment variable.")

SLACK_BOT_TOKEN = redivis.organization("TheTrace").secret("gva_slackbot_token")
SLACK_CHANNEL_ID = "C096NBWPZA7"

def get():
    
    logger.info('Getting notebooks from Redivis...')
    username = "asasani"  # Replace with your Redivis username
    workflow_name = "gun sales:v49p"  # Replace with your workflow name
    notebook_name = "nics_sales_estimates:x2ma"  # Replace with your notebook name
    
    notebook = redivis.notebook(f"{username}.{workflow_name}.{notebook_name}")
    
    logger.info(f'Running {notebook_name} notebook...')
    try:
        notebook.run(wait_for_finish=True)  # Wait for the notebook to finish running
    except Exception as e:
        send_slack(f'Gun Sales Tracker notebook failed: {e}', True)
    logger.info(f'Running {notebook_name} notebook finished.')
    # Wordpress triggers here or in Redivis notebook itself.
    send_slack("TEST - Gun Sales Tracker data pulled successfully: https://nics-data.s3.amazonaws.com/nics-latest.csv")

def send_slack(text, error=False):
    color = '#FFFFFF'
    if error:
        color = '#FF0000'
    try:
        response = requests.post(
            "https://slack.com/api/chat.postMessage",
            headers={"Authorization": f"Bearer {SLACK_BOT_TOKEN.get_value()}"},
            json={
                "channel": SLACK_CHANNEL_ID,
                "text": "Gun Sales Tracker",
                "attachments": [
                    {
                        "color": color
                        "text": text
                    }
                ]
            }
        )
        response.raise_for_status()
        data = response.json()
        if not data.get("ok"):
            raise ValueError(f"Slack API error: {data}")
    except Exception as e:
        log(f"[Slack] Failed to send message: {e}")
