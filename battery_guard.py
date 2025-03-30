# ===============================
# Battery Guard - Auto Battery Monitor
# ===============================
# Author: jmon360
# Date: 2025
# Project Type: Python Automation Script
# Platform: Windows 10/11

"""
Description:
Battery Guard is a lightweight Python-based system monitor that checks battery health in real-time.
It sends alerts via system pop-ups when the battery is low, charging, or fully charged. This script helps
prevent unnecessary wear on your battery and promotes healthy charging cycles — all without needing
a heavy app or GUI.

Detailed Pseudocode Overview:
1. IMPORT required libraries (psutil, time, os).
2. DEFINE a function `check_battery` to perform the following battery checks:
    - Retrieve battery information using the `psutil.sensors_battery()` function.
    - IF no battery is detected:
        - Print a warning about missing hardware.
        - Stop further execution by returning from the function.
    - Extract and store details:
        a) Percentage of battery left.
        b) Whether the computer is currently plugged in (charging or not).
        c) Estimated time left for the battery to discharge (in seconds and minutes).
    - Display a detailed battery status in the console log:
        Format: `Battery: [percent]% | Plugged in: [True/False] | Time left: [minutes] mins`.
3. IMPLEMENT conditional checks to assess battery state:
    - IF unplugged (not charging) AND battery percentage is less than 20%:
        a) Use `os.system` to send a pop-up alert to the user, prompting them to plug in.
        b) Alert message: "Low battery! Plug in now — only [percent]% left."
    - IF plugged in (charging):
        a) Display a message in the console:
            i) If battery is below 95%: "Charging — keep it plugged in."
            ii) If battery is at 95% or above: "Fully charged — unplug to save battery cycles."
4. DEFINE the `main` loop in the script:
    - Use an infinite loop (`while True`).
    - Call the `check_battery` function repeatedly every 5 minutes.
    - Use `time.sleep(300)` to insert the wait time.

Key Goals:
- Ensure that the system monitors battery conditions indefinitely with controlled intervals.
- Reduce unnecessary battery wear by prompting the user to act based on specific battery conditions.
"""

# ===============================
# Import Libraries
# ===============================
import psutil  # For system and battery information
import time  # For interval-based execution
import os  # For sending system alerts


# ===============================
# Battery Check Function
# ===============================
def check_battery():
    # STEP 1: Retrieve battery info
    battery = psutil.sensors_battery()

    # STEP 2: Check if the battery is detected
    if battery is None:
        # Print warning and exit this iteration if no battery is found
        print("Warning: No battery detected — check your hardware!")
        return

    # STEP 3: Extract specific battery details
    percent = battery.percent  # The current percentage of battery remaining
    plugged = battery.power_plugged  # Boolean: True if plugged in, False otherwise
    secs_left = battery.secsleft  # Estimated seconds left to charge/discharge

    # STEP 4: Convert estimated time (seconds) into minutes (if available)
    mins_left = secs_left // 60 if secs_left > 0 else "Unknown"

    # STEP 5: Print battery status in the console
    status = f"Battery: {percent}% | Plugged in: {plugged} | Time left: {mins_left} mins"
    print(status)

    # STEP 6: Trigger alerts or messages based on battery conditions
    if not plugged and percent < 20:  # Low battery and NOT charging
        os.system(f'msg * "Low battery! Plug in now — only {percent}% left."')
    elif plugged and percent < 95:  # Charging, but not yet fully charged
        print("Charging — keep it plugged in.")
    elif plugged and percent >= 95:  # Fully charged while still plugged in
        print("Fully charged — unplug to save battery cycles.")


# ===============================
# Main Loop
# ===============================
if __name__ == "__main__":
    # Infinite loop to continuously monitor the battery every 5 minutes
    while True:
        # Call the battery check function
        check_battery()
        # Wait for 5 minutes before repeating the check
        time.sleep(300)

