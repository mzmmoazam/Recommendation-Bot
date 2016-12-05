import telebot
import requests

bot=telebot.TeleBot("Telegam API ")
print("started")   # gets printed in console

#I have named this bot of mine Chappie

# I later upgrade this bot and used NLP in it.

@bot.message_handler(commands=['start'])
def yoyo(message):
    x="Hi..!This is Chappie.\nWhat would you like to see today.\n\nThese are the aspects."
    x+="\nmovie\nmusic\nbooks\nauthors\nshows\ngame\n\nChoose any option and enter your choice in the format\n eg. movie : movie_name"

    bot.reply_to(message,x)
    #bot.reply_to(message,l)



@bot.message_handler(func=(lambda message:True and "movie :"in message.text.lower()))
def formovie(message):

    query = message.text.replace("movie : ","")
    query = query.replace(' ', '+')
    print(query)
    tastekidAPI=" taste kid API"
    url1 = 'https://www.tastekid.com/api/similar?q=' + query + '&tastekidAPI&format=json&type=movie'
    r = requests.get(url1)
    x=eval(r.text)
    s='\n'.join([i["Name"] for i in x["Similar"]["Results"]])
    bot.reply_to(message,s )

@bot.message_handler(func=lambda message:True and "music :"in message.text.lower())
def fgokn(message):
    query = message.text.replace("music : ", "")
    query = query.replace(' ', '+')
    print(query)
    url1 = 'https://www.tastekid.com/api/similar?q=' + query + '&tastekidAPI&format=json&type=music'
    r = requests.get(url1)
    x = eval(r.text)
    s = '\n'.join([i["Name"] for i in x["Similar"]["Results"]])
    bot.reply_to(message, s)

@bot.message_handler(func=lambda message:True and "game :"in message.text.lower())
def fgokn(message):
    query = message.text.replace("game : ", "")
    query = query.replace(' ', '+')
    print(query)
    url1 = 'https://www.tastekid.com/api/similar?q=' + query + '&tastekidAPI&format=json&type=game'
    r = requests.get(url1)
    x = eval(r.text)
    s = '\n'.join([i["Name"] for i in x["Similar"]["Results"]])
    bot.reply_to(message, s)

@bot.message_handler(func=lambda message:True and "book :"in message.text.lower())
def fgokn(message):
    query = message.text.replace("book : ", "")
    query = query.replace(' ', '+')
    print(query)
    url1 = 'https://www.tastekid.com/api/similar?q=' + query + '&tastekidAPI&format=json&type=book'
    r = requests.get(url1)
    print(r.text)
    x = eval(r.text)
    s = '\n'.join([i["Name"] for i in x["Similar"]["Results"]])
    bot.reply_to(message, s)


@bot.message_handler(func=lambda message:True and "author :"in message.text.lower())
def fgokn(message):
    query = message.text.replace("author : ", "")
    query = query.replace(' ', '+')
    print(query)
    url1 = 'https://www.tastekid.com/api/similar?q=' + query + '&tastekidAPI&format=json&type=author'
    r = requests.get(url1)
    print(r.text)
    x = eval(r.text)
    s = '\n'.join([i["Name"] for i in x["Similar"]["Results"]])
    bot.reply_to(message, s)

@bot.message_handler(func=lambda message:True and "shows :"in message.text.lower())
def fgokn(message):
    query = message.text.replace("shows : ", "")
    query = query.replace(' ', '+')
    print(query)
    url1 = 'https://www.tastekid.com/api/similar?q=' + query + '&tastekidAPI&format=json&type=shows'
    r = requests.get(url1)
    print(r.text)
    x = eval(r.text)
    s = '\n'.join([i["Name"] for i in x["Similar"]["Results"]])
    bot.reply_to(message, s)



@bot.message_handler(func=lambda message:True)
def blab(message):
    bot.reply_to(message,"Couldn't get what u want .please try again\n\n /start")


bot.polling()









