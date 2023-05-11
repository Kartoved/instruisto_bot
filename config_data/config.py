from dataclasses import dataclass
from environs import Env
from aiogram import Bot
import hashlib
import os

@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None):
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN'))), env('SALT')

config, SALT = load_config()

bot: Bot = Bot(token=config.tg_bot.token,
               parse_mode='HTML')
