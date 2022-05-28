import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from loguru import logger

from vk_bot.tools.files import load_yaml_file

BASE_DIR = Path(__name__).resolve().parent
DATA_DIR = BASE_DIR.joinpath("vk_bot/data")
ENV_PATH = BASE_DIR.joinpath(".env")

load_dotenv(dotenv_path=ENV_PATH)


@dataclass
class Bot:
    token: str


@dataclass
class Database:
    type: str
    name: str
    host: Optional[str]
    port: Optional[int]
    user: Optional[str]
    password: Optional[str]


@dataclass
class Config:
    bot: Bot
    db: Database
    db_url: str
    bot_msgs: dict
    bot_btns: dict


def setup_config() -> Config:
    db = Database(
        type=os.getenv("DATABASE_TYPE"),
        name=os.getenv("DATABASE_NAME"),
        host=os.getenv("DATABASE_HOST"),
        port=int(os.getenv("DATABASE_PORT")),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD")
    )

    match db.type:
        case "postgres":
            db_url = (f"postgres://{db.user}:{db.password}@{db.host}:"
                      f"{db.port}/{db.name}")
        case "sqlite":
            db_url = f"sqlite://{BASE_DIR.joinpath(db.name)}"
        case _:
            logger.error("database type not initial")
            return sys.exit()

    return Config(
        bot=Bot(token=os.getenv("VK_API_TOKEN")),
        db=db,
        db_url=db_url,
        bot_msgs=load_yaml_file(DATA_DIR.joinpath("messages.yaml")),
        bot_btns=load_yaml_file(DATA_DIR.joinpath("buttons.yaml"))
    )


config = setup_config()