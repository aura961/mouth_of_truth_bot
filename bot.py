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


# 신규 입장 처리
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.message

    if not message:
        return

    # 텔레그램 입장 시스템 메시지 삭제
    try:
        await message.delete()
        print("입장 시스템 메시지 삭제 완료")
    except Exception as e:
        print("입장 메시지 삭제 실패:", e)


    # 입장한 사용자 정보
    for user in message.new_chat_members:

        username = user.username if user.username else "없음"

        text = f"""
어서오세요 기다리고 있었어요.

저는 아우라의 문지기,
진실의 입이에요.

거짓말을 하면
당신의 손을 물어버릴거에요.

사용자명 : @{username}
고유번호 : {user.id}
"""

        keyboard = [[
            InlineKeyboardButton(
                "제휴문의",
                url=CONTACT
            ),
            InlineKeyboardButton(
                "제3구역",
                url=CHANNEL
            )
        ]]

        await context.bot.send_message(
            chat_id=message.chat.id,
            text=text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


# 퇴장 / 강퇴 처리
async def left(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.message

    if not message:
        return

    # 퇴장 시스템 메시지 삭제
    try:
        await message.delete()
        print("퇴장/강퇴 메시지 삭제 완료")
    except Exception as e:
        print("퇴장 메시지 삭제 실패:", e)



app = Application.builder().token(TOKEN).build()


# 입장 (초대링크 포함)
app.add_handler(
    MessageHandler(
        filters.StatusUpdate.NEW_CHAT_MEMBERS,
        welcome
    )
)


# 나감 / 추방
app.add_handler(
    MessageHandler(
        filters.StatusUpdate.LEFT_CHAT_MEMBER,
        left
    )
)


print("봇 실행중...")
app.run_polling()
