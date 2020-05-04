from emoji import emojize
from ..settings import BLOCKED_SETS


def handle(update, context):
    evil = emojize(":imp:", use_aliases=True)
    blocked_list = ", ".join(BLOCKED_SETS)

    text = "To search for a set, just type @brickminerbot + set number or set name. You should be presented to a list of results, just select the one you wan't to show."

    if BLOCKED_SETS:
        text = text + \
            f"\nI'm sorry but you will never be able to get info for the {blocked_list}, they are {evil}"

    update.message.reply_text(text)
