from flask import Flask, render_template, send_file, jsonify, request
from flask_cors import CORS
import webbrowser
import sqlite3
import pandas as pd

app = Flask(__name__, template_folder='../front')
CORS(app)

posibles_opciones = ['Registrar asistencia', 'Añadir trabajador', 'Añadir alumno', 'Crear Excel con datos',
'Consultar alumno']



#LAS RUTAS Y METODOS DE LA APLICACION
@app.route('/', methods=['GET'])
def mostrar_plantilla():
    return render_template('index.html')

@app.route('/autocompletar/<opcion>')
def mandar_opcion(opcion):
    respuesta = {'resultado': []}
    for i in posibles_opciones:
        if opcion.lower() in i.lower():
            respuesta['resultado'].append(i)
    return jsonify(respuesta)


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

#MANDAR DIFERENTES HTML DEPEDIENTO DE LA OPCION QUE ELIJA
@app.route('/opciones/nuevo_alumno')
def mandar_HTML_nuevo_alumno():
    return render_template('nuevo_alumno.html')

@app.route('/opciones/nuevo_trabajador')
def mandar_HTML_nuevo_trabajador():
    return render_template('nuevo_trabajador.html')

@app.route('/opciones/registrar_asistencia')
def mandar_HTML_registrar_asistencia():
    return render_template('registrar_asistencia.html')

@app.route('/opciones/consultar_alumno')
def mandar_HTML_consultar_alumno():
    return render_template('consultar_alumno.html')

@app.route('/opciones/crear_excel_con_datos')
def crear_excel():
    try:
        conexion = sqlite3.connect(basedatos)
        cursor = conexion.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = cursor.fetchall()

        with pd.ExcelWriter('../datos/datos_exportados.xlsx') as escritor_excel:
            for tabla in tablas:
                nombre_tabla = tabla[0]
                datos_tabla = pd.read_sql_query(f"SELECT * FROM {nombre_tabla}", conexion)
                datos_tabla.to_excel(escritor_excel, sheet_name=nombre_tabla, index=False)

        conexion.close()

        return jsonify({'respuesta': 'Datos creados correctamente'})
    
    except Exception as e:
        print(e)
        return jsonify({'respuesta': 'Ha ocurrido un problema'})
    
@app.route('/datos')
def mandar_excel():
    return send_file('../datos/datos_exportados.xlsx', as_attachment=True)


#CONEXION BASE DE DATOS
basedatos = '../db_browser/base_datos_prueba.db'



#NUEVOS ALUMNOS Y TRABAJADORES
@app.route('/alumno/procesar_formulario', methods=['POST'])
def nuevo_alumno():
    try:
        nombre = request.form.get('nombre')
        fecha_nacimiento = request.form.get('fechaNacimiento')
        sexo = request.form.get('sexo')
        conexion = sqlite3.connect(basedatos)
        cursor = conexion.cursor()
        cursor.execute('insert into alumnos values (?,?,?)', (nombre, fecha_nacimiento, sexo))
        conexion.commit()
        return '', 204

    except Exception as e:
        print(f"Error al procesar el formulario: {str(e)}")
        return render_template('existe_en_base_datos.html', persona='alumno')
    
@app.route('/procesar/trabajador', methods=['POST'])
def nuevo_trabajador():
    try:
        nombre = request.form.get('nombre')
        fecha_nacimiento = request.form.get('fechaNacimiento')
        sexo = request.form.get('sexo')
        conexion = sqlite3.connect(basedatos)
        cursor = conexion.cursor()
        cursor.execute('insert into alumnos values (?,?,?)', (nombre, fecha_nacimiento, sexo))
        conexion.commit()
        return '', 204

    except Exception as e:
        print(f"Error al procesar el formulario: {str(e)}")
        return render_template('existe_en_base_datos.html', persona='trabajador')
    

@app.route('/buscar/alumno/<entrada>')
def buscar_alumno(entrada):
    conexion = sqlite3.connect(basedatos)
    cursor = conexion.cursor()
    cursor.execute('select nombre from alumnos where nombre like ?', ('%'+entrada+'%',))
    consulta = cursor.fetchall()
    respuesta = {'respuesta': consulta}
    return jsonify(respuesta)

@app.route('/registrar', methods=['POST'])
def registrar_alumno():
    nombre = request.json['nombre']
    fecha = request.json['fecha']
    conexion = sqlite3.connect(basedatos)
    cursor = conexion.cursor()
    cursor.execute('select count(*) from asistencia_alumnos where nombre = ? and fecha_asistencia = ?',  (nombre, fecha))
    consulta = cursor.fetchall()
    n = consulta[0][0] # 1 si ya esta registrado y 0 si no lo está
    if n == 0:
        cursor.execute('insert into asistencia_alumnos values (?,?)', (nombre, fecha))
        conexion.commit()
        return jsonify({'respuesta': 'Asistencia registrada'})
    else:
        return jsonify({'respuesta': 'Asistencia ya registrada'})
    

@app.route('/consultar/<nombre_alumno>')
def enviar_consulta_alumno(nombre_alumno):
    conexion = sqlite3.connect(basedatos)
    cursor = conexion.cursor()
    cursor.execute('select * from alumnos where nombre = ?', (nombre_alumno,))
    info = cursor.fetchall()
    respuesta = {}
    for nombre, fecha_nacimiento, sexo in info:
        respuesta['nombre'] = nombre
        respuesta['fecha_nacimiento'] = fecha_nacimiento
        respuesta['sexo'] = sexo

    respuesta['asistencias'] = []
    cursor.execute('select fecha_asistencia from asistencia_alumnos where nombre = ?', (nombre_alumno,))
    asistencias = cursor.fetchall()
    for asistencia in asistencias:
        respuesta['asistencias'].append(asistencia[0])
    return jsonify(respuesta)



webbrowser.open('http://127.0.0.1:5001')
app.run(host='127.0.0.1', port=5001)

