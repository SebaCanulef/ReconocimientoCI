function validateForm() {
    var selectedLugar = document.getElementById("UbicacionID").value;
    var options = document.querySelectorAll("#lugar option");
    var isValid = false;

    for (var i = 0; i < options.length; i++) {
        if (options[i].value === selectedLugar) {
            isValid = true;
            break;
        }
    }

    if (!isValid) {
        alert("Por favor seleccione un lugar de la lista proporcionada.");
        return false;
    } else {
        var selectedLugarID = document.querySelector(`#lugar option[value='${selectedLugar}']`).getAttribute('id');
        document.getElementById("nombreLugar").value = selectedLugar;
        document.getElementById("idLugar").value = selectedLugarID;
        return true;
    }
}