import random
import telebot
from telebot import types
from datetime import datetime
import jdatetime as jdate
from gtts import gTTS
import qrcode
import io

TOKEN = "7103454782:AAFf55hTAtS5jxyOnXXets45o7YvuEkMTeM"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

user_states = {}

keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
key_1 = types.KeyboardButton("Start ✅")
key_2 = types.KeyboardButton("Game 🎲")
key_3 = types.KeyboardButton("Age 🕵️‍♂️")
key_4 = types.KeyboardButton("Voice 🔊")
key_5 = types.KeyboardButton("Max 🥇")
key_6 = types.KeyboardButton("Argmax 🎖")
key_7 = types.KeyboardButton("QrCode 🖨")
key_8 = types.KeyboardButton("Help 🎈")
keyboard.add(key_1, key_2, key_3, key_4, key_5, key_6, key_7, key_8,key_9)

def start_game(chat_id):
    user_states[chat_id] = {"game": {"playing": True, "number": random.randint(1,100), "guesses": 0}}
    game_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    game_keyboard.add(types.KeyboardButton("New Game 🔄"))
    bot.send_message(chat_id, "Game started! Guess a number between 1 and 100.", reply_markup=game_keyboard)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Hello {message.from_user.first_name}, welcome to your friendly BOT😍😎, Please select your request from the menu", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Start ✅")
def start_message(message):
    bot.send_message(message.chat.id, f"Hi {message.from_user.first_name}😎, Please select your request from the menu", reply_markup=keyboard)
@bot.message_handler(commands=['game'])
@bot.message_handler(func=lambda message: message.text == "Game 🎲")
def handle_game_start(message):
    start_game(message.chat.id)

@bot.message_handler(func=lambda message: message.chat.id in user_states and "game" in user_states[message.chat.id] and user_states[message.chat.id]["game"]['playing'])
def handle_guess(message):
    chat_id = message.chat.id
    game_state = user_states[chat_id]["game"]
    guess = int(message.text) if message.text.isdigit() else None
    if guess is None:
        bot.send_message(chat_id, "Please enter a valid number.")
        return

    game_state['guesses'] += 1

    if guess == game_state['number']:
        bot.send_message(chat_id, f"Well done, it is true👏, The random number was: {game_state['number']}, and your all steps to find it is: {game_state['guesses']}")
        game_state['playing'] = False
        bot.send_message(chat_id, "Select an option from the menu or start a new game.", reply_markup=keyboard)
    elif guess < game_state['number']:
        bot.send_message(chat_id, "Go up 🔼")
    else:
        bot.send_message(chat_id, "Go down 🔽")
@bot.message_handler(commands=['age'])
@bot.message_handler(func=lambda message: message.text == "Age 🕵️‍♂️")
def ask_for_birthdate(message):
    bot.send_message(message.chat.id, "Please enter your birthdate in format as: (YYYY/MM/DD).")

@bot.message_handler(func=lambda message: "/" in message.text and len(message.text.split("/")) == 3)
def calculate_age(message):
    birthdate = message.text.split("/")
    birthdate = jdate.date(int(birthdate[0]), int(birthdate[1]), int(birthdate[2]))
    today = jdate.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    bot.send_message(message.chat.id, f"You are {age} years old.")

@bot.message_handler(commands=['voice'])
@bot.message_handler(func=lambda message: message.text == "Voice 🔊")
def ask_for_text(message):
    bot.send_message(message.chat.id, "Please send me a sentence in English to convert to voice, format as: (v: My text).")

@bot.message_handler(func=lambda message: "v:" in message.text)
def text_to_voice(message):
    text_to_convert = message.text.replace('v:', '').strip()
    tts = gTTS(text_to_convert, lang='en')
    voice = io.BytesIO()
    tts.write_to_fp(voice)
    voice.seek(0)
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['max',"argmax"])
@bot.message_handler(func=lambda message: message.text == "Max 🥇" or message.text == "Argmax 🎖")
def ask_for_array(message):
    user_states[message.chat.id] = {"command": message.text}
    bot.send_message(message.chat.id, "Please enter a list of numbers separated by commas, format as: (1,2,3,...).")

@bot.message_handler(func=lambda message: "," in message.text and message.chat.id in user_states)
def handle_array_commands(message):
    command = user_states[message.chat.id].get("command")
    numbers = [int(n) for n in message.text.split(',') if n.isdigit()]
    if command == "Max 🥇" or command == "/max":
        max_value = max(numbers)
        bot.send_message(message.chat.id, f"The maximum number is: {max_value}")
    elif command == "Argmax 🎖" or command == "/argmax":
        max_index = numbers.index(max(numbers))
        bot.send_message(message.chat.id, f"The index of the maximum number is: {max_index+1}")

    if message.chat.id in user_states:
        del user_states[message.chat.id]

@bot.message_handler(commands=['qrcode'])
@bot.message_handler(func=lambda message: message.text == "QrCode 🖨")
def ask_for_qr_data(message):
    bot.send_message(message.chat.id, "Please send me the data you want to encode in a QR code, format as: (qr: My request).")

@bot.message_handler(func=lambda message: "qr:" in message.text)
def generate_qr_code(message):
    data_for_qr = message.text.replace('qr:', '').strip()
    qr = qrcode.make(data_for_qr)
    img = io.BytesIO()
    qr.save(img, 'PNG')
    img.seek(0)
    bot.send_photo(message.chat.id, img)

@bot.message_handler(commands=['help'])
@bot.message_handler(func=lambda message: message.text == "Help 🎈")
def show_help(message):
    help_text = """
    /start - Greet with the user's name
/game - Start a number guessing game
/age - Calculate your age based on Shamsi (Hijri Shamsi) calendar
/voice - Convert a sentence in English to voice
/max - Find the maximum number in a list
/argmax - Find the index of the maximum number in a list
/qrcode - Generate a QR code from the input text
/photo - You can have a random Photo
/help - Show this help message
    """
    bot.send_message(message.chat.id, help_text)

bot.infinity_polling()