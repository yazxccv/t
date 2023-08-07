from pyrogram import Client

from mody.Keyboards import start_key, login_key,subs
from mody.Redis import db
from mody.yad import Bfilter


@Client.on_message(Bfilter('/start'))
async def start(client, message):
    if db.get(f'{client.me.id}:{message.from_user.id}:session'):
        await message.reply('- اهلا عزيزي 🔥\n\n- يمكنك  التجميع في بوتات التمويل من هنا ⚙️\n- قم بأضافة حساباتك واستمتع 🌝\n- البوت يعمل علي بوت العرب\n- قناة البوت : @MWMM20 ', reply_markup=start_key, )
    else:
        await message.reply('- مرحبا عزيزي يجب عليك تسجيل بحسابك  😊\n\n- سوف تقوم بستقبال النقاط عليه ♥️', reply_markup=login_key,)


@Client.on_message(Bfilter('حساباتي ↺'))
async def count_of_userbots(client, message):
    await message.reply(f"حساباتك ⇅ : {db.scard(f'{client.me.id}:{message.from_user.id}:sessions')}")
