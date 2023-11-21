from telegram.ext import Filters, CommandHandler, MessageHandler, Updater
import requests

Token = "6864397763:AAE9XXy8XIFtlAvem1zs5jghQf4C0XgA5wI"

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
    API_Key = '99271d6bcbec1e205f414bcd204865ff'

def get_city():
    API_Key = '99271d6bcbec1e205f414bcd204865ff'
