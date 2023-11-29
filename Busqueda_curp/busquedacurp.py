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


if __name__ == '__main__':
    app.run(debug=True)