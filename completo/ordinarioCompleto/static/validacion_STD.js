function validarFormulario() {
    if (!validarCURP()) {
        alert('Ingrese un CURP válido.');
        return false;
    }

    if (!validarTelefono()) {
        alert('Ingrese un número de teléfono válido.');
        return false;
    }

    return true;
}
function validarCURP() {
    var curp = document.getElementById('curp').value.trim();

    // Validar la longitud
    if (curp.length !== 18) {
        alert('La CURP debe tener 18 caracteres.');
        return false;
    }

    // Validar el formato de la CURP
    var curpRegex = /^[A-Z]{4}[0-9]{6}[HM][A-Z]{5}[0-9]{2}$/;
    if (!curpRegex.test(curp)) {
        alert('Formato de CURP no válido.');
        return false;
    }

    return true;
}



function validarTelefono() {
    var telefono = document.getElementById('telefono').value;
    // Elimina espacios y guiones del número de teléfono
    telefono = telefono.replace(/\s+/g, '').replace(/-/g, '');
    // Verifica si el número de teléfono tiene 10 dígitos
    return /^\d{10}$/.test(telefono);
}
