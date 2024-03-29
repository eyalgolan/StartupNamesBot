import logging
import random
import telegram
from telegram.ext import (Updater, CommandHandler)
import os

PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '<telegram token>'

emoji_money = "\U0001F911"
emoji_sad = "\U0001F628"
emoji_cry = "\U0001F62D"
emoji_very_sad = "\U0001F62B"


def startup_name_generator():

    # Generates a random startup name

    choice = random.random()
    thresholds = [0.1, 0.4]

    first_word = ['Cloud','Tera', 'Mega', 'Zeta', 'Peta', 'Right', 'Cyber',
                  'Global','Net', 'Data', 'Machine', 'Killer', 'Intense',
                  'Continues','Robot', 'Internet', 'Be', 'Poly', 'Lum',
                  'Tailor', 'Embedded', 'Micro', 'Light', 'Smart', 'Slick',
                  'Crypto', 'Sync', 'Deep', 'Hack', 'Digital', 'Agile',
                  'Social', 'Vector' ,'Wire', 'Geo', 'Vu', 'Azu',
                  'Atlas', 'Spo', ' Linear', 'Mash', 'Witchetty', 'Spotted',
                  'Rocky', 'Intelligent', 'Silent', 'Live', 'Bio', 'Wireless',
                  'Intel', 'Face', 'Sky', 'Water', 'Earth', 'Air', 'Momo',
                  'Graph', 'Twist', 'Applied', 'Rapid', 'KickAss', 'RedNeck',
                  'Life', 'Inner', 'Outer', 'Void', 'null', 'Hero', 'Research',
                  'Threat']

    second_word = ['API', 'Endpoint', 'Framework', 'Reliability', 'Analytics',
                   '.io', 'Inc', 'Vision', 'IO', 'Container', 'Data',
                   'Robotics', 'Chain', 'Mining', 'Bound', 'Med', 'Gold',
                   'Industry', 'Dev', 'AI','AR','VR', 'Script', '360',
                   'Core', 'Silos', 'Unicorn', 'Log', 'Automation', 'Box',
                   'Mining','Ops', 'Grid', 'Image', 'Maps', 'UI', 'Flow',
                   'Coin', 'Goal', 'Pala', 'Dos', 'bird', 'Dude', 'Ton',
                   'oop', 'byss', 'Mail', 'Dumplings', 'Rabbit', 'fingers',
                   'Monkey', 'Hub', 'VPN', 'Vpn', 'Burn', 'Ocean', 'cache',
                   'App', 'Communications','CI','CD','Deploy','Deployment',
                   'X', 'Go','Lang', 'Matters', 'Mama', 'Papa', 'Fox', 'Tube',
                   'Chat', 'Waves', 'Zone', 'Shadow', 'Bots', 'Avatar', 'Goat',
                   'Koala', 'Motors','IoT', 'Shark', 'Lock', 'Job', 'Task',
                   'Motion', 'Ninja', 'Fort', 'Brain', 'Online', 'Chewbacca',
                   'Jedi', 'Star']

    complete_word = ['CrazyUnicorn', 'MicroBlockchain', 'TeraAI',
                     'YOLOMining', 'SeahorseVision', 'DataGuy',
                     'CryptoRobotics', 'GorebyssDev', 'FireShipper',
                     'UnicornAI', 'yourMamasContainer.io', 'EmbeddedNinja',
                     'SlimGrid']

    # Choose words according to random generated number and thresholds
    if choice > thresholds[0]:
        first_word_item = random.choice(first_word)
        first_word_item = first_word_item.title()
        second_word_item = random.choice(second_word).title()

        if choice > thresholds[1] and len(second_word_item) >= 3:
            # lowercase the first letter of the second word
            second_word_item = second_word_item.lower()
        return first_word_item+second_word_item

    else:
        return random.choice(complete_word)

def respond_to_start_message(update, context):

    # Responds to "/start"

    keyboard = [['/gimme']]
    reply = telegram.ReplyKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Hey!\n"
                                  "I'm the Startup Names Bot :)\n"
                                  "/gimme to start",
                             reply_markup=reply)

def respond_to_gimme_message(update, context):
    # Responds to "/gimme"

    keyboard = [['/gimme'],
                ['/yes'],['/no']]
    reply = telegram.ReplyKeyboardMarkup(keyboard)
    response = "\n\nNow that you have a cool name for " \
                                  "your startup, let's talk business. \n" \
                                  "Split the profits 50 50? \n\n" \
                                  "Write /gimme to try again"
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text= startup_name_generator())
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text= response,
                             reply_markup=reply)

def error_handler(update, context):
    # Log Errors caused by Updates
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def respond_to_yes_message(update, context):
    # Responds to "/yes" response

    keyboard = [['/gimme']]
    reply = telegram.ReplyKeyboardMarkup(keyboard)
    response = emoji_money + emoji_money + emoji_money
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=response,
                             reply_markup=reply)
def respond_to_no_message(update, context):
    # Responds to "/no" response

    keyboard = [['/gimme']]
    reply = telegram.ReplyKeyboardMarkup(keyboard)
    response = emoji_sad + emoji_cry + emoji_very_sad
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=response,
                             reply_markup=reply)

def main():

    # Create the Updater
    updater = Updater(token=TOKEN,
                      use_context=True)
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register commands to the Dispatcher
    start_handler = CommandHandler('start', respond_to_start_message)
    gimme_handler = CommandHandler('gimme', respond_to_gimme_message)
    yes_handler = CommandHandler('yes', respond_to_yes_message)
    no_handler = CommandHandler('no', respond_to_no_message)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(gimme_handler)
    dispatcher.add_handler(yes_handler)
    dispatcher.add_handler(no_handler)

    # log all errors
    dispatcher.add_error_handler(error_handler)

    # # Start the bot on Heroku
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://startupnamesbot.herokuapp.com/' + TOKEN)


    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
