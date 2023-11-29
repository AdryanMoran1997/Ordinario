function validarCURP() {
    var curp = document.getElementById('curp').value.trim().toUpperCase();

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
