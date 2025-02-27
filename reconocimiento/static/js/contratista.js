function validateForm() {
    var selectedEmpresa = document.getElementById("EmpID").value;
    var options = document.querySelectorAll("#empresas option");
    var isValid = false;

    for (var i = 0; i < options.length; i++) {
        if (options[i].value === selectedEmpresa) {
            isValid = true;
            break;
        }
    }

    if (!isValid) {
        alert("Por favor seleccione una empresa de la lista proporcionada.");
        return false;
    } else {
        var selectedEmpresaID = document.querySelector(`#empresas option[value='${selectedEmpresa}']`).getAttribute('id');
        document.getElementById("nombreEmpresa").value = selectedEmpresa;
        document.getElementById("idEmpresa").value = selectedEmpresaID;

        // Capturar la observación
        var observacion = document.getElementById('observacion').value;
        document.getElementById("observacionHidden").value = observacion;

        return true;
    }
}

var observacionField = document.getElementById('observacion');
var maxLength = 200;

observacionField.addEventListener('input', function () {
    if (observacionField.value.length > maxLength) {
        observacionField.value = observacionField.value.slice(0, maxLength);
    }
});