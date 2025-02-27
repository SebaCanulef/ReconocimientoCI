function validateForm() {
    var selectedColaborador = document.getElementById("ColaboradorID").value;
    var options = document.querySelectorAll("#trabajador option");
    var isValid = false;

    for (var i = 0; i < options.length; i++) {
        if (options[i].value === selectedColaborador) {
            isValid = true;
            break;
        }
    }

    if (!isValid) {
        alert("Por favor seleccione un colaborador de la lista proporcionada.");
        return false;
    } else {
        var selectedColaboradorID = document.querySelector(`#trabajador option[value='${selectedColaborador}']`).getAttribute('id');
        document.getElementById("nombreColaborador").value = selectedColaborador;
        document.getElementById("idColaborador").value = selectedColaboradorID;
        return true;
    }
}
