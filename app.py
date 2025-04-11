from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "55f2e4f2ebd376e3a01ac6fcb7b72e27"

@app.route('/', methods=['GET', 'POST'])
def home():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=55f2e4f2ebd376e3a01ac6fcb7b72e27&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity']
            }
        else:
            weather = 'error'
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
