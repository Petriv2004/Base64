#!/usr/bin/python3

import cgi
import json
import sqlite3

def consultar_persona_por_id(persona_id):
    conexion = sqlite3.connect('/var/www/html/base64/personas.db')
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM personas WHERE id=?", (persona_id,))
    resultado = cursor.fetchone()

    conexion.close()
    if resultado:
        id_persona, nombre, correo, edad, imagen_base64 = resultado
        return {'id': id_persona, 'nombre': nombre, 'correo': correo, 'edad': edad, 'imagen': imagen_base64}
    else:
        return None

print("Content-Type: application/json")
print()

form = cgi.FieldStorage()
persona_id = form.getvalue("id")

if persona_id:
    persona = consultar_persona_por_id(int(persona_id))
    if persona:
        print(json.dumps(persona))
    else:
        print(json.dumps(None))
else:
    print(json.dumps({"error": "No se ha proporcionado un ID"}))
