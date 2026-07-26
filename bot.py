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


# 모든 시스템 메시지 삭제 + 입장 처리
async def system_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.message

    if not message:
        return


    # ===== 입장 감지 =====
    if message.new_chat_members:

        # 시스템 입장 메시지 삭제
        try:
            await message.delete()
        except Exception as e:
            print("입장 삭제 실패:", e)


        for user in message.new_chat_members:

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
                chat_id=update.effective_chat.id,
                text=text,
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

        return



    # ===== 모든 퇴장 / 추방 시스템 메시지 삭제 =====
    if message.left_chat_member:

        try:
            await message.delete()
        except Exception as e:
            print("퇴장/추방 삭제 실패:", e)

        return



    # ===== 기타 텔레그램 서비스 메시지 삭제 =====
    if message.is_automatic_forward:
        return


    # 필요하면 모든 서비스 메시지 제거
    if message.service:
        try:
            await message.delete()
        except Exception as e:
            print("기타 시스템 메시지 삭제 실패:", e)



app = Application.builder().token(TOKEN).build()


# 모든 시스템 메시지 감시
app.add_handler(
    MessageHandler(
        filters.ALL,
        system_message
    )
)


app.run_polling()
