

from pyrogram import Client
from pyrogram.types import Message

from mody.Keyboards import start_key, subs
from mody.Redis import db
from mody.get_session import getSession
from mody.yad import Bfilter



@Client.on_message(Bfilter("طريقة الاستخدام 📝"))


async def login_to_other(client: Client, message: Message):
 
        await message.reply('- مرحبا عزيزي المستخدم 😇 \n\n- طريقة استخدام البوت 🙃\n1 - ⚠️ سيطلب منك تسجيل دخول بحسابك ⚠️\n\n(لاتقلق فنحن لانستطيع الوصول لحسابك هو في امان لاكن  هذا اجراء لستقبال النقاط علي حسابك )\n\n2 - بعد تسجيل الدخول سوف ينبثق لك كيبورد 🌝\n\n(تستطيع اضافة حساب وحذف حساب الخ.. )\n\nبعد اضافة حساب سيقوم ببدء التجميع تلقائيا 😎\n***- لتجنب حظر حساباتك من بوت التجميع***\n   1- قم بوضع صوره\n  2- قم بوضع اسم \n  3- قم بوضع بايو \n   4- لا تبيع نقاط كسر', reply_markup=subs)





