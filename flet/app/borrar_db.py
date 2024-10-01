import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect('./app_database.db')
cursor = conexion.cursor()

# Obtener los nombres de todas las tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()

# Eliminar cada tabla
for tabla in tablas:
    nombre_tabla = tabla[0]
    cursor.execute(f"DROP TABLE IF EXISTS {nombre_tabla}")
    print(f"Tabla {nombre_tabla} eliminada.")

# Confirmar los cambios
conexion.commit()
conexion.close()
