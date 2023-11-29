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

################ Menu Principal ##################################################################
# Función para cargar datos desde la base de datos

    connection = mysql.connector.connect(**db_config)
    return connection
@app.route('/registro')
def registro_login():
    return render_template('Registro_login.html')
# Ruta para agregar un nuevo elemento
@app.route('/agregar', methods=['POST'])
def agregar():
    if request.method == 'POST':
        # Obtener datos del formulario
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        nombre = request.form['nombre']
        paterno = request.form['paterno']
        materno = request.form['materno']
        telefono = request.form['telefono']

        # Conectar a la base de datos
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        try:
            # Ejecutar una consulta para insertar datos en la tabla 'usuario'
            cursor.execute('INSERT INTO usuario (Usuario, Contraseña, Nombre, Paterno, Materno, Telefono) VALUES (%s, %s, %s, %s, %s, %s)',
                           (usuario, contraseña, nombre, paterno, materno, telefono))

            # Confirmar y cerrar la conexión
            conn.commit()
            cursor.close()
            conn.close()

            # Redireccionar a la página principal después de agregar
            return redirect(url_for('registro_login'))

        except Exception as e:
            print(f"Error al insertar en la base de datos: {e}")
            # Manejar el error según sea necesario
            return render_template('error.html', error_message="Error al registrar en la base de datos")
################ Ruta para el formulario de inicio de sesión ######################################
@app.route('/login_form')
def login_form():
    return render_template('login_form.html')

@app.route('/iniciar_sesion', methods=['POST'])
def login():
    username = request.form['usuario']
    password = request.form['contrasena']

    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    query = "SELECT * FROM usuario WHERE Usuario = %s AND Contraseña = %s"
    cursor.execute(query, (username, password))

    if cursor.fetchone():
        # Si las credenciales son válidas, redirige al usuario a la página de dashboard
        return redirect(url_for('menu'))
    else:
            return jsonify({'Error de inicio de secion'}), 401

# Ruta para la página de menú
@app.route('/menu')
def menu():
    # Puedes renderizar el formulario o página que desees para el dashboard
    return render_template('menu.html')


# Creo que es crud municipios
@app.route('/nueva_pagina')
def nueva_pagina():
    # Obtener todos los municipios desde la base de datos
    connection = get_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM municipio")
    municipios = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('nueva_pagina.html', municipios=municipios)
@app.route('/agregar_municipio', methods=['POST'])
def agregar_municipio():
    if request.method == 'POST':
        municipio = request.form['municipio']
        if municipio:
            connection = get_db()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO municipio (municipio) VALUES (%s)", (municipio,))
            connection.commit()
            cursor.close()
            connection.close()
    return redirect('/nueva_pagina')

@app.route('/actualizar_municipio', methods=['POST'])
def actualizar_municipio():
    if request.method == 'POST':
        id_municipio = request.form['id']
        nuevo_municipio = request.form['municipio']
        if nuevo_municipio:
            connection = get_db()
            cursor = connection.cursor()
            cursor.execute("UPDATE municipio SET municipio = %s WHERE idmunicipio = %s", (nuevo_municipio, id_municipio))
            connection.commit()
            cursor.close()
            connection.close()
    return redirect('/nueva_pagina')

@app.route('/eliminar/<string:id_municipio>')
def eliminar_municipio(id_municipio):
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM municipio WHERE idmunicipio = %s", (id_municipio,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect('/nueva_pagina')

def get_db():
    return mysql.connector.connect(**db_config)
@app.route('/')
def index():
    return render_template('Registro_login.html')


@app.route('/agregar_tramite', methods=['POST'])
def agregar_tramite():
    if request.method == 'POST':
        tramite = request.form['tramite']
        if tramite:
            connection = get_db()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO tramite (Tramite) VALUES (%s)", (tramite,))
            connection.commit()
            cursor.close()
            connection.close()
    return redirect('/nueva_pagina_tramite')

@app.route('/actualizar_tramite', methods=['POST'])
def actualizar_tramite():
    if request.method == 'POST':
        id_tramite = request.form['id']
        nuevo_tramite = request.form['tramite']
        if nuevo_tramite:
            connection = get_db()
            cursor = connection.cursor()
            cursor.execute("UPDATE tramite SET Tramite = %s WHERE idTramite = %s", (nuevo_tramite, id_tramite))
            connection.commit()
            cursor.close()
            connection.close()
    return redirect('/nueva_pagina_tramite')

@app.route('/eliminar_tramite/<string:id_tramite>')
def eliminar_tramite(id_tramite):
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tramite WHERE idTramite = %s", (id_tramite,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect('/nueva_pagina_tramite')

@app.route('/nueva_pagina_tramite')
def nueva_pagina_tramite():
    # Obtener todos los trámites desde la base de datos
    connection = get_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tramite")
    tramites = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('nueva_pagina_tramite.html', tramites=tramites)
#######################busqueda curp"""""""""""""""""""""""""""""""
# Ruta para la página de búsqueda por CURP
# Ruta para la página de búsqueda por CURP
@app.route('/busqueda_curp')
def busqueda_curp():
    return render_template('busqueda_curp.html')

# Ruta para el formulario de búsqueda por CURP
@app.route('/busqueda_curp_form', methods=['GET', 'POST'])
def busqueda_curp_form():
    if request.method == 'POST':
        curp = request.form['curp']
        return redirect(url_for('buscar_solicitud', curp=curp))
    return render_template('index.html')


# Ruta para buscar la solicitud por CURP
@app.route('/buscar/<curp>')
def buscar_solicitud(curp):
    # Configurar la conexión a la base de datos
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()

    query_alumno = "SELECT * FROM alumno WHERE Curp = %s"
    cursor.execute(query_alumno, (curp,))
    resultado_alumno = cursor.fetchall()

    if resultado_alumno:
        alumno = resultado_alumno[0]
        id_alumno = alumno[0]

        query_solicitud = "SELECT s.*, e.estatus, t.tramite, m.municipio " \
                          "FROM solicitud s " \
                          "JOIN estatus e ON s.id_estatus = e.idmestatus " \
                          "JOIN tramite t ON s.id_tramite = t.idTramite " \
                          "JOIN municipio m ON s.id_municipio = m.idmunicipio " \
                          "WHERE s.id_alumno = %s"
        cursor.execute(query_solicitud, (id_alumno,))
        resultado_solicitud = cursor.fetchall()

        if resultado_solicitud:
            solicitud = resultado_solicitud[0]
            estatus_values = obtener_valores_estatus(cursor)
            municipio_values = obtener_valores_municipios(cursor)

            return render_template('resultado.html', alumno=alumno, solicitud=solicitud, estatus_values=estatus_values, municipio_values=municipio_values)
        else:
            mensaje = "No se encontraron resultados de solicitud para el CURP proporcionado."
    else:
        mensaje = "No se encontraron resultados para el CURP proporcionado."

    cursor.close()
    db.close()

    return render_template('resultado.html', mensaje=mensaje)

# Ruta para actualizar la información
# Ruta para actualizar la información
@app.route('/actualizar/<id_alumno>', methods=['POST'])
def actualizar_solicitud(id_alumno):
    # Obtener datos del formulario
    nuevo_nombre = request.form['nuevo_nombre']
    nuevo_paterno = request.form['nuevo_paterno']
    nuevo_materno = request.form['nuevo_materno']
    nuevo_telefono = request.form['nuevo_telefono']
    nuevo_turno = request.form['nuevo_turno']
    nueva_fecha = request.form['nueva_fecha']
    nuevo_estatus = request.form['nuevo_estatus']
    nuevo_municipio = request.form['nuevo_municipio']

    # Configurar la conexión a la base de datos
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()

    try:
        # Código de actualización en la base de datos
        query_actualizar_alumno = "UPDATE alumno SET Nombre = %s, Paterno = %s, Materno = %s, Telefono = %s WHERE idAlumno = %s"
        cursor.execute(query_actualizar_alumno, (nuevo_nombre, nuevo_paterno, nuevo_materno, nuevo_telefono, id_alumno))

        query_actualizar_solicitud = "UPDATE solicitud SET Turno = %s, Fecha = %s, id_estatus = (SELECT idmestatus FROM estatus WHERE estatus = %s), id_municipio = (SELECT idmunicipio FROM municipio WHERE municipio = %s) WHERE id_alumno = %s"
        cursor.execute(query_actualizar_solicitud, (nuevo_turno, nueva_fecha, nuevo_estatus, nuevo_municipio, id_alumno))

        # Confirmar la transacción
        db.commit()

        # Devuelve una respuesta JSON indicando que la actualización fue exitosa
        return jsonify({'message': 'La información se ha actualizado correctamente'})

    except Exception as e:
        # Manejar el error según sea necesario
        print(f"Error al actualizar la información: {e}")
        return jsonify({'error': 'Error al actualizar la información'})

    finally:
        # Cerrar la conexión a la base de datos
        cursor.close()
        db.close()
###########Eliminar#############################
@app.route('/eliminar/<id_alumno>', methods=['GET', 'POST'])
def eliminar_solicitud(id_alumno):
    if request.method == 'POST':
        # Manejar la lógica de eliminación aquí
        try:
            # Configurar la conexión a la base de datos
            db = mysql.connector.connect(**db_config)
            cursor = db.cursor()

            # Código de eliminación en la base de datos
            query_eliminar_solicitud = "DELETE FROM solicitud WHERE id_alumno = %s"
            cursor.execute(query_eliminar_solicitud, (id_alumno,))

            # Confirmar la transacción
            db.commit()

            # Devuelve una respuesta JSON indicando que la eliminación fue exitosa
            return jsonify({'message': 'La solicitud se ha eliminado correctamente'})

        except Exception as e:
            # Manejar el error según sea necesario
            print(f"Error al eliminar la solicitud: {e}")
            return jsonify({'error': 'Error al eliminar la solicitud'})

        finally:
            # Cerrar la conexión a la base de datos
            cursor.close()
            db.close()

    # Si la solicitud no es POST, redirige o renderiza según sea necesario
    return redirect(url_for('alguna_otra_ruta'))
# Ruta para eliminar la información

# Funciones auxiliares
def obtener_valores_estatus(cursor):
    query_estatus = "SELECT estatus FROM estatus"
    cursor.execute(query_estatus)
    resultado_estatus = cursor.fetchall()
    return [estatus[0] for estatus in resultado_estatus]

def obtener_valores_municipios(cursor):
    query_municipios = "SELECT municipio FROM municipio"
    cursor.execute(query_municipios)
    resultado_municipios = cursor.fetchall()
    return [municipio[0] for municipio in resultado_municipios]
################dashboard####################
conn = mysql.connector.connect(**db_config)
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
@app.route('/get_data')
def get_data():
    try:
        # Crea un cursor para ejecutar consultas SQL
        cursor = conn.cursor(dictionary=True)

        # Consulta SQL para obtener el número de solicitudes "Resuelto" por municipio
        query = """
            SELECT m.municipio, COUNT(s.idSolicitud) as resuelto_count
            FROM municipio m
            LEFT JOIN solicitud s ON m.idmunicipio = s.id_municipio
            WHERE s.id_estatus = 1  # Ajusta el ID de estatus según tu base de datos
            GROUP BY m.idmunicipio;
        """
        cursor.execute(query)

        # Obtiene los resultados de la consulta
        data = cursor.fetchall()

        return jsonify(data)
    except Exception as e:
        print(f"Error al obtener datos de la base de datos: {e}")
        return jsonify([])  # Devuelve una lista vacía en caso de error
    finally:
        # Cierra el cursor
        cursor.close()
@app.route('/dashboard_pendiente.html')
def dashboard_pendiente():
    return render_template('dashboard_pendiente.html')
@app.route('/get_data_pendiente')
def get_data_pendiente():
    try:
        # Crea un cursor para ejecutar consultas SQL
        cursor = conn.cursor(dictionary=True)

        # Consulta SQL para obtener el número de solicitudes "Pendiente" por municipio
        query = """
            SELECT m.municipio, COUNT(s.idSolicitud) as pendiente_count
            FROM municipio m
            LEFT JOIN solicitud s ON m.idmunicipio = s.id_municipio
            WHERE s.id_estatus = 2  # Ajusta el ID de estatus "Pendiente" según tu base de datos
            GROUP BY m.idmunicipio;
        """
        cursor.execute(query)

        # Obtiene los resultados de la consulta
        data = cursor.fetchall()

        return jsonify(data)
    except Exception as e:
        print(f"Error al obtener datos de la base de datos: {e}")
        return jsonify([])  # Devuelve una lista vacía en caso de error
    finally:
        # Cierra el cursor
        cursor.close()
# Función para obtener datos de la solicitud por CURP
# Ruta para buscar y descargar la información de un alumno por su CURP
@app.route('/buscar_alumno', methods=['GET', 'POST'])
def buscar_alumno():
    if request.method == 'POST':
        curp = request.form['curp']

        # Conecta a la base de datos
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        # Consulta SQL para obtener la información del alumno por su CURP
        query = "SELECT * FROM alumno WHERE Curp = %s"
        cursor.execute(query, (curp,))
        alumno = cursor.fetchone()

        # Cierra la conexión a la base de datos después de leer los resultados
        cursor.close()
        connection.close()

        if alumno:
            # Si se encuentra el alumno, crea un archivo de texto con su información
            file_content = f"Nombre: {alumno['Nombre']}\n"
            file_content += f"Paterno: {alumno['Paterno']}\n"
            file_content += f"Materno: {alumno['Materno']}\n"
            file_content += f"Teléfono: {alumno['Telefono']}\n"
            file_content += f"Municipio: {alumno['Municipio_id']}\n"
            file_content += f"Nivel de Curso: {alumno['NivelCurso_id']}\n"
            file_content += f"Trámite: {alumno['Tramite_id']}\n"

            # Guarda el archivo en el servidor
            file_path = f"alumno_{curp}.txt"
            with open(file_path, 'w') as file:
                file.write(file_content)

            # Descarga el archivo
            return send_file(file_path, as_attachment=True)

        else:
            # Si no se encuentra el alumno, muestra un mensaje de error
            error_message = "No se encontró un alumno con ese CURP."
            return render_template('buscar_alumno.html', error_message=error_message)

    return render_template('buscar_alumno.html')
if __name__ == '__main__':
    app.run(debug=True)
