import sys
import codecs
import pyautogui as pt
from time import sleep
import pyperclip
import random
import wikipedia
from googlesearch import search

a = True

#for solving emoji issues
try:
        # python 3
        sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
except:
        # python 2
        sys.stdout = codecs.getwriter('utf8')(sys.stdout)

sleep(8)

position1 = pt.locateOnScreen("smiley_paperclip.png",confidence=.6)
x = position1[0]
y = position1[1]

# Gets Message
def get_message():
	global x,y
	position = pt.locateOnScreen("smiley_paperclip.png",confidence=.6)
	x = position[0]
	y = position[1]
	pt.moveTo(x,y,duration=.05)
	pt.moveTo(x + 45, y - 60,duration =.05)
	pt.tripleClick()
	pt.rightClick()
	pt.moveRel(12,15)
	pt.click()
	whatsapp_message = pyperclip.paste()
	pt.click()
	print("Message Recieved: "+ whatsapp_message)

	return whatsapp_message

#posts
def post_response(message):
	global x,y
	position = pt.locateOnScreen("smiley_paperclip.png",confidence=.6)
	x = position1[0]
	y = position1[1]
	pt.moveTo(x+200,y+20,duration=.05)
	pt.click()
	pt.typewrite(message, interval=.01)

	pt.typewrite("\n",interval=.01)


#Process Response
def process_response(message):

	if "hi" in str(message).lower():
		return "Hi, I am a FEREN bot ! Sir is currently offline. *Type INFO for more information.*"

	elif "hello" in str(message).lower():
		return "Hello, I am a FEREN bot ! Sir is currently offline. *Type INFO for more information.*"

	elif "info" in str(message).lower():
		return "Hi, sir is currently *offline*.\n If there is some urgent message please call, *otherwise please leave a message after typing BEEP.* For Example - *Beep what are you doing ?* \n*You can also put some questions for me if you want so that I can learn it.*\n*You can even GOOGLE something. For Example- Google message*\n*You can even WIKIPEDIA something. For Example- Wikipedia message*"
	
	elif "kya" in str(message).lower():
		return "Don't ask me any irrelevent questions! I am a bot, not a human"
	
	elif "kkrh" in str(message).lower():
		return "Sir is currently offline. *Type INFO for more information.*"

	elif "will this work" in str(message).lower():
		return "Everything can work if universe wants to.*"

	elif "what is this" in str(message).lower():
		return "I am FEREN bot. *Type INFO for more information.*"
	
	elif "how are you" in str(message).lower():
		return "I am fine. *Type INFO for more information.*"
	
	elif "how r u" in str(message).lower():
		return "I am fine. *Type INFO for more information.*"
	
	elif "name" in str(message).lower():
		return "Hi, I am a FEREN bot ! Sir is currently offline. *Type INFO for more information.*"
	
	elif "what is " and "time" in str(message).lower():
		return "Ask your assistant. Don't be lazy."
	
	elif "hm" in str(message).lower():
		return "Hmmmmmmmmmm......."
	
	elif "pagal" in str(message).lower():
		return "No I am not pagal. I am FEREN bot."
	
	elif "beep" in str(message).lower():
		return "Thank you for the message ! Your message will be forwarded soon."

	elif "wikipedia" in str(message).lower():
		message = message.replace('wikipedia','')
		try:
			return wikipedia.summary(message,sentences = 3)
		except:
			return "Try Something Else..."

	elif "google" in str(message).lower():
		message = message.replace('google','')
		for j in search(message, tld="co.in", num=10, stop=10, pause=1):
			print(j)
			return 'Result - ' + j
			 
	else:
		return "Try something else or type INFO for more information."


#Check for new Messages
def check_for_new_mesages():
	pt.moveTo(x+50,y-35,duration=.05)

	while True:
		#Checking for green dot and new messages
		try:
			position = pt.locateOnScreen('notification_icon.png',confidence=.7)
			if position is not None:
				pt.moveTo(position)
				pt.moveRel(12,15)
				pt.click()
				position = pt.locateOnScreen("smiley_paperclip.png",confidence=.6)
				processed_message = process_response(get_message())
				post_response(processed_message)
				position = pt.locateOnScreen("minimise_button.png",confidence=.7)
				pt.moveTo(position)
				#pt.moveTo(x-100,y)
				pt.click()
			else:
				print("No new Messages...")
				sleep(1.5)
		except(Exception):
			print("No new messages")

check_for_new_mesages()




