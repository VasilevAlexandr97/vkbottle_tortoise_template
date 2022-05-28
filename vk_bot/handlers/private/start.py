from vkbottle.bot import Blueprint, Message

bp = Blueprint("Start Blueprint")
bp.on.vbml_ignore_case = True


@bp.on.private_message(text=["start", "начать", "привет"])
@bp.on.private_message(payload={"command": "start"})
async def start_handler(message: Message):
    print(message.text)