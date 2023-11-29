
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