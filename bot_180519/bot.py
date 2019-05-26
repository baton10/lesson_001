from telegram.ext import Updater, CommandHandler

PROXY = {'proxy_url': 'socks5h://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)
def greet_user(bot, update):
    print('Вызван /start')

def main():
    mybot = Updater("640766054:AAElGpwr1a5IAHjhisA9bgrbtE5PDLX9tfI", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))

    mybot.start_polling()
    mybot.idle()

main()