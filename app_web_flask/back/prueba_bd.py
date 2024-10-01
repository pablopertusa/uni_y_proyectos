import sqlite3 as sq

# Conectar a la base de datos (o crearla si no existe)
conn = sq.connect('/Users/pablo/Desktop/segundo/aplicacion/db_browser/base_datos_prueba.db')

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Crear una nueva tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS alumnos (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        telefono integer
    )
''')

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()