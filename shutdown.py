import os
from gpiozero import Button
button = Button(2)
def print_thing():
    print ("button pressed")
    os.system("sudo shutdown -r now")

button.when_pressed = print_thing