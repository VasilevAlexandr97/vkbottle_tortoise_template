from vk_bot.config import setup_config
from vk_bot.initialize import setup_bot

bot = setup_bot()

config = setup_config()

bot_messages = config.bot_msgs
bot_buttons = config.bot_btns