import time
import threading

from espalexa import Espalexa

# create a espalexa object
espalexa = Espalexa()

# callback function for dimmable device
def callback(brightness):
	print("Brightness: " + str(brightness))

# callback function for color device
def callback_color(brightness, rgb):
	print("Brightness: " + str(brightness))
	print(rgb)
	print("Red: " + str((rgb >> 16) & 0xFF) + ", Green: " + str((rgb >> 8) & 0xFF) + ", Blue: " + str(rgb & 0xFF))
		
def loop(espalexa):
	while True:
		espalexa.loop()
		time.sleep(1)
			
if __name__ == "__main__":
	# add devices
	espalexa.addDevice("Light without color", callback, "dimmable")
	espalexa.addDevice("Light with color", callback_color, "extendedcolor")
	
	# initialize espalexa
	espalexa.begin()	
			
	# start the espalexa loop thread
	t = threading.Thread(target = loop, args = (espalexa,))
	t.daemon = True
	t.start()
	
	# keep the script running
	while True:
		print(".")
		time.sleep(60)
