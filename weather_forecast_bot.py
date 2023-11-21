from telegram.ext import Filters, CommandHandler, MessageHandler, Updater
import requests

Token = ""

updater = Updater(Token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("""
                              Welcome to Weather Forecast bot!
I can provide weather forecasts for any location in the world☀️☁️🌧
                              """)

def help(update, context):
    update.message.reply_text("""
                              /start -> Welcome to the bot
/help -> This message
/get_city -> You should enter the city name after this command first and use ```get_weather``` command after it
/get_weather -> Enter this command to get the weather forecast!
                              """)

def get_weather(update, context):
    API_Key = ''
    info = get_lat_lon()
    latitude = info[0]
    longitude = info[1]
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_Key}&units=metric'
    response = requests.get(url)
    update.message.reply_text(response.json())

def get_city(update, context):
    API_Key = ''
    global city
    city = update.message.text

def get_lat_lon():
    API_Key = ''
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_Key}"
    response = requests.get(url)
    lat = response.json()[0]['lat']
    lon = response.json()[0]['lon']
    return lat, lon


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('get_weather', get_weather))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, get_city))

updater.start_polling()
updater.idle()