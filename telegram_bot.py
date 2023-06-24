from telegram.ext import Updater, CommandHandler

updater = Updater(token="6066892297:AAHXmHLf4lf4oVDPEtxfFrcgK1Z9JTZRhVA", use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to my Bot")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/help_me for help")

def help_me(update, context):
    help_message = """
    /help_me  -> Ask for help
    /content -> View content
    /python -> A python playlist
    /javascript -> View Javascript playlist
    /Cpp -> View C++ playlist
    /contact -> Contact Information
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_message)

def content(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="We have links to various course playlists")

def python(update, context):
    python_message = """You can get good python video tutorials on the following sites:
    https://youtube.com/playlist?list=PLTjRvDozrdlxj5wgH4qkvwSOdHLOCx10f
    https://youtube.com/playlist?list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB
    https://youtube.com/playlist?list=PL9ooVrP1hQOE4KoZLUP4LgBwFH2IJCQs6
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text=python_message)

def javascript(update, context):
    javascript_message = """You can get good javascript video tutorials on the following sites:
    https://youtube.com/playlist?list=PLsyeobzWxl7rrvgG7MLNIMSTzVCDZZcT4
    https://youtube.com/playlist?list=PLWKjhJtqVAbleDe3_ZA8h3AO2rXar-q2V
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text=javascript_message)

def cpp(update, context):
    cpp_message = """You can get good C++ video tutorials on the following site:
    https://youtube.com/playlist?list=PL_c9BZzLwBRJVJsIfe97ey45V4LP_HXiG
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text=cpp_message)

def contact(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Call: 0503986624 for assistance")

# Add a handler for each function
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help_me', help_me))
dispatcher.add_handler(CommandHandler('content', content))
dispatcher.add_handler(CommandHandler('python', python))
dispatcher.add_handler(CommandHandler('javascript', javascript))
dispatcher.add_handler(CommandHandler('Cpp', cpp))
dispatcher.add_handler(CommandHandler('contact', contact))

updater.start_polling()
updater.idle()
