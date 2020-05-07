from emoji import emojize
from bot.settings import Settings

settings = Settings()


def handle(update, context):
    evil = emojize(":imp:", use_aliases=True)
    blocked_list = ", ".join(settings.blocked_sets())

    text = "Welcome to the Brickminer bot!"

    if settings.blocked_sets():
        text = text + \
            f"\nI'm sorry but you will never be able to get info for the {blocked_list}, they are {evil}"

    update.message.reply_text(text)
