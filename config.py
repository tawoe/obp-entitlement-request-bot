from dotenv import load_dotenv
from os import getenv
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("obp_python")
logger.propagate = True

load_dotenv()
obp_api_host = getenv('OBP_HOSTNAME', 'http://localhost:8080')
obp_username = getenv('OBP_USERNAME')
obp_password = getenv('OBP_PASSWORD')
obp_consumer_key = getenv('OBP_CONSUMER_KEY')
rocket_chat_host = getenv('ROCKET_CHAT_HOST')
rocket_chat_username = getenv('ROCKET_CHAT_USERNAME')
rocket_chat_password = getenv('ROCKET_CHAT_PASSWORD')
