import requests
from config import logger


def create_direct_login_token(username, user_password, consumer_key, obp_api_host, verify=True):
	authorization = f"DirectLogin username={username},password={user_password},consumer_key={consumer_key}"
	headers = {'Content-Type': 'application/json', 'Authorization': authorization}

	payload = None
	url = obp_api_host + "/my/logins/direct"
	try:
		token = requests.post(url, headers=headers, json=payload, verify=verify).json()["token"]
	except Exception as e:
		logger.exception(f'Could not authenticate with OBP: {e}')
		token = ""
	return token




