import keyboard
import pyautogui
import time

# Track the time of the last Enter press
last_enter_press_time = 0

# Time window to detect double Enter press (in seconds)
double_press_threshold = 0.5

# Function to be called when Enter is pressed
def on_enter_press(event):
    global last_enter_press_time
    
    current_time = time.time()
    time_since_last_press = current_time - last_enter_press_time
    
    # Check if Enter was pressed twice within the threshold
    if time_since_last_press <= double_press_threshold:
        print("Double Enter detected! Switching tab...")
        pyautogui.hotkey('ctrl', 'tab')  # Switch Chrome tab


        
        last_enter_press_time = 0  # Reset the time after switching tab
    else:
        # Update the time of the most recent Enter press
        last_enter_press_time = current_time
        print("Enter pressed once. Waiting for second press...")

# Set up the listener for Enter key presses
keyboard.on_press_key('enter', on_enter_press)

# Run in the background indefinitely
print("Listening for Enter key presses... Press Enter twice quickly to switch tabs.")
keyboard.wait()  # Keep the script running
