document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        var usuarioInput = document.getElementById('usuario');
        var contraseñaInput = document.getElementById('contraseña');
        var telefonoInput = document.getElementById('telefono');

        // Validación del usuario
        if (usuarioInput.value.length <= 6) {
            alert('El usuario debe tener más de 6 caracteres.');
            event.preventDefault(); // Evitar que el formulario se envíe
            return;
        }

        // Validación de la contraseña
        if (contraseñaInput.value.length <= 6) {
            alert('La contraseña no puede ser corta.');
            event.preventDefault();
            return;
        }

        // Validación del teléfono
        var telefonoRegex = /^\d{10}$/;
        if (!telefonoRegex.test(telefonoInput.value)) {
            alert('El teléfono debe tener 10 números.');
            event.preventDefault();
            return;
        }

        // Si todas las validaciones pasan, puedes enviar el formulario
    });
});
