import telegram.ext

token = "https://www.drawize.com/play?sscid=61k7_z9k2k&#"

update =  telegram.ext.update(token,use_contexto=True)

dispatcher = update.dispatcher

def start(update,context):
    update.message.reply_to("Welcome to my Bot")


def help(update,context):
    update.message.reply_to("""
    /start -> Welcome to channel
    /help  -> Ask for help
    /content -> View content
    /python -> A python playlist
    /javascript -> View Javascript playlist
    /C++ -> View C++ playlist
    /contact -> Contact Information
    """)

def