import keyboard

print("Press 'a' to test key press detection")
while True:
    if keyboard.is_pressed('a'):
        print("Key 'a' was pressed")
        break
