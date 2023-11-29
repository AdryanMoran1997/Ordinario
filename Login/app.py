##################Login################################################################
# Ruta principal
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
################ Menu Principal ##################################################################
# Función para cargar datos desde la base de datos

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
