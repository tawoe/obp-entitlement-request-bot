from config import obp_api_host, obp_username, obp_password, obp_consumer_key
from obp.create_direct_login_token import create_direct_login_token
from rocket_chat.create_bot import send_msg
from obp.get_entitlement_requests import get_entitlement_request
from datetime import  datetime, timedelta
from time import sleep
#login to obp

token = create_direct_login_token(
	username=obp_username,
	user_password=obp_password,
	consumer_key=obp_consumer_key,
	obp_api_host=obp_api_host
)
while True:
	entitlement_requests = get_entitlement_request(
		obp_api_host=obp_api_host,
		obp_auth_token=token
	)



	for e in entitlement_requests:
		# 'created': '2021-12-07T15:32:20Z'
		datetime_str = e['created']
		entitlement_creation_date = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%SZ')
		if entitlement_creation_date > datetime.now() - timedelta(minutes=5):
			send_msg(f'New entitlement request(s) for {obp_api_host}', 'monitoring-alerts')
			break
	sleep(300)

