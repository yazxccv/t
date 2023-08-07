from pyrogram import Client, filters
from pyrogram.types import Message

from mody.Keyboards import start_key, cancel, subs
from mody.Redis import db
from mody.yad import Bfilter


@Client.on_message(Bfilter("حذف حساب ✘"))
async def delete_other(client: Client, message: Message):
    if db.scard(f'{client.me.id}:{message.from_user.id}:sessions') >= 1:
        msg = await message.ask('ارسل ايدي الحساب 🆔', filters.text, start_key, reply_markup=cancel)
        await message.reply('جاري حذف الحساب 😪', reply_markup=start_key)
        db.sadd(f'{client.me.id}:{message.from_user.id}:delete_userbot', msg.text)
    else:
        await message.reply('⌯ لا يوجد لديك حسابات لحذفها', reply_markup=subs)

