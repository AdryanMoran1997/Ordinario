

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
