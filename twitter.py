from twython import Twython
import time
import RPi.GPIO as GPIO
import camera

APP_KEY = 'y41mgd4xnJny8S8YKdzhc5j1S'
APP_SECRET = 'o1DSRJGGtZkBZANwu92yZMlBPiR31QEsAkRqPkefcRi1zS1N3y'
OAUTH_TOKEN = '2505082970-OslkWNt2YHfVmiRFIuI4W0GgGFQB1n4cSsjYL9t'
OAUTH_TOKEN_SECRET = 'G0eAgs48U7dlIeC0rehWlb0A6njw0QByquqnFbEe9gAKg'

LED = 24
BUTTON = 23
light_on = False
x = 0

GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def printFunction(channel):
	global light_on
	print("Button pressed")

	camera.cameramain()

	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	
	photo = open('photo.jpg', 'rb')
	twitter.update_status_with_media(status='Checkout this cool image!', media=photo)

	if(not light_on):
		GPIO.output(LED, True)
		light_on = True
	else:
		GPIO.output(LED, False)
		light_on = False

GPIO.add_event_detect(BUTTON, GPIO.RISING, callback=printFunction, bouncetime=300)

while True:
	if(light_on):
		x += 1
	else:
		x -= 1	

#twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#twitter.update_status(status='TWEET!')
