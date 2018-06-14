## Finding your position

When you are playing Minecraft, your program will need to verify that you are inside the photobooth. If you are, then it will trigger the `take_the_pic` function and take a picture with the camera. To do this, Minecraft needs to know where you are in the world.

To find your position, you use the code, `x, y, x = mc.player.getPos()`.  This saves the `x`, `y`, and `z` position of your player into the variables `x`, `y`, and `z`.  You can then use `print(x)` to print the `x` value, or `print(x, y, z)` to see them all. Now you know the position of the player, you can test to see if they are in the photobooth. As we're using Minecraft we can also use `mc.postToChat` to send the coordinates to the Minecraft window.

--- task ---

Change the message "Hello world" to "Find the photobooth" after the `Minecraft.create()` line like so:

```python
mc = Minecraft.create()

mc.postToChat("Find the photobooth")
```

--- /task ---

--- task ---

Add to the end of your code:

``` python
while True:
    x, y, z, = mc.player.getPos()
    mc.postToChat((x, y, z))
```

--- /task ---

--- task ---

Save and run the code and you'll see your coordinates posted to the Minecraft window.

--- /task ---

--- task ---

Focus on the Python window and press `Ctrl + C` to stop the code running.

--- /task ---

