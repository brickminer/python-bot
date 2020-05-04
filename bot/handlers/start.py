from emoji import emojize
from ..settings import BLOCKED_SETS


def handle(update, context):
    evil = emojize(":imp:", use_aliases=True)
    blocked_list = ", ".join(BLOCKED_SETS)

    text = "Welcome to the Brickminer bot!"

    if BLOCKED_SETS:
        text = text + \
            f"\nI'm sorry but you will never be able to get info for the {blocked_list}, they are {evil}"

    update.message.reply_text(text)
