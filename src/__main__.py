from flask import Flask
from flask_cors import CORS
import requests

from src import env

app = Flask(__name__)
CORS(app)


@app.route('/mesto/<param>')
def get_api_key(param):

    # Get response from request
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={param}&units=metric&appid={env.API_KEY}')

    # Transform response into json
    body = response.json()

    # Return body and status code in response
    return body, response.status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=env.PORT, debug=False)
