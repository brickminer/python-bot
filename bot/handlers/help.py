from emoji import emojize
from bot.settings import Settings

settings = Settings()


def handle(update, context):
    evil = emojize(":imp:", use_aliases=True)
    blocked_list = ", ".join(settings.blocked_sets())

    text = "To search for a set, just type @brickminerbot + set number or set name. You should be presented to a list of results, just select the one you want to show."

    if settings.blocked_sets():
        text = text + \
            f"\nI'm sorry but you will never be able to get info for the {blocked_list}, they are {evil}"

    update.message.reply_text(text)
