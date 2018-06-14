## Take a picture

Next, you'll write some code to take a picture with the camera.

--- task ---

Add the following lines to the end of your program:

``` python
camera.start_preview()
sleep(2)
camera.capture('/home/pi/selfie.jpg')
camera.stop_preview()
```

We have set the camera to show a two second preview so that you can strike your pose and smile before the picture is taken. The image is stored as a file called `selfie.jpg` in your home directory.

--- /task ---

--- task ---

Save and run your program to take a picture!

--- /task ---

--- task ---

Open the File Manager to view the picture you took.

--- /task ---


