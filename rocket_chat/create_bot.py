from rocketchat_API.rocketchat import RocketChat
from config import rocket_chat_host, rocket_chat_username, rocket_chat_password


rocket = RocketChat(rocket_chat_username, rocket_chat_password, server_url=rocket_chat_host)
def send_msg(msg: str, channel:str):
	rocket.chat_post_message(msg, channel=channel)