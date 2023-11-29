Ruta para la página de menú
@app.route('/menu')
def menu():
    # Puedes renderizar el formulario o página que desees para el dashboard
    return render_template('menu.html')

@app.route('/')
def menu_principal():
    return render_template('menu_principal.html')