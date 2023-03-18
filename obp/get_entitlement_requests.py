import requests
from config import logger


def get_entitlement_request(obp_api_host, obp_auth_token, verify=True):
	authorization = f'DirectLogin token={obp_auth_token}'
	headers = {'Content-Type': 'application/json', 'Authorization': authorization}
	url = obp_api_host + "/obp/v5.1.0/entitlement-requests"
	try:
		entitlement_requests = requests.get(url, headers=headers, verify=verify).json()["entitlement_requests"]
	except Exception as e:
		logger.exception(f'Could not get entitlement requests: {e}')
		return {}
	return entitlement_requests




