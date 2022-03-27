import telebot
import base64
import converter
import validator

# https://api.telegram.org/bot5147131042:AAFU6X7o0_aci-_nNlGr-RPgFxPYHMTwx3o/getUpdates
bot = telebot.TeleBot('5147131042:AAFU6X7o0_aci-_nNlGr-RPgFxPYHMTwx3o')

text = ""
time = ""
ava = ""

def image_to_base64(photo_id):
	photo_file = bot.get_file(photo_id)
	photo_bytes = bot.download_file(photo_file.file_path)
	return base64.b64encode(photo_bytes)

@bot.message_handler(commands=['start'])
def start_message(message):
	with open(r"template\assets\instruction.png", "rb") as file:
		bot.send_photo(message.chat.id, file)

@bot.message_handler(content_types=["photo"])
def get_message(message):
	global text, time, av
	if not validator.valid(message.caption):
		bot.send_message(message.chat.id, 'syntax error')
		return
	
	encoded = image_to_base64(message.photo[-1].file_id)
	message_arr = message.caption.strip().split()

	text, time = " ".join(message_arr[:-1]) ,message_arr[-1]
	photo = converter.get_screen( text, time, str(encoded)[2:-1] )
	bot.send_document(message.chat.id, photo)

bot.polling(none_stop=True)