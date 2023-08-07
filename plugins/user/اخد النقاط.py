from asyncio import create_task, sleep

from mody.Redis import db
from mody.get_info import sudo_info
from mody.yad import Bot, sudo_client
from info import user_bot


async def collect_points():
    while not await sleep(10):
        for link in db.smembers(f'{Bot.me.id}:{sudo_info.id}:links'):
            db.srem(f'{Bot.me.id}:{sudo_info.id}:links', link)
            await sudo_client.send_message(user_bot, f'/start {link}')
            await sleep(5)


create_task(collect_points())
