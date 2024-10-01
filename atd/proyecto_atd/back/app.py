from flask import Flask, request, render_template, jsonify, send_file
import requests, json
from flask_cors import CORS

app = Flask(__name__, template_folder='../front')
CORS(app)

#PARA TENER UNA BASE DE DATOS DE LOS JUGADORES POR SUS NOMBRES
datos = {}
resp = requests.get('https://api.api-tennis.com/tennis/?method=get_standings&event_type=ATP&APIkey=09034a855e6225a76c07480070e4b0f576e9828fb1c436f53db871484715be28')
data = json.loads(resp.content)
url = 'https://api.api-tennis.com/tennis/'

cont = 0
for jugador in data['result']:
    datos[jugador['player']] = {'player_key': jugador['player_key'], 'country': jugador['country'], 'place': jugador['place'], 'points': jugador['points']}
    cont += 1
    if cont == 1000:
        break


#LAS RUTAS Y METODOS DE LA APLICACION
@app.route('/', methods=['GET'])
def mostrar_plantilla():
    return render_template('index.html')


@app.route('/info/<nombre_jugador>')
def info_jugador(nombre_jugador):
    player_key = str(datos[nombre_jugador]['player_key'])
    parametros = {'method':'get_players', 'player_key': player_key, 'APIkey': '09034a855e6225a76c07480070e4b0f576e9828fb1c436f53db871484715be28'}
    req = requests.get(url, params=parametros)
    resul = req.content
    resul = json.loads(resul)
    resul['result'][0]['ranking'] = datos[nombre_jugador]['place']
    resul['result'][0]['points'] = datos[nombre_jugador]['points']
    return jsonify(resul)

@app.route('/autocompletar/<nombre_jugador>')
def sugerir_jugador(nombre_jugador):
    resul = {'resultado': list()}
    for jugador in datos:
        if nombre_jugador.lower() in jugador.lower():
            resul['resultado'].append(jugador)
    return jsonify(resul)

@app.route('/front/styles.css')
def mandar_css():
    return send_file('../front/styles.css', mimetype='text/css')

@app.route('/front/script.js')
def mandar_js():
    return send_file('../front/script.js', mimetype='application/javascript')

@app.route('/front/images/<nombre_imagen>')
def mandar_imagen(nombre_imagen):
    return send_file(f'../front/images/{nombre_imagen}', mimetype='image/png')

@app.route('/front/fonts/Montserrat/static/<nombre_fuente>')
def mandar_fuente(nombre_fuente):
    return send_file(f'../front/fonts/Montserrat/static/{nombre_fuente}', mimetype='font/ttf')


app.run(host='0.0.0.0', port=5000)
