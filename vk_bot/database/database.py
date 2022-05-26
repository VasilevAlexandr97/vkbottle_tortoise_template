from loguru import logger
from tortoise import Tortoise
from vk_bot.config import config

# for migrations
TORTOISE_ORM = {
    "connections": {"default": config.db_url},
    "apps": {
        "models": {
            "models": [
                "vk_bot.database.models.user",
                "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}


async def database_connection():
    logger.debug("database connection")
    await Tortoise.init(
        db_url=config.db_url,
        modules={
            "models": ["vk_bot.models.user"],
        }
    )


async def close_database_connection():
    logger.debug("close database connection")
    await Tortoise.close_connections()


async def on_startup() -> None:
    await database_connection()


async def on_shutdown() -> None:
    await close_database_connection()
