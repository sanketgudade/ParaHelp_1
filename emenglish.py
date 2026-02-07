from pynput import keyboard
from playsound import playsound
import time
import os
import pygetwindow as gw  # For getting the active window (install via `pip install pygetwindow`)

enter_count = 0
last_time = time.time()
target_html_file = 'Main.html'  # Change this to the name of your HTML file

# Function to stop any ongoing audio or media
def stop_other_sounds():
    try:
        os.system("pkill -f Emergency.mp3")  # Stop if another emergency sound is already playing
        print("Stopped any ongoing sounds.")
    except Exception as e:
        print(f"Error stopping sounds: {e}")

# Function to check if the active window is the browser showing the target HTML file
def is_html_file_active():
    try:
        active_window = gw.getActiveWindow()
        if active_window and target_html_file in active_window.title:
            return True
        return False
    except Exception as e:
        print(f"Error checking active window: {e}")
        return False

def on_press(key):
    global enter_count, last_time
    
    # Check if the active window is the browser showing the target HTML file
    if not is_html_file_active():
        return  # Do nothing if we're not in the correct browser tab

    if key == keyboard.Key.enter:
        current_time = time.time()

        # Reset enter_count if more than 1 second has passed
        if current_time - last_time > 1:
            enter_count = 0
        
        enter_count += 1
        last_time = current_time
        
        if enter_count == 2:  # Double enter detected
            print("Playing emergency voice note...")

            # Stop all other sounds or media
            stop_other_sounds()

            # Play the emergency sound 3 times
            for _ in range(3):  
                playsound('Emergency.mp3')
            enter_count = 0  # Reset the count after playing the sound

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener if ESC is pressed

# Start the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


