## Testing whether you are in the Photobooth

At this point we have a photobooth, the coordinates of the trigger block, and code to control the camera module and take a picture. The next step is to test whether the program identifies when you are in the photobooth. To do this we must create a loop which checks if your player's co-ordinates match the trigger block coordinates. If they do, then you are standing in the photobooth. To do this we use a simple `if` statement, which we call a conditional.

--- task ---

Change the lines inside your `while` loop to test the players position below:

```python
while True:
    x, y, z = mc.player.getPos()

    sleep(3)

    if x >= 10.5 and y == 9.0 and z == -44.3:
        mc.postToChat("You are in the photobooth!")
```

You will note that the `if` statement checks if `x` value is greater than or equal to `10.5`: this is ensure that it picks up the block as it could have a value of `10.6`. 

--- /task ---

--- task ---

Change the coordinates in the if statement to those of your own photobooth.

--- hints ---

--- hint ---

Replace the `x`, `y`, and `z` values with the values from your photobooth.

--- /hint ---

--- hint ---

This line of code will need changing:

```python
if x >= 10.5 and y == 9.0 and z == -44.3:
```

--- /hint ---

--- hint ---

If your photobooth was at position `11.5, 3, 34.5` the code will need changing too:

```python
if x >= 11.5 and y == 3.0 and z == 34.5:
```

You may also need to change the operators `>=`, `==` to `<=` depending on the position of your photobooth and its entrance.

--- /hint ---

--- /hints ---

--- /task ---

--- task ---

Save and run your code to test it: walk into your photobooth and you should see the message "You are in the photobooth!" in the Minecraft window.

--- /task ---

