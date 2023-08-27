import time
import pyautogui

# Sleep for a few seconds to give you time to focus on the input field
time.sleep(5)

# Simulate clicking on the first entry field
pyautogui.click(x=your_x_coordinate, y=your_y_coordinate)

# Type the food order using the keyboard
pyautogui.write("Your food order")

# Simulate pressing the Enter key to submit the order
pyautogui.press("enter")

# Calculate the coordinates of the next "bar" or entry
next_entry_x = your_next_x_coordinate
next_entry_y = your_next_y_coordinate

# Simulate clicking on the next entry
pyautogui.click(x=next_entry_x, y=next_entry_y)
