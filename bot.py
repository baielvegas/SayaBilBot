import telebot
import re
from telebot import types

dbfile = 'mydictionary.tsv'

# token and url for bot
TOKEN = "731839567:AAEEWfeYriNNDRNRmw9h3wOVKBa2IBJ-Fuw"
bot = telebot.TeleBot(TOKEN)

# start of real code

# adding reaction to commands as /start and /go

dico = []

def load_dictionary(fname):
    dico = []
    for line in open(fname, 'r').readlines():
        # discard lines that have no content or are comments
        line = line.strip()
        if line == '':
            continue
        if line[0] == '#':
            continue

        # process file to replace spaces with tabs
        line = re.sub('  +', ' ', line)
        line = line.replace(' ', '\t', 3)
        row = line.split('\t')

        # add the line to the internal dictionary
        dico.append(row)
    return dico

def lookup_word(word, dico):
    print('W:',word)
    print('D:', dico)
    for w in dico:
        print('X:',word,'«',w,'«' ,w[0],w[1], w[2])
        if w[0] == word or w[1] == word or w[2] == word:
            return w[3]

    return "Соз табылган жок"

@bot.message_handler(commands = ['start', 'go'])
def start_handler(message):

    dico = load_dictionary(dbfile)

    print(dico)

    # creating button for bot for easier using

    menu = types.ReplyKeyboardMarkup(resize_keyboard = True)
    menu.add("Compass")
    menu.add("Political Terminology")
    menu.add("Башкы идеологиялар")

    # bot sending messages

    # button for this message for further choice
    choose = bot.send_message(message.chat.id, "СаяБилге кош келиниздер. Бул бот адамдардын саясатты жакшыраак тушунууго жардам берет. Сизге эмне керек экенин танданыз: 1.Компас or 2.Саясий терминология or 3. Башкы идеологиялар", reply_markup=menu)

    bot.register_next_step_handler(choose, ideologies)
    bot.register_next_step_handler(choose, compass)

    bot.register_next_step_handler(choose, terms)





@bot.message_handler(content_types=['text'])
def compass(msg):
    if msg.text == "Compass":
        # editing button for this function
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu.add("Артка")
        cdefinition = bot.send_message(msg.chat.id, "Бул политикалык компас. Анда 2 ок бар, саясий жана экономикалык. ", reply_markup=menu)
        bot.register_next_step_handler(cdefinition, start_handler)

@bot.message_handler(content_types=['text'])
def terms(msg):
    if msg.text == "Political Terminology":
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu.add("Go back please")
        menu.add("Yes, of course")
        termins = bot.send_message(msg.chat.id, "Are you want to search for political terminology?", reply_markup=menu)
        bot.register_next_step_handler(termins, start_handler)



    else:
        dico = load_dictionary(dbfile)
        definition = lookup_word(msg.text, dico)
        bot.send_message(msg.chat.id, definition)

@bot.message_handler(content_types=['text'])
def ideologies(msg):
    if msg.text == "What is Ideology":
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu.add("🐍 Right")
        menu.add("🇦🇴Left")
        menu.add("Go back")
        ideaDefinition = bot.send_message(msg.chat.id, "Ideologies are mostly divided to 2 types, left and right", reply_markup=menu)

        bot.register_next_step_handler(ideaDefinition, rightS)
        bot.register_next_step_handler(ideaDefinition, leftS)

@bot.message_handler(content_types=['text'])
def rightS(msg):
    if msg.text == "🐍 Right":
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu.add("Go back")
        rightSide = bot.send_message(msg.chat.id, "Right is cool", reply_markup=menu)
        bot.register_next_step_handler(rightSide, start_handler)

@bot.message_handler(content_types=['text'])
def leftS(msg):
    if msg.text == "🇦🇴Left":
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu.add("Go back")
        leftSide = bot.send_message(msg.chat.id, "Left is cool", reply_markup=menu)
        bot.register_next_step_handler(leftSide, start_handler)




bot.polling()
