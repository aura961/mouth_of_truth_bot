from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    ContextTypes,
    MessageHandler,
    filters,
)

TOKEN = "YOUR_TOKEN"

CONTACT = "https://t.me/aura961"
CHANNEL = "https://t.me/adaura961"


async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # 시스템 입장 메시지 삭제
    try:
        await update.message.delete()
    except Exception as e:
        print("입장 시스템메시지 삭제 실패:", e)

    for user in update.message.new_chat_members:

        username = user.username
        user_id = user.id

        text = f"""
어서오세요 기다리고 있었어요.
저는 아우라의 문지기, 진실의 입이에요.
거짓말을 하면 당신의 손을 물어버릴거에요.

사용자명 : @{username if username else "없음"}
고유번호 : {user_id}
"""

        keyboard = [[
            InlineKeyboardButton("제휴문의", url=CONTACT),
            InlineKeyboardButton("제3구역", url=CHANNEL)
        ]]

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


async def left(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.delete()
    except Exception as e:
        print("퇴장 시스템메시지 삭제 실패:", e)


app = Application.builder().token(TOKEN).build()

# 입장
app.add_handler(
    MessageHandler(
        filters.StatusUpdate.NEW_CHAT_MEMBERS,
        welcome
    )
)

# 퇴장
app.add_handler(
    MessageHandler(
        filters.StatusUpdate.LEFT_CHAT_MEMBER,
        left
    )
)

app.run_polling()
