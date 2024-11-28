import sqlite3
import base64

def convertir_imagen_base64(ruta_imagen):
    with open(ruta_imagen, "rb") as imagen_file:
        return base64.b64encode(imagen_file.read()).decode('utf-8')

def crear_base_datos():
    conexion = sqlite3.connect('personas.db')
    cursor = conexion.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS personas (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nombre TEXT NOT NULL,
                      correo TEXT NOT NULL,
                      edad INTEGER NOT NULL,
                      imagen TEXT NOT NULL)''')

    imagen_base64 = convertir_imagen_base64('/home/felipe-trivi-o/Descargas/felipe.jpg')
    cursor.execute('''INSERT INTO personas (nombre, correo, edad, imagen)
                      VALUES (?, ?, ?, ?)''', ('Felipe Triviño', 'felipe@gmail.com', 20, imagen_base64))

    conexion.commit()
    conexion.close()

if __name__ == '__main__':
    crear_base_datos()
    print("Base de datos creada y registro insertado")