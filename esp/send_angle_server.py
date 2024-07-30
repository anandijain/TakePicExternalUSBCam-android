from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

ESP32_IP = "http://192.168.4.31"  # Replace with the IP address of your ESP32

def set_servo_angles(angle1, angle2):
    if 0 <= angle1 <= 180 and 0 <= angle2 <= 180:
        url = f"{ESP32_IP}/servo?angle1={angle1}&angle2={angle2}"
        print(url)
        response = requests.get(url)
        return response.text
    else:
        return "Invalid angles. Must be between 0 and 180."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        angle1 = int(request.form.get('angle1'))
        angle2 = int(request.form.get('angle2'))
        result = set_servo_angles(angle1, angle2)
        return render_template_string(HTML_TEMPLATE, result=result)
    return render_template_string(HTML_TEMPLATE)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Servo Control</title>
</head>
<body>
    <h1>Set Servo Angles</h1>
    <form method="POST">
        <label for="angle1">Angle 1:</label>
        <input type="number" id="angle1" name="angle1" min="0" max="180" required><br><br>
        <label for="angle2">Angle 2:</label>
        <input type="number" id="angle2" name="angle2" min="0" max="180" required><br><br>
        <button type="submit">Set Angles</button>
    </form>
    {% if result %}
        <h2>Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
