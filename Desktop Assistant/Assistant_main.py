import time
import random
from plyer import notification
import winsound
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
from selenium import webdriver
from urllib.parse import quote
import os
from pywinauto import application
from pykeyboard import PyKeyboard
import pyjokes
import requests
import pyautogui


webbrowser.register('brave',None,webbrowser.BackgroundBrowser("--Location of Brave Browser"))
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("--Location Of Chrome Browser"))

k = PyKeyboard()
 
engine = pyttsx3.init('sapi5')
engine.setProperty("rate", 178)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=4 and hour<12:
		speak('Good Morning')
	elif hour>=12 and hour<18:
		speak('Good Afternoon')
	else:
		speak('Good Evening')

	speak('How may I help you')

def takeCommand():
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print('Listening...')
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print('Recognising...')
		query = r.recognize_google(audio, language='en-in')
		print(f"User said: {query}\n") 

	except Exception as e:
		#print(e)
		print('Say that again please...')
		return "None"
	return query

if __name__ == '__main__':
	wishMe()
	x = True
	while x:
		query = takeCommand().lower()

		if 'wikipedia' in query:
			speak('Searching Wikipedia')
			try:
				query = query.replace('wikipedia','')
				results = wikipedia.summary(query, sentences = 2)
				speak("According to Wikipedia")
				print(results)
				speak(results)
			except:
				speak('Try something else')

		elif 'open google' in query:
			webbrowser.get('brave').open('google.com')

		elif 'open youtube' in query:
			webbrowser.get('brave').open('youtube.com')

		elif 'on youtube' in query:
			query = query.replace('on youtube','')
			base_url = "https://www.youtube.com/results?search_query="
			final_url = base_url + quote(query)
			webbrowser.get('brave').open(final_url)
		
		elif 'play' in query:
			song = query.replace('play','')
			speak('Playing' + song)
			print('Playing' + song)
			print()
			pywhatkit.playonyt(song)

		elif 'google' in query:
			query = query.replace('google','')
			base_url = "http://www.google.com/search?q="
			final_url = base_url + quote(query)
			webbrowser.get('brave').open(final_url)

		elif 'search' in query:
			query = query.replace('search','')
			base_url = "http://www.google.com/search?q="
			final_url = base_url + quote(query)
			webbrowser.get('brave').open(final_url)

		elif 'open whatsapp' in query:
			webbrowser.get('brave').open('https://web.whatsapp.com/')

		elif 'bye bye' in query:
			speak('bye see you soon')
			x = False

		elif 'bye-bye' in query:
			speak('bye see you soon')
			x = False

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f'The time is {strTime}')

		elif 'the date' in query:
			strDate = datetime.datetime.now().strftime("%d/%m/%Y")
			speak(f'Today is {strDate}')

		elif 'the day' in query:
			strDay = datetime.datetime.now().strftime("%A")
			speak(f'Today is {strDay}')
		
		elif 'open visual studio' in query:
			codePath = '--Location of Visual Studio'
			os.startfile(codePath)

		elif 'close visual studio' in query:
			os.system("TASKKILL /F /IM code.exe")

		elif 'open task manager' in query:
			os.startfile('C:\\WINDOWS\\system32\\Taskmgr.exe')

		elif 'close task manager' in query:
			os.system("TASKKILL /F /IM Taskmgr.exe")

		elif 'open chrome' in query:
			chromePath = 'Location of Chrome Browser'
			os.startfile(chromePath)

		elif 'close chrome' in query:
			os.system("TASKKILL /F /IM chrome.exe")

		elif 'open brave' in query:
			bravePath = 'Location of Brave Browser'
			os.startfile(bravePath)

		elif 'close brave' in query:
			os.system("TASKKILL /F /IM brave.exe")

		elif 'open firefox' in query:
			firefoxPath = 'Location of Firefox Browser'
			os.startfile(firefoxPath)

		elif 'close chrome' in query:
			os.system("TASKKILL /F /IM firefox.exe")

		elif 'open calculator' in query:
			calcPath = 'C:\\Windows\\System32\\calc.exe'
			os.startfile(calcPath)

		elif 'close calculator' in query:
			os.system("TASKKILL /F /IM Calculator.exe")

		elif 'what is the weather in' in query:
			city = query.replace('what is the weather in','')
			api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=--Your API ID of Open Weather Map"
			json_data = requests.get(api).json()
			condition = json_data['weather'][0]['main']
			temp = int(json_data['main']['temp'] - 273.15)
			min_temp = int(json_data['main']['temp_min'] - 273.15)
			max_temp = int(json_data['main']['temp_max'] - 273.15)
			pressure = json_data['main']['pressure']
			humidity = json_data['main']['humidity']
			wind = json_data['wind']['speed']
			sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise'] - 19800))	
			sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset'] - 19800))
			print(f'Currently it\'s {temp}°C with {condition} in {city} with high of {max_temp}°C and low of {min_temp}°C.')
			speak(f'currently its {temp} degrees with {condition} in {city} with high of {max_temp} and low of {min_temp}')

		elif 'tell me about the weather in' in query:
			city = query.replace('tell me about the weather in','')
			api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=--Your API ID of Open Weather Map"
			json_data = requests.get(api).json()
			condition = json_data['weather'][0]['main']
			temp = int(json_data['main']['temp'] - 273.15)
			min_temp = int(json_data['main']['temp_min'] - 273.15)
			max_temp = int(json_data['main']['temp_max'] - 273.15)
			pressure = json_data['main']['pressure']
			humidity = json_data['main']['humidity']
			wind = json_data['wind']['speed']
			sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise'] - 19800))	
			sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset'] - 19800))
			print(f'Currently it\'s {temp}°C with {condition} in {city} with high of {max_temp}°C and low of {min_temp}°C.')
			speak(f'currently its {temp} degrees with {condition} in {city} with high of {max_temp} and low of {min_temp}')

		elif 'tell me about the weather of' in query:
			city = query.replace('tell me about the weather of','')
			api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=--Your API ID of Open Weather Map"
			json_data = requests.get(api).json()
			condition = json_data['weather'][0]['main']
			temp = int(json_data['main']['temp'] - 273.15)
			min_temp = int(json_data['main']['temp_min'] - 273.15)
			max_temp = int(json_data['main']['temp_max'] - 273.15)
			pressure = json_data['main']['pressure']
			humidity = json_data['main']['humidity']
			wind = json_data['wind']['speed']
			sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise'] - 19800))	
			sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset'] - 19800))
			print(f'Currently it\'s {temp}°C with {condition} in {city} with high of {max_temp}°C and low of {min_temp}°C.')
			speak(f'currently its {temp} degrees with {condition} in {city} with high of {max_temp} and low of {min_temp}')

		elif 'tell me the weather in' in query:
			city = query.replace('tell me the weather in ','')
			api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=--Your API ID of Open Weather Map"
			json_data = requests.get(api).json()
			condition = json_data['weather'][0]['main']
			temp = int(json_data['main']['temp'] - 273.15)
			min_temp = int(json_data['main']['temp_min'] - 273.15)
			max_temp = int(json_data['main']['temp_max'] - 273.15)
			pressure = json_data['main']['pressure']
			humidity = json_data['main']['humidity']
			wind = json_data['wind']['speed']
			sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise'] - 19800))	
			sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset'] - 19800))
			print(f'Currently it\'s {temp}°C with {condition} in {city} with high of {max_temp}°C and low of {min_temp}°C.')
			speak(f'currently its {temp} degrees with {condition} in {city} with high of {max_temp} and low of {min_temp}')

		elif 'tell me the weather of' in query:
			city = query.replace('tell me the weather of','')
			api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=--Your API ID of Open Weather Map"
			json_data = requests.get(api).json()
			condition = json_data['weather'][0]['main']
			temp = int(json_data['main']['temp'] - 273.15)
			min_temp = int(json_data['main']['temp_min'] - 273.15)
			max_temp = int(json_data['main']['temp_max'] - 273.15)
			pressure = json_data['main']['pressure']
			humidity = json_data['main']['humidity']
			wind = json_data['wind']['speed']
			sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise'] - 19800))	
			sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset'] - 19800))
			print(f'Currently it\'s {temp}°C with {condition} in {city} with high of {max_temp}°C and low of {min_temp}°C.')
			speak(f'currently its {temp} degrees with {condition} in {city} with high of {max_temp} and low of {min_temp}')

		elif 'tell me the weather' in query:
			speak('name the city please')
			city = takeCommand().lower()
			api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=--Your API ID of Open Weather Map"
			json_data = requests.get(api).json()
			condition = json_data['weather'][0]['main']
			temp = int(json_data['main']['temp'] - 273.15)
			min_temp = int(json_data['main']['temp_min'] - 273.15)
			max_temp = int(json_data['main']['temp_max'] - 273.15)
			pressure = json_data['main']['pressure']
			humidity = json_data['main']['humidity']
			wind = json_data['wind']['speed']
			sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise'] - 19800))	
			sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset'] - 19800))
			print(f'Currently it\'s {temp}°C with {condition} in {city} with high of {max_temp}°C and low of {min_temp}°C.')
			speak(f'currently its {temp} degrees with {condition} in {city} with high of {max_temp} and low of {min_temp}')


		elif 'weather in' in query:
			city = query.replace('weather in','')
			api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=--Your API ID of Open Weather Map"
			json_data = requests.get(api).json()
			condition = json_data['weather'][0]['main']
			temp = int(json_data['main']['temp'] - 273.15)
			min_temp = int(json_data['main']['temp_min'] - 273.15)
			max_temp = int(json_data['main']['temp_max'] - 273.15)
			pressure = json_data['main']['pressure']
			humidity = json_data['main']['humidity']
			wind = json_data['wind']['speed']
			sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise'] - 19800))	
			sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset'] - 19800))
			print(f'Currently it\'s {temp}°C with {condition} in {city} with high of {max_temp}°C and low of {min_temp}°C.')
			speak(f'currently its {temp} degrees with {condition} in {city} with high of {max_temp} and low of {min_temp}')

		elif 'what is the weather' in query:
			speak('name the city please')
			city = takeCommand().lower()
			api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=--Your API ID of Open Weather Map"
			json_data = requests.get(api).json()
			condition = json_data['weather'][0]['main']
			temp = int(json_data['main']['temp'] - 273.15)
			min_temp = int(json_data['main']['temp_min'] - 273.15)
			max_temp = int(json_data['main']['temp_max'] - 273.15)
			pressure = json_data['main']['pressure']
			humidity = json_data['main']['humidity']
			wind = json_data['wind']['speed']
			sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise'] - 19800))	
			sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset'] - 19800))
			print(f'Currently it\'s {temp}°C with {condition} in {city} with high of {max_temp}°C and low of {min_temp}°C.')
			speak(f'currently its {temp} degrees with {condition} in {city} with high of {max_temp} and low of {min_temp}')

		elif 'what is the temperature in' in query:
			city = query.replace('what is temperature in','')
			api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=--Your API ID of Open Weather Map"
			json_data = requests.get(api).json()
			condition = json_data['weather'][0]['main']
			temp = int(json_data['main']['temp'] - 273.15)
			min_temp = int(json_data['main']['temp_min'] - 273.15)
			max_temp = int(json_data['main']['temp_max'] - 273.15)
			print(f'Currently it\'s {temp}°C with {condition} in {city} with high of {max_temp}°C and low of {min_temp}°C.')
			speak(f'currently its {temp} degrees with {condition} in {city} with high of {max_temp} and low of {min_temp}')

		elif 'temperature in' in query:
			city = query.replace('temperature in','')
			api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=--Your API ID of Open Weather Map"
			json_data = requests.get(api).json()
			condition = json_data['weather'][0]['main']
			temp = int(json_data['main']['temp'] - 273.15)
			min_temp = int(json_data['main']['temp_min'] - 273.15)
			max_temp = int(json_data['main']['temp_max'] - 273.15)
			print(f'Currently it\'s {temp}°C with {condition} in {city} with high of {max_temp}°C and low of {min_temp}°C.')
			speak(f'currently its {temp} degrees with {condition} in {city} with high of {max_temp} and low of {min_temp}')

		elif 'what is the temperature of' in query:
			city = query.replace('what is the temperature of','')
			api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=--Your API ID of Open Weather Map"
			json_data = requests.get(api).json()
			condition = json_data['weather'][0]['main']
			temp = int(json_data['main']['temp'] - 273.15)
			min_temp = int(json_data['main']['temp_min'] - 273.15)
			max_temp = int(json_data['main']['temp_max'] - 273.15)
			print(f'Currently it\'s {temp}°C with {condition} in {city} with high of {max_temp}°C and low of {min_temp}°C.')
			speak(f'currently its {temp} degrees with {condition} in {city} with high of {max_temp} and low of {min_temp}')

		elif 'temperature of' in query:
			city = query.replace('temperature of','')
			api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=--Your API ID of Open Weather Map"
			json_data = requests.get(api).json()
			condition = json_data['weather'][0]['main']
			temp = int(json_data['main']['temp'] - 273.15)
			min_temp = int(json_data['main']['temp_min'] - 273.15)
			max_temp = int(json_data['main']['temp_max'] - 273.15)
			print(f'Currently it\'s {temp}°C with {condition} in {city} with high of {max_temp}°C and low of {min_temp}°C.')
			speak(f'currently its {temp} degrees with {condition} in {city} with high of {max_temp} and low of {min_temp}')

		elif 'what is the temperature' in query:
			speak('name the city please')
			city = takeCommand().lower()
			api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=--Your API ID of Open Weather Map"
			json_data = requests.get(api).json()
			condition = json_data['weather'][0]['main']
			temp = int(json_data['main']['temp'] - 273.15)
			min_temp = int(json_data['main']['temp_min'] - 273.15)
			max_temp = int(json_data['main']['temp_max'] - 273.15)
			print(f'Currently it\'s {temp}°C with {condition} in {city} with high of {max_temp}°C and low of {min_temp}°C.')
			speak(f'currently its {temp} degrees with {condition} in {city} with high of {max_temp} and low of {min_temp}')
		
		elif 'sunrise in' in query:
			city = query.replace('sunrise in','')
			api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=--Your API ID of Open Weather Map"
			json_data = requests.get(api).json()
			min_temp = int(json_data['main']['temp_min'] - 273.15)
			max_temp = int(json_data['main']['temp_max'] - 273.15)
			sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise'] - 19800))	
			sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset'] - 19800))
			print(f'In {city}, Sunrise time will be {sunrise} and sunset time will be {sunset}.')
			speak(f'In {city}, Sunrise time will be {sunrise} and sunset time will be {sunset}')

		elif 'sunrise of' in query:
			city = query.replace('sunrise of','')
			api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=--Your API ID of Open Weather Map"
			json_data = requests.get(api).json()
			min_temp = int(json_data['main']['temp_min'] - 273.15)
			max_temp = int(json_data['main']['temp_max'] - 273.15)
			sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise'] - 19800))	
			sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset'] - 19800))
			print(f'In {city}, Sunrise time will be {sunrise} and sunset time will be {sunset}.')
			speak(f'In {city}, Sunrise time will be {sunrise} and sunset time will be {sunset}')

		elif 'sunrise' in query:
			speak('name the city please')
			city = takeCommand().lower()
			api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=--Your API ID of Open Weather Map"
			json_data = requests.get(api).json()
			min_temp = int(json_data['main']['temp_min'] - 273.15)
			max_temp = int(json_data['main']['temp_max'] - 273.15)
			sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise'] - 19800))	
			sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset'] - 19800))
			print(f'In {city}, Sunrise time will be {sunrise} and sunset time will be {sunset}.')
			speak(f'In {city}, Sunrise time will be {sunrise} and sunset time will be {sunset}')

		elif 'sunset in' in query:
			city = query.replace('sunset in','')
			api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=--Your API ID of Open Weather Map"
			json_data = requests.get(api).json()
			min_temp = int(json_data['main']['temp_min'] - 273.15)
			max_temp = int(json_data['main']['temp_max'] - 273.15)
			sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise'] - 19800))	
			sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset'] - 19800))
			print(f'In {city}, Sunrise time will be {sunrise} and sunset time will be {sunset}.')
			speak(f'In {city}, Sunrise time will be {sunrise} and sunset time will be {sunset}')

		elif 'sunset of' in query:
			city = query.replace('sunset of','')
			api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=--Your API ID of Open Weather Map"
			json_data = requests.get(api).json()
			min_temp = int(json_data['main']['temp_min'] - 273.15)
			max_temp = int(json_data['main']['temp_max'] - 273.15)
			sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise'] - 19800))	
			sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset'] - 19800))
			print(f'In {city}, Sunrise time will be {sunrise} and sunset time will be {sunset}.')
			speak(f'In {city}, Sunrise time will be {sunrise} and sunset time will be {sunset}')

		elif 'sunset' in query:
			speak('name the city please')
			city = takeCommand().lower()
			api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=--Your API ID of Open Weather Map"
			json_data = requests.get(api).json()
			min_temp = int(json_data['main']['temp_min'] - 273.15)
			max_temp = int(json_data['main']['temp_max'] - 273.15)
			sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise'] - 19800))	
			sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset'] - 19800))
			print(f'In {city}, Sunrise time will be {sunrise} and sunset time will be {sunset}.')
			speak(f'In {city}, Sunrise time will be {sunrise} and sunset time will be {sunset}')

		elif 'what is' in query:
			query = query.replace('what is','')
			base_url = "http://www.google.com/search?q="
			final_url = base_url + quote(query)
			webbrowser.get('brave').open(final_url)

		elif 'how many' in query:
			base_url = "http://www.google.com/search?q="
			final_url = base_url + quote(query)
			webbrowser.get('brave').open(final_url)

		elif 'tell me about' in query:
			query = query.replace('tell me about','')
			base_url = "http://www.google.com/search?q="
			final_url = base_url + quote(query)
			webbrowser.get('brave').open(final_url)

		elif 'who is' in query:
			query = query.replace('who is','')
			base_url = "http://www.google.com/search?q="
			final_url = base_url + quote(query)
			webbrowser.get('brave').open(final_url)

		elif 'which is' in query:
			base_url = "http://www.google.com/search?q="
			final_url = base_url + quote(query)
			webbrowser.get('brave').open(final_url)

		elif 'which have' in query:
			base_url = "http://www.google.com/search?q="
			final_url = base_url + quote(query)
			webbrowser.get('brave').open(final_url)

		elif 'how to' in query:
			base_url = "http://www.google.com/search?q="
			final_url = base_url + quote(query)
			webbrowser.get('brave').open(final_url)
		
		elif 'how do' in query:
			base_url = "http://www.google.com/search?q="
			final_url = base_url + quote(query)
			webbrowser.get('brave').open(final_url)

		elif 'open amazon' in query:
			webbrowser.get('brave').open('amazon.in')

		elif 'on amazon' in query:
			query = query.replace('on amazon','')
			base_url = "https://www.amazon.in/s?k="
			final_url = base_url + quote(query)
			webbrowser.get('brave').open(final_url)

		elif 'open flipkart' in query:
			webbrowser.get('brave').open('flipkart.com')

		elif 'on flipkart' in query:
			query = query.replace('on flipkart','')
			base_url = "https://www.flipkart.com/search?q="
			final_url = base_url + quote(query)
			webbrowser.get('brave').open(final_url)

		elif 'open gmail' in query:
			webbrowser.get('brave').open('https://mail.google.com/mail/u/0/#inbox')

		elif 'open other gmail' in query:
			webbrowser.get('brave').open('https://mail.google.com/mail/u/1/#inbox')

		elif 'open instagram' in query:
			webbrowser.get('brave').open('www.instagram.com')

		elif 'on instagram' in query:
			base_url = "http://www.google.com/search?q="
			final_url = base_url + quote(query)
			webbrowser.get('brave').open(final_url)

		elif 'open facebook' in query:
			webbrowser.get('brave').open('www.facebook.com')

		elif 'on facebook' in query:
			base_url = "http://www.google.com/search?q="
			final_url = base_url + quote(query)
			webbrowser.get('brave').open(final_url)

		elif 'open twitter' in query:
			webbrowser.get('brave').open('www.twitter.com')

		elif 'on twitter' in query:
			base_url = "http://www.google.com/search?q="
			final_url = base_url + quote(query)
			webbrowser.get('brave').open(final_url)

		elif 'open hotstar' in query:
			webbrowser.get('chrome').open('https://www.hotstar.com/in')

		elif 'on hotstar' in query:
			base_url = "http://www.google.com/search?q="
			final_url = base_url + quote(query)
			webbrowser.get('brave').open(final_url)

		elif 'open google notes' in query:
			webbrowser.get('brave').open('https://keep.google.com/')

		elif 'open notes' in query:
			webbrowser.get('brave').open('https://keep.google.com/')

		elif 'open google keeps' in query:
			webbrowser.get('brave').open('https://keep.google.com/')

		elif 'open keeps' in query:
			webbrowser.get('brave').open('https://keep.google.com/')

		elif 'open notepad' in query:
			notepadPath = 'C:\\WINDOWS\\system32\\notepad.exe'
			os.startfile(notepadPath)

		elif 'close notepad' in query:
			os.system("TASKKILL /F /IM notepad.exe")

		elif 'open word' in query:
			wordPath = 'C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.exe'
			os.startfile(wordPath)

		elif 'close word' in query:
			os.system("TASKKILL /F /IM word.exe")

		elif 'open paint' in query:
			paintPath = 'C:\\WINDOWS\\system32\\mspaint.exe'
			os.startfile(paintPath)

		elif 'close paint' in query:
			os.system("TASKKILL /F /IM paint.exe")

		elif 'write this' in query:
			app = application.Application()
			app.start("Notepad.exe")
			speak('What to write')
			print('Writing...')
			note = 'hello'
			while 'done' not in note:
				note = takeCommand().lower()
				app.Notepad.Edit.TypeKeys((f"{note} %s"), with_spaces = True)
		
		elif 'open download' in query:
			downloadPath = '--Location of Downloads Folder'
			os.startfile(downloadPath)

		elif 'open downloads' in query:
			downloadPath = '--Location of Downloads Folder'
			os.startfile(downloadPath)					
			
		elif 'open screenshot' in query:
			screenshotsPath = '--Location of Screenshots Folder'
			os.startfile(screenshotsPath)

		elif 'open screenshots' in query:
			screenshotsPath = '--Location of Screenshots Folder'
			os.startfile(screenshotsPath)

		elif 'open' in query:
			query = query.replace('open','')
			base_url = "http://www.google.com/search?q="
			final_url = base_url + quote(query)
			webbrowser.get('brave').open(final_url)

		elif 'set alarm' in query:
			speak('Please select hour in 24 hours format')
			hour = takeCommand().lower()
			speak('Please select minute')
			min = takeCommand().lower()
			if int(min)<10:
				min = f'0{min}'
				min = str(min)
			set_alarm_timer = f"{hour}:{min}"
			speak(f'Done your alarm has been set for {hour} hour and {min} minutes')
			while True:
				current_time = datetime.datetime.now()
				now = current_time.strftime("%H:%M")
				if now == set_alarm_timer:
					notification.notify(
					title = '**Time to Wake Up !!!',
					message = 'You should wake up now !!!!!',
					app_icon = "alarm_icon.ico",
					timeout = 30
						)
					winsound.PlaySound("alarm_audio.wav",winsound.SND_FILENAME)
					break

		elif 'set reminder' in query:
			speak('what is the title of remaider')
			title = takeCommand().lower()
			speak('what is the message')
			message = takeCommand().lower()
			speak('Please select hour in 24 hours format')
			hour = takeCommand().lower()
			speak('Please select minute')
			min = takeCommand().lower()
			if int(min)<10:
				min = f'0{min}'
				min = str(min)
			set_alarm_timer = f"{hour}:{min}"
			speak(f'Done your remainder has been set for {hour} hour and {min} minutes')
			while True:
				current_time = datetime.datetime.now()
				now = current_time.strftime("%H:%M")
				if now == set_alarm_timer:
					notification.notify(
					title = title,
					message = message,
					app_icon = "reminder_icon.ico",
					timeout = 60
						)
					winsound.PlaySound("reminder_audio.wav",winsound.SND_FILENAME)
					break

		elif 'double' in query:
			k.press_key(k.alt_key)
			k.tap_key(k.tab_key,n=2,interval=0.1)
			k.release_key(k.alt_key)

		elif 'interchange' in query:
			k.press_key(k.alt_key)
			k.tap_key(k.tab_key)
			k.release_key(k.alt_key)

		elif 'touching' in query:
			k.press_key(k.alt_key)
			k.tap_key(k.tab_key)
			k.release_key(k.alt_key)

		elif 'type' in query:
			recite = query.replace('type','')
			k.type_string(recite)

		elif 'type and search' in query:
			recite = query.replace('type and search','')
			k.type_string(recite)
			k.tap_key(k.enter_key)

		elif 'type and enter' in query:
			recite = query.replace('type and enter','')
			k.type_string(recite)
			k.tap_key(k.enter_key)

		elif 'backward' in query:
			k.tap_key(k.browser_back_key)
		
		elif 'forward' in query:
			k.tap_key(k.browser_forward_key)

		elif 'volume up' in query:
			for i in range(12):
				k.tap_key(k.volume_up_key)
		
		elif 'volume down' in query:
			for i in range(12):
				k.tap_key(k.volume_down_key)

		elif 'up' in query:
			k.tap_key(k.page_up_key)
		
		elif 'down' in query:
			k.tap_key(k.page_down_key)

		elif 'full screen' in query:
			k.tap_key('f')
		
		elif 'mute' in query:
			k.tap_key(k.volume_mute_key)
		
		elif 'unmute' in query:
			k.tap_key(k.volume_mute_key)

		elif 'brightness up' in query:
			k.press_key(k.function_keys)
			k.tap_key(k.left_key)
			k.release_key(k.function_keys)

		elif 'escape' in query:
			k.tap_key(k.escape_key)
		
		elif 'close tab' in query:
			k.press_key(k.control_l_key)
			k.tap_key('w')
			k.release_key(k.control_l_key)

		elif 'new tab' in query:
			k.press_key(k.control_l_key)
			k.tap_key('t')
			k.release_key(k.control_l_key)

		elif 'first tab' in query:
			k.press_key(k.control_l_key)
			k.tap_key(k.numpad_keys[1])
			k.release_key(k.control_l_key)

		elif 'second tab' in query:
			k.press_key(k.control_l_key)
			k.tap_key(k.numpad_keys[2])
			k.release_key(k.control_l_key)

		elif 'third tab' in query:
			k.press_key(k.control_l_key)
			k.tap_key(k.numpad_keys[3])
			k.release_key(k.control_l_key)

		elif 'forth tab' in query:
			k.press_key(k.control_l_key)
			k.tap_key(k.numpad_keys[4])
			k.release_key(k.control_l_key)

		elif 'fifth tab' in query:
			k.press_key(k.control_l_key)
			k.tap_key(k.numpad_keys[5])
			k.release_key(k.control_l_key)

		elif 'maximize' in query:
			k.press_key(k.windows_l_key)
			k.tap_key(k.up_key)
			k.release_key(k.windows_l_key)
		
		elif 'minimise' in query:
			k.press_key(k.windows_l_key)
			k.tap_key(k.down_key)
			k.release_key(k.windows_l_key)

		elif 'joke' in query:
			jokeV = pyjokes.get_joke()
			print(jokeV)
			speak(jokeV)

		elif 'pick a number' in query:
			speak('tell the least number')
			min_num = takeCommand().lower()
			min_num = int(min_num)
			speak('tell the highest number')
			max_num = takeCommand().lower()
			max_num = int(max_num)
			randomNum = random.randint(min_num,max_num)
			print(f'The random number is {randomNum}.')
			speak(f'the random number is {randomNum}')

		elif 'screenshot' in query:
			k.press_key(k.windows_l_key)
			k.tap_key(k.print_screen_key)
			k.release_key(k.windows_l_key)
		
		elif 'resume' in query:
			k.tap_key(k.media_play_pause_key)

		elif 'pause' in query:
			k.tap_key(k.media_play_pause_key)

		elif 'next' in query:
			k.tap_key(k.media_next_track_key)

		elif 'previous' in query:
			k.tap_key(k.media_prev_track_key)

		elif 'shutdown' in query:
			speak('Are you sure you shutdown your pc')
			shutdownAns = takeCommand().lower()
			if shutdownAns == 'no':
				speak('sure your pc will not shutdown')
			elif shutdownAns == 'yes':
				speak('your pc will shutdown in few seconds')
				os.system("shutdown /s /t 1")

		elif 'restart' in query:
			speak('Are you sure you want to restart your pc')
			restartAns = takeCommand().lower()
			if restartAns == 'no':
				speak('sure your pc will not restart')
			elif restartAns == 'yes':
				speak('your pc will restart in few seconds')
				os.system("shutdown /r /t 1")

		elif 'sleep' in query:
			speak('Are you sure you want to put your pc in sleep mode')
			restartAns = takeCommand().lower()
			if restartAns == 'no':
				speak('sure your pc will not sleep')
			elif restartAns == 'yes':
				speak('your pc will go to sleep in few seconds')
				os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

		
		

		





		


		