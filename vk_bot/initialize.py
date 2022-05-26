from vkbottle.bot import Bot

from vk_bot.config import config
from vk_bot.database.database import on_shutdown, on_startup
from vk_bot.handlers import bps


def setup_handlers(bot: Bot):
    # loading handlers
    for bp in bps:
        bp.load(bot)


def setup_bot() -> Bot:
    # Bot initialization
    bot = Bot(config.bot.token)

    bot.loop_wrapper.on_startup.append(on_startup())
    bot.loop_wrapper.on_shutdown.append(on_shutdown())

    setup_handlers(bot=bot)

    # Returnging initializated bot
    return bot
