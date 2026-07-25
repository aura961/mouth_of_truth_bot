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
🎉 새로운 사용자가 입장했습니다.

👤 닉네임 : {name}
🔗 사용자명 : @{username if username else "없음"}
🆔 고유번호 : {user_id}
"""

    keyboard = [
        [
            InlineKeyboardButton("제휴문의", url=CONTACT),
            InlineKeyboardButton("공지채널", url=CHANNEL)
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
