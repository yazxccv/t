from pyrogram import idle

import DRGLIB
from mody.Keyboards import start_key
from mody.Redis import db
from mody.get_info import sudo_info, get_bot
from mody.yad import Bot, sudo_client


async def main():
    await Bot.start()
    if db.get(f'{Bot.me.id}:restart'):
        await Bot.send_message(sudo_info.username, 'شكرا لنتظارك تستطيع استخدام البوت 😎', reply_markup=start_key)
        db.delete(f'{Bot.me.id}:restart')
    if db.get(f'{get_bot.id}:{sudo_info.id}:session'):
        try:
            await sudo_client.start()
            sudo_client.login = True
        except Exception as e:
            print(e)
            db.delete(f'{get_bot.id}:{sudo_info.id}:session')
    print("تم تشغيل البوت بنجاح")
    await idle()
    await Bot.stop()
    print("تم ايقاف البوت بنجاح")


if __name__ == '__main__':
    DRGLIB.client.loop.run_until_complete(main())
