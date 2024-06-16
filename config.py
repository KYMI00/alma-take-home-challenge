import os
import logging
from dotenv import load_dotenv

load_dotenv()

class Config:
    openai_api_key = os.getenv('OPENAI_API_KEY')
    openai_api_base = os.getenv('OPENAI_API_BASE')
    openai_api_version = "2024-02-01"
    openai_deployment_name = os.getenv('OPENAI_DEPLOYMENT_NAME')
    logger = logging.getLogger(__name__)

    # blob storage configuration
    account_url =os.getenv('account_url')
