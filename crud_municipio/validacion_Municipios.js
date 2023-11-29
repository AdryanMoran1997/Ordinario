// validacion_Municipios.js

function validarFormulario() {
    var tramiteInput = document.getElementById('tramite');

    // Verificar si el campo está vacío
    if (tramiteInput.value.trim() === '') {
        alert('Por favor, ingrese un trámite');
        return false; // Detener el envío del formulario
    }

    // Puedes agregar más validaciones si es necesario

    return true; // Permitir el envío del formulario
}
