# %%
import requests

ESP32_IP = "http://192.168.4.31"  # Replace with the IP address of your ESP32

def toggle_led(state):
    if state == "on":
        response = requests.get(f"{ESP32_IP}/led/on")
        print(response.text)
    elif state == "off":
        response = requests.get(f"{ESP32_IP}/led/off")
        print(response.text)
# %%
# Example usage
toggle_led("on")

# %%

# Add a delay if needed
toggle_led("off")

# %%
