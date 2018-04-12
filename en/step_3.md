## Importing the Minecraft and PiCamera Modules

The first thing you need to do is import the Minecraft API (Application Programming Interface). This enables you to connect to Minecraft and use Python to code. You also need to import the PiCamera module to control the camera and the time module to add a small delay between taking the photo and then taking the next photo.

- Open Minecraft from the application menu; enter an existing world or create a new one.

- Move the Minecraft window to one side of the screen.

    You'll need to use the `Tab` key to take your mouse's focus away from the Minecraft window to move it. You'll need this later when you switch between the Minecraft and Python windows.

- Open Python 3 from the **programming** menu:

    ![Open Python 3](images/python3-app-menu.png)

    This will open up the Python IDLE code editor which you will use to write the photobooth program.

- Click `New > Window` to open a new window.

- Enter the code shown below:

	``` python
	from mcpi.minecraft import Minecraft
	from picamera import PiCamera
	from time import sleep

	mc = Minecraft.create()
    camera = PiCamera()

	mc.postToChat("Hello world")
	```

- Save with `Ctrl + S` and run the program with `F5`. You should see the message "Hello world" appear in the Minecraft world.

