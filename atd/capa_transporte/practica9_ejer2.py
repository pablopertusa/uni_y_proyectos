from flask import Flask, jsonify, request

app = Flask(__name__)

libros = [
  {'titulo':    'Computer networking : a top-down approach',
   'autores':   ['Kurose, James F.', 'Ross, Keith W.'],
   'edicion':   7,
   'editorial': 'Pearson',
   'anyo':      2017},
  {'titulo':    'Learning Python network programming',
   'autores':   ['Faruque Sarker, Dr. M. O.', 'Washington, S.'],
   'edicion':   2,
   'editorial': 'Packt Publising',
   'anyo':      2015},
  {'titulo':    'Practical Web Scraping for Data Science',
   'autores':   ['vanden Broucke, Seppe', 'Baesens, Bart'],
   'edicion':   1,
   'editorial': 'Apress',
   'anyo':      2018}
]

id_nueva = 0
for libro in libros:
    libro['id'] = id_nueva
    id_nueva += 1

@app.route("/libros", methods=["GET"])
def getLibros():
    return jsonify(libros)

@app.route("/libro/<id>", methods=["GET"])
def getLibro(id):
    id = int(id)
    for libro in libros:
        if libro['id'] == id:
            break
    return jsonify(libro)

@app.route('/libro', methods=['POST'])
def postLibro():
    titulo     = request.json['titulo']
    autores    = request.json['autores']
    edicion    = request.json['edicion']
    editorial  = request.json['editorial']
    anyo       = request.json['anyo']

    nuevoLibro = {'titulo':    titulo,
                  'autores':   autores,
                  'edicion':   edicion,
                  'editorial': editorial,
                  'anyo':      anyo
                 }
    libros.append(nuevoLibro)

    return jsonify(nuevoLibro)

@app.route('/libro/<id>', methods=['PATCH'])
def patchLibro(id):
    id = int(id)
    encontrado = False
    for libro in libros:
        if libro['id'] == id:
            libroModificado = libro
            encontrado = True
    if encontrado:
        for atributo in request.json:
            if atributo in libroModificado:
                libroModificado[atributo] = request.json[atributo]
    
        return jsonify(libroModificado)
    return None

@app.route('/libro/<id>', methods=['DELETE'])
def deleteLibro(id):
    cont = 0
    id = int(id)
    for libro in libros:
        if libro['id'] == id:
            del libros[cont]
            return jsonify({"mensaje": f"Libro con ID {id} eliminado correctamente"}), 204
        cont += 1
    return jsonify({"mensaje": f"Libro con ID {id} no encontraddo"}), 404




if __name__ == '__main__':
    app.run(port=8080)