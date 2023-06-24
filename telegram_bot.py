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
    /Cpp -> View C++ playlist
    /contact -> Contact Information
    """)

def content(update,context):
    update.message.reply_text("We have links to various course playlist")

def python(update,context):
    update.message.reply_text("""You can get good python video tutorials on the following sites:
    https://youtube.com/playlist?list=PLTjRvDozrdlxj5wgH4qkvwSOdHLOCx10f
    https://youtube.com/playlist?list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB
    https://youtube.com/playlist?list=PL9ooVrP1hQOE4KoZLUP4LgBwFH2IJCQs6
    """)

def javascript(update,context):
    update.message.reply_text("""You can get good javascript video tutorials on the following sites:
    https://youtube.com/playlist?list=PLsyeobzWxl7rrvgG7MLNIMSTzVCDZZcT4
    https://youtube.com/playlist?list=PLWKjhJtqVAbleDe3_ZA8h3AO2rXar-q2V
    """)

def cpp(update,context):
    update.message.reply_text("""You can get good javascript video tutorials on the following sites:
    https://youtube.com/playlist?list=PL_c9BZzLwBRJVJsIfe97ey45V4LP_HXiG
    """)

def contact(update,context):
    update.message.reply_text("Call: 0503986624 for assistance")