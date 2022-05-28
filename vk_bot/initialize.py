from vkbottle.bot import Bot

from vk_bot.database.database import on_shutdown, on_startup
from vk_bot.handlers import bps
from vk_bot.middlewares.registration import RegistrationMiddleware


def setup_middlewares(bot: Bot) -> None:
    bot.labeler.message_view.register_middleware(RegistrationMiddleware)


def setup_handlers(bot: Bot):
    # loading handlers
    for bp in bps:
        bp.load(bot)


def setup_bot(bot_token: str) -> Bot:
    # Bot initialization
    bot = Bot(bot_token)

    bot.loop_wrapper.on_startup.append(on_startup())
    bot.loop_wrapper.on_shutdown.append(on_shutdown())

    setup_middlewares(bot)
    setup_handlers(bot=bot)

    # Returnging initializated bot
    return bot
