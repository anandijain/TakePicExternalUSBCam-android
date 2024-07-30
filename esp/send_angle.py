# %%
import requests

ESP32_IP = "http://192.168.4.31"  # Replace with the IP address of your ESP32

def set_servo_angles(angle1, angle2):
    if 0 <= angle1 <= 180 and 0 <= angle2 <= 180:
        url = f"{ESP32_IP}/servo?angle1={angle1}&angle2={angle2}"
        print(url)
        response = requests.get(url)
            
        print(response.text)
    else:
        print("Invalid angles. Must be between 0 and 180.")

# Example usage
set_servo_angles(90, 45)  # Set servo1 to 90 degrees and servo2 to 45 degrees

# %% 
# Example usage
set_servo_angles(0, 170)

# %%
set_servo_angles(0, 10)

# %%
set_servo_angles(180, 100)

# %%
set_servo_angles(0, 0)

# %%

set_servo_angles(0, 45)
set_servo_angles(0, 45)
# %%

set_servo_angles(0, 65)
# %%

set_servo_angle(65)
# %%

set_servo_angles(90, 90)
# %%
set_servo_angles(80, 80)

# %%
set_servo_angles(70, 70)
# %%
set_servo_angles(20, 40)
# %%

set_servo_angles(0, 40)
# %%
import time
while True:
    set_servo_angles(0, 0)
    time.sleep(1)
    set_servo_angles(0, 180)
    time.sleep(1)
 # %%
