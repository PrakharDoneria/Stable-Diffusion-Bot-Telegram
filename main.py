import os
import http.client
import json
import requests
import telebot
from io import BytesIO

telegram_api_token = os.getenv("TELEGRAM_API_TOKEN")

if not telegram_api_token:
    print("Telegram API token not found. Please set the TELEGRAM_API_TOKEN environment variable.")
    exit()

api_key = os.getenv("RAPIDAPI_KEY")

if not api_key:
    print("RapidAPI key not found. Please set the RAPIDAPI_KEY environment variable.")
    exit()

bot = telebot.TeleBot(telegram_api_token)

def send_message(chat_id, text):
    bot.send_message(chat_id, text)

def send_photo(chat_id, photo):
    bot.send_chat_action(chat_id, 'upload_photo')
    bot.send_photo(chat_id, photo)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, 'Send me a prompt and I will generate an image for you.')

@bot.message_handler(commands=['ai'])
def handle_ai(message):
    try:
        chat_id = message.chat.id
        text = message.text

        if len(text.split()) > 1:
            prompt = ' '.join(text.split()[1:])

            conn = http.client.HTTPSConnection("text-to-image-stable-ai.p.rapidapi.com")
            payload = "prompt=" + prompt
            headers = {
                'content-type': "application/x-www-form-urlencoded",
                'X-RapidAPI-Key': api_key,
                'X-RapidAPI-Host': "text-to-image-stable-ai.p.rapidapi.com"
            }
            conn.request("POST", "/prompt", payload, headers)
            res = conn.getresponse()
            data = res.read()

            response_json = json.loads(data.decode("utf-8"))
            image_url = response_json.get("image_url")

            if image_url:
                image_response = requests.get(image_url)
                image_data = BytesIO(image_response.content)

                send_photo(chat_id, image_data)
            else:
                send_message(chat_id, "Failed to generate image.")
        else:
            send_message(chat_id, "Please provide a prompt after /ai command.")
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        print(error_message)
        send_message(chat_id, error_message)

bot.polling()
