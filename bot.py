from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, ContextTypes, MessageHandler, filters


TOKEN = "8791356089:AAFkcEBt1BvgDkbeOcQRLhzCkAnxMZZoV2c"

CONTACT = "https://t.me/aura961"
CHANNEL = "https://t.me/adaura961"


async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.new_chat_members[0]

    name = user.full_name
    username = user.username
    user_id = user.id

    text = f"""
어서오세요 기다리고 있었어요.
저는 아우라의 문지기, 진실의 입이에요.
거짓말을 하면 당신의 손을 물어버릴거에요.

 사용자명 : @{username if username else "없음"}
 고유번호 : {user_id}
"""

    keyboard = [
        [
            InlineKeyboardButton("제휴문의", url=CONTACT),
            InlineKeyboardButton("제3구역", url=CHANNEL)
        ]
    ]

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(
        filters.StatusUpdate.NEW_CHAT_MEMBERS,
        welcome
    )
)

app.run_polling()
