from mcpi.minecraft import Minecraft
from picamera import PiCamera
from time import sleep

mc = Minecraft.create()
camera = PiCamera()

mc.postToChat("Find the photobooth")

while True:
    x, y, z = mc.player.getPos()

    if x >= 10.5 and y == 9.0 and z == -44.3:
        mc.postToChat("You are in the photobooth!")
        sleep(1)
        mc.postToChat("Smile!")
        sleep(1)
        camera.start_preview()
        sleep(2)
        camera.capture('/home/pi/selfie.jpg')
        camera.stop_preview()
        mc.postToChat("Check out your picture")

    sleep(3)
