from flask import Flask, render_template, request, redirect, url_for, jsonify,send_file,flash
import mysql.connector
from config_singleton import ConfigSingleton
from database import cargar_datos_desde_bd
from database import Queries
import os
app = Flask(__name__)

# Utilizar la clase ConfigSingleton para la configuración de la base de datos
config_singleton = ConfigSingleton()
db_config = config_singleton.db_config
#################Menu################################################################
@app.route('/')
def menu_principal():
    return render_template('menu_principal.html')
#################estudiante############################################################
@app.route('/registro_estudiante')
def registro_estudiante():
    municipios = cargar_datos_desde_bd("municipio")
    niveles_curso = cargar_datos_desde_bd("nivelcurso")
    tramites = cargar_datos_desde_bd("tramite")
    return render_template('registro_estudiante.html', municipios=municipios, niveles_curso=niveles_curso, tramites=tramites)

@app.route('/registrar_alumno', methods=['POST'])
def registrar_alumno():
    if request.method == 'POST':
        curp = request.form['curp']
        nombre = request.form['nombre']
        paterno = request.form['paterno']
        materno = request.form['materno']
        telefono = request.form['telefono']
        municipio_id = request.form['municipio']
        nivel_curso_id = request.form['nivel_curso']
        tramite_id = request.form['tramite']

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Obtener el turno actual para el municipio seleccionado
        cursor.execute("SELECT MAX(Turno) FROM solicitud WHERE id_municipio = %s", (municipio_id,))
        max_turno = cursor.fetchone()[0]
        turno = max_turno + 1 if max_turno is not None else 1

        # Resto del código para la inserción del alumno
        cursor.execute("INSERT INTO alumno (Curp, Nombre, Paterno, Materno, Telefono, Municipio_id, NivelCurso_id, Tramite_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (curp, nombre, paterno, materno, telefono, municipio_id, nivel_curso_id, tramite_id))
        connection.commit()

        # Obtener el ID del alumno recién insertado
        cursor.execute("SELECT LAST_INSERT_ID()")
        id_alumno = cursor.fetchone()[0]

        # Resto del código para la generación automática de solicitud
        estatus_id = 1  # Puedes personalizar esto según tus necesidades
        fecha = "2023-11-16"  # Puedes obtener la fecha actual y formatearla

        cursor.execute("INSERT INTO solicitud (Turno, id_alumno, id_estatus, id_tramite, id_municipio, Fecha) VALUES (%s, %s, %s, %s, %s, %s)",
                       (turno, id_alumno, estatus_id, tramite_id, municipio_id, fecha))
        connection.commit()
        
        cursor.close()
        connection.close()

        return redirect(url_for('registro_estudiante'))
##################Busqueda_curp######################################################

def conectar_db():
    connection = mysql.connector.connect(**config_singleton.db_config)
    return connection
@app.route('/')
def b():
    return render_template('b.html')

@app.route('/buscar_nueva', methods=['POST'])
def buscar_tiket():
    curp = request.form['curp']
    
    connection = conectar_db()
    
    if connection is not None and connection.is_connected():
        cursor = connection.cursor(dictionary=True)
        
        query = Queries.buscar_solicitud(curp)
        
        cursor.execute(query, (curp,))
        
        result = cursor.fetchone()
        
        if result:
            # Crear el contenido del archivo de texto
            contenido = f"Solicitud para CURP: {curp}\n\n"
            contenido += f"Turno: {result['Turno']}\n"
            contenido += f"Nombre del Alumno: {result['NombreAlumno']}\n"
            contenido += f"Estatus: {result['estatus']}\n"
            contenido += f"Trámite: {result['Tramite']}\n"
            contenido += f"Municipio: {result['municipio']}\n"
            contenido += f"Fecha: {result['Fecha']}\n"

            # Especifica la ruta completa del archivo
            ruta_archivo = os.path.join(r'C:\Users\adria\Downloads\Ordinario', f"resultado_{curp}.txt")

            # Guardar el contenido en el archivo txt
            with open(ruta_archivo, 'w') as archivo:
                archivo.write(contenido)

            # Cerrar la conexión y el cursor
            cursor.close()
            connection.close()

            # Enviar el archivo al usuario para descargar
            return send_file(ruta_archivo, as_attachment=True)
        else:
            flash("No se encontró ninguna solicitud para la CURP proporcionada.")
            return redirect(url_for('b'))
            
    if connection is not None and connection.is_connected():
        connection.close()
        cursor.close()