from pyrogram import Client
from pyrogram.types import Message

from mody.Keyboards import start_key
from mody.Keyboards import subs

from mody.Redis import db
from mody.get_session import getSession
from mody.yad import Bfilter


@Client.on_message(Bfilter("تسجيل حساب ✙"))
async def login_to_other(client: Client, message: Message):
    if db.scard(f'{client.me.id}:{message.from_user.id}:sessions') <= 30:
        user, get_me, session = await getSession(message, start_key)
        db.sadd(f'{client.me.id}:{message.from_user.id}:sessions', session)
        await message.reply('- تم تسجيل الحساب بنجاح ✅', reply_markup=start_key)
    else:
        await message.reply('غير مسموح لك بالاضافة اكثر من هيك 😭😂', reply_markup=subs)
