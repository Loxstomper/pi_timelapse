# Created by Lochie Ashcroft

from picamera import Picamera
from os import system
from time import sleep


# Functions
def user_settings():
    global number_photos
    global delay
    number_photos = int(input("Please enter number of photos to be taken (leave blank for unlimited): "))
    delay = int(input("Please enter the delay between photos in seconds: "))
    confirm_settings()


def confirm_settings():
    print("Confirming settings. ", number_photos, " photo(s) will be taken with a delay of ", delay)
    correct = input("Is this correct? [Y/n]: ")

    if correct == "Y" or correct == "y":
        pass
    elif correct == "N" or correct == "n":
        user_settings()
    else:
        print("Incorrect input returning to the start.")
        sleep(1)
        user_settings()


# Camera Setup
camera = PiCamera()
camera.resolution = (1920, 1080)  # can go more but 1080p is good

# shout out to me
print("Created by Lochie Ashcroft.\n\n")

user_settings()

# clear terminal
system("clear")

# decide if infinite photos or a max number of photos
if number_photos == "":
    print("Starting capture now!")
    print("To stop at any time hold down ctrl+c")
    i = 0
    while True:
        camera.capture('image{0:05d}.jpg'.format(i))
        i += 1  # because not using a for loop
        sleep(delay)

else:
    print("Starting capture now!")
    print("To stop at any time hold down ctrl+c")
    print("Total capture time = ", number_photos * delay, " seconds")

    for i in range(number_photos + 1):
        camera.capture('image{0:05d}.jpg'.format(i))
        print(i, "/", number_photos)
        sleep(delay)


