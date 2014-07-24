from twython import Twython
import time
import RPi.GPIO as GPIO
import camera

#Variables to store your twitter authentication info
APP_KEY = 'y41mgd4xnJny8S8YKdzhc5j1S'
APP_SECRET = 'o1DSRJGGtZkBZANwu92yZMlBPiR31QEsAkRqPkefcRi1zS1N3y'
OAUTH_TOKEN = '2505082970-OslkWNt2YHfVmiRFIuI4W0GgGFQB1n4cSsjYL9t'
OAUTH_TOKEN_SECRET = 'G0eAgs48U7dlIeC0rehWlb0A6njw0QByquqnFbEe9gAKg'

#Pin connected to your button
BUTTON = 23

x = 0

#Set the pinmode for the board
GPIO.setmode(GPIO.BOARD)

#Set the mode for your button pin
GPIO.setup(BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def printFunction(channel):
	global light_on
	print("Button pressed")

	#Run the function to take a picture
	camera.cameramain()

	#Pass authentication info into Twython
	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	
	#Store the photo
	photo = open('photo.jpg', 'rb')

	#Tweet the photo
	twitter.update_status_with_media(status='Checkout this cool image!', media=photo)

#Add event listener to listen for the button press
GPIO.add_event_detect(BUTTON, GPIO.RISING, callback=printFunction, bouncetime=300)

while True:
	x += 1
	x -= 1	
