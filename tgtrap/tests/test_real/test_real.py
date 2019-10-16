import asyncio

import uvloop
from aiotg import Bot, Chat

from tgtrap.tests.test_real.test_config import (
    BOT_TOKEN,
    PROXY_URL,
)

from tgtrap.tests.test_real.tg_trap_example import TgTrapExample


bot = Bot(api_token=BOT_TOKEN, proxy=PROXY_URL)
trap = TgTrapExample(mongo_cs='mongodb://localhost:27017', mongo_db='tg_trap')


@bot.command("(.+)")
async def bitcoin(chat: Chat, match):
    await trap.process_message(chat.message)
    await chat.send_text('hello')


def main():
    bot.run(debug=True)


if __name__ == '__main__':
    uvloop.install()
    main()
