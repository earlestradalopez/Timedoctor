import time
def downloadFile(url, file):
	import urllib.request
	print('Beginning file download with urllib2...')
	urllib.request.urlretrieve(url, file)
	print('Download completed...')

def runFile(file):
	import subprocess
	pid = subprocess.Popen([file]).pid

def runFileWait(file):
	import os
	os.system(file)

def sendKeys(key):
	import keyboard
	_value = key.split(' ')
	keyboard.send(_value[0])
	time.sleep(int(_value[1]))

def key_write(text):
	import keyboard
	keyboard.write(text)

def mouse_click(sec):
	import pyautogui	
	pyautogui.click()
	time.sleep(int(sec))

def mouse_move(xy):
	import pyautogui	
	_xy = xy.split(' ')
	pyautogui.moveTo(int(_xy[0]), int(_xy[1]))
	time.sleep(int(_xy[2]))

def osSleep(sec):
	import os
	secs = sec.split(' ')
	os.system("timeout " + secs[0])

def check_file_exist(_file):
	import pathlib	
	file = pathlib.Path(_file)
	for x in range(10):
		if file.exists ():
			time.sleep(10)
			return True
		time.sleep(5)
	return False

def check_file_not_exist(_file):
	import pathlib
	file = pathlib.Path(_file)
	for x in range(10):
		if not file.exists ():
			time.sleep(10)
			return True
		time.sleep(5)
	return False

def get_set_config(value):
	import configparser
	config = configparser.ConfigParser()		
	_value = value.split(' ')
	if len(_value) == 2:		
		config.read('config.ini')
		return config[_value[0]][_value[1]]
	else:		
		config.set(_value[0],_value[1],_value[2])
		config.set('DEFAULT', 'timestart', timeparse())
		with open('config.ini', 'w') as configfile:
			config.write(configfile)

def signup():
	import requests
	import json
	from datetime import datetime
	url = 'https://api2.timedoctor.com:443/api/1.0/register/signup'
	dateTimeObj = datetime.now() 
	timestampStr = dateTimeObj.strftime("%Y-%m-%d.%H.%M")
	email = "qa-automation-earl-" + timestampStr + "@timedoctor.dev"
	myobj = {
	  "name": "qa-automation-earll",
	  "email": email,
	  "password": "123456",
	  "company": "qa-automation-earl",
	  "trackingMode": "silent",
	  "timezone": "",
	  "referrer": "",
	  "pricingPlan": "",
	  "splitTest": [
	    {
	      "name": "",
	      "value": ""
	    }
	  ]
	}
	data = requests.post(url, json =  myobj)
	json_load = json.loads(data.content)
	print (json_load)
	if(str(json_load).find('error') == -1):
		get_set_config("DEFAULT email " + email)
		return email
	else:
		print("Unsuccessful registration!")
		return ''

def getAuthorizationDetails(value):
	import requests
	import json
	url = 'https://api2.timedoctor.com:443/api/1.0/authorization/login'
	email = get_set_config("DEFAULT email")
	myobj = {
  		"deviceId": "",
  		"email": email,
		"password": "123456",
		"totpCode": "",
		"permissions": ""
		}
	data = requests.post(url, json =  myobj)
	json_load = json.loads(data.content)
	if value == 'token':
		return json_load["data"]["token"]
	if value == 'company_id':
		return json_load["data"]["companies"][0]["id"]
	else:
		return json_load["data"]["token"] + " " + json_load["data"]["companies"][0]["id"]

def getActivityTimeuse(tokenid):
	import requests
	import json
	_value = tokenid.split(' ')
	url = 'https://api2.timedoctor.com:443/api/1.0/activity/timeuse?company=' + _value[1] + '&&from=' + get_set_config("DEFAULT timestart").replace(':','%3A') + '&to=' + timeparse().replace(':','%3A') + '&&&&&&&token=' + _value[0]
	data = requests.get(url)
	json_load = json.loads(data.content)
	print(json_load)
	_apps = ["Time Doctor 2 | v3.0.52", "Untitled - Google Chrome", "The Verge - Google Chrome", "Untitled - Google Chrome", "Facebook - Log In or Sign Up - Google Chrome", "Calculator", "Untitled - Google Chrome", "api2.timedoctor.com - Google Chrome", "Calculator", "Question", "Setup"]
	#_void_app = ["Windows Security Alert", "Administrator: Command Prompt", "Select Administrator: Command Prompt"]
	x = 0
	for _data in json_load["data"][0]:
		if(x == len(_apps)):
			print("True")
			return True
		elif(_data["title"].startswith(_apps[x])):
			x+=1
	print("False")
	return False

def timeparse():
	import datetime
	dateTimeObj = datetime.datetime.now(tz=datetime.timezone.utc)
	timestampStr = dateTimeObj.strftime("%Y-%m-%dT%H:%M:%S.00")
	return timestampStr 

def window_activate(text):
	import win32gui
	w = win32gui
	_window = w.GetWindowText (w.GetForegroundWindow())
	print(_window)
	if(_window.startswith(text) == -1):
		time.sleep(10)
		_window = w.GetWindowText (w.GetForegroundWindow())
		print(_window)
		sendKeys('alt+tab 3')

