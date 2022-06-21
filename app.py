# Importation des packages nécessaires
import urllib
import json
from flask import Flask, render_template, request, abort, Response

# Initialisation de notre application Flask
app = Flask(__name__)

########################################################################################################################
# Routage de l'url vers la fonction correspondante
@app.route('/', methods=['GET', 'POST'])
def get_weather():
    city = request.args.get('city')
    if city is None:
        abort(400, 'Missing argument city')

    data = {}
    data['q'] = request.args.get('city')
    data['appid'] = '13ca210a7281f48b9e44697ae40b3228'
    data['units'] = 'metric'
    url_values = urllib.parse.urlencode(data)
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    full_url = url + '?' + url_values
    data = urllib.request.urlopen(full_url)
    resp = Response(data)
    resp.status_code = 200
    return render_template('index.html', title='Weather App', data=json.loads(data.read().decode('utf8')))

########################################################################################################################
### Lancement de l'application lorsqu'on run le code
if __name__ == '__main__':
    app.run()
