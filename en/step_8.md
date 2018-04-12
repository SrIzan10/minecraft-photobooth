## Putting it all together

Now you have a working photobooth we need to add the camera module to take a picture. We will add a quick reminder to smile and then call the camera capture code.

- Add the instructions to send messages to Minecraft and the call to `capture()` inside your `if` statement:

    ```python
    if x >= 10.5 and y == 9.0 and z == -44.3:
        mc.postToChat("You are in the Photobooth!")
        sleep(1)
        mc.postToChat("Smile!")
        sleep(1)
        camera.start_preview()
        sleep(2)
        camera.capture('/home/pi/selfie.jpg')
        camera.stop_preview()

    sleep(3)
    ```

This will keep checking your location. When your location matches that of the photobooth, it will take a picture with the camera.

