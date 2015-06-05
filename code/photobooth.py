from mcpi import minecraft
from picamera import PiCamera
from time import sleep

def take_the_pic():
    with PiCamera() as camera:
        camera.start_preview()
        sleep(2)
        camera.capture('/home/pi/selfie.jpg')

mc = minecraft.Minecraft.create()

mc.postToChat("Find the photobooth")

while True:
    x, y, z = mc.player.getPos()
       
    sleep(3)
    
    if x >= 10.5 and y == 9.0 and z == -44.3:
        mc.postToChat("You are in the photobooth!")
        sleep(1)
        mc.postToChat("Smile!")
        sleep(1)
        take_the_pic()
        mc.postToChat("Check out your picture")
        sleep(5)
