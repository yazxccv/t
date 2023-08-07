from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start_key = ReplyKeyboardMarkup(
    [
        ["حذف حساب ✘","تسجيل حساب ✙"],
        ["حساباتي ↺","تعيين النقاط √"],
    ],
    resize_keyboard=True
)

login_key = ReplyKeyboardMarkup(
    [
        ["تسجيل الدخول ⚙️"],
        ["طريقة الاستخدام 📝"],
    ],
    resize_keyboard=True
)

cancel = ReplyKeyboardMarkup(
    [
        ["الغاء ✘"],
    ],
    resize_keyboard=True,
)

send_you_contact = ReplyKeyboardMarkup(
    [
        [KeyboardButton('مشاركة جهة اتصالك 👥', request_contact=True)],
    ],
    resize_keyboard=True,
)

subs = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("𝗚𝗢𝗟𝗗𝗘𝗡 𝗦𝗢𝗨𝗥𝗖𝗘", url=f"https://t.me/xooue"),
            ],
        ]
    )