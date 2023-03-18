import os
from RocketChatBot import RocketChatBot
from config import rocket_chat_host, rocket_chat_username, rocket_chat_password

botname = os.environ['BOTNAME']
botpassword = os.environ['BOTPASSWORD']
server_url = os.environ['BOT_URL']


def create_bot():
	bot = RocketChatBot(
		rocket_chat_username,
		rocket_chat_password,
		rocket_chat_host
	)
	return bot
