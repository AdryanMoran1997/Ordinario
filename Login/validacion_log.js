document.addEventListener('DOMContentLoaded', function () {
    var form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        var usuario = document.querySelector('input[name="usuario"]').value;
        var contrasena = document.querySelector('input[name="contrasena"]').value;

        if (usuario.trim() === '' || contrasena.trim() === '') {
            alert('Por favor, completa todos los campos.');
            event.preventDefault(); // Evita que el formulario se envíe si hay campos vacíos
        }
    });
});
