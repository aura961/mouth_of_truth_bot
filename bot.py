from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    ContextTypes,
    MessageHandler,
    filters,
)

import os


TOKEN = os.environ.get("TOKEN")


CONTACT = "https://t.me/aura961"
CHANNEL = "https://t.me/adaura961"


async def system_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.message

    if message is None:
        return


    # =================================
    # 신규 입장 처리
    # (초대 링크 포함)
    # =================================

    if message.new_chat_members:

        # 텔레그램 기본 입장 시스템 메시지 삭제
        try:
            await message.delete()
        except Exception as e:
            print("입장 메시지 삭제 실패:", e)


        # 환영 메시지 전송
        for user in message.new_chat_members:

            username = user.username or "없음"


            text = f"""
어서오세요 기다리고 있었어요.

저는 아우라의 문지기,
진실의 입이에요.

거짓말을 하면 당신의 손을 물어버릴거에요.


사용자명 : @{username}
고유번호 : {user.id}
"""


            keyboard = [
                [
                    InlineKeyboardButton(
                        "제휴문의",
                        url=CONTACT
                    ),
                    InlineKeyboardButton(
                        "제3구역",
                        url=CHANNEL
                    )
                ]
            ]


            await context.bot.send_message(
                chat_id=message.chat.id,
                text=text,
                reply_markup=InlineKeyboardMarkup(keyboard)
            )


        return



    # =================================
    # 퇴장 처리
    # (자진퇴장 / 관리자 추방 동일 처리)
    # =================================

    if message.left_chat_member:

        try:
            await message.delete()

        except Exception as e:
            print("퇴장 메시지 삭제 실패:", e)

        return



    # =================================
    # 기타 시스템 메시지 삭제
    # =================================

    system_messages = [

        message.pinned_message is not None,

        message.group_chat_created,

        message.supergroup_chat_created,

        message.new_chat_photo,

        message.video_chat_started,

        message.video_chat_ended,

    ]


    if any(system_messages):

        try:
            await message.delete()

        except Exception as e:
            print("시스템 메시지 삭제 실패:", e)



# =================================
# TOKEN 확인
# =================================

if not TOKEN:
    raise Exception("TOKEN 환경변수가 없습니다.")



# =================================
# 봇 실행
# =================================

app = Application.builder().token(TOKEN).build()


app.add_handler(
    MessageHandler(
        filters.ALL,
        system_handler
    )
)


print("Bot Started")


app.run_polling(
    drop_pending_updates=True
)
