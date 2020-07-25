import logging
import random
from telegram.ext import (Updater, CommandHandler)


def name_generator():

    choice = random.random()
    thresholds = [0.2]
    first_word = ['Right', 'Cyber', 'Global', 'Net', 'Data', 'Machine',
                  'Robot', 'Internet', 'Be', 'Poly', 'lum', 'Tailor',
                  'Embedded', 'Micro', 'Light', 'Smart', 'Slick',
                  'Crypto', 'Sync', 'Deep', 'Hack', 'Digital', 'Agile',
                  'Social', 'Vector' ,'Wire','Ada','Tok', 'Geo', 'Vu', 'Azu',
                  'Atlas', 'Spo', ' Linear', 'Mash', 'Witchetty', 'Spotted',
                  'Rocky']

    second_word = ['.io', 'Inc', 'Vision', 'IO', 'Container', 'Data',
                   'robotics', 'Chain', 'Mining', 'Bound', 'Med', 'gold',
                   'industry', 'Dev', 'AI','AR','VR', 'Script', '360',
                   'Core', 'Silos', 'Unicorn', 'Log', 'Automation', 'Box',
                   'Mining','ops', 'Grid', 'Image', 'Maps', 'UI', 'Flow',
                   'Coin', 'gool', 'pala', 'dos', 'bird', 'dude', 'ton',
                   'oop', 'byss', 'Mail', 'Dumplings', 'Rabbit', 'fingers'
                   'Monkey']

    complete_word = ['CrazyUnicorn', 'MicroBlockchain', 'JirachiAI',
                     'HorseMining', 'SeahorseVision', 'FeebasData',
                     'DelibirdRobotics', 'GorebyssDev', 'LombreDocs',
                     'BidoofMedia', 'Fletchling.io', 'EmbeddedPidove']

    if choice > thresholds[0]:
        first_word_item = random.choice(first_word)
        second_word_item = random.choice(second_word)

        return first_word_item+second_word_item

    else:
        return random.choice(complete_word)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Hey!\n"
                                  "I'm the Startup Names Bot :)\n"
                                  "/gimme to start")

def gimme(update, context):
    response = name_generator() + "\n\nNow that you have a cool name for " \
                                  "your startup, lets talk business. \n" \
                                  "Split the profits 50 50?"
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text= response)

# Create the Updater and pass it your bot's token.
def main():

    # Create the Updater
    updater = Updater(token='993360636:AAFiqvCi9bquQoOUKZTPhXf9NT7Ei3kaqko',
                      use_context=True)
    updater.bot.setWebhook('https://startupnamesbot.herokuapp.com/' + '993360636:AAFiqvCi9bquQoOUKZTPhXf9NT7Ei3kaqko')
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Start the logger
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

    # Register commands to the Dispatcher
    start_handler = CommandHandler('start', start)
    joke_handler = CommandHandler('gimme', gimme)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(joke_handler)

    # Start the bot
    updater.start_polling()

if __name__ == '__main__':
    main()