document.addEventListener('DOMContentLoaded', function() {
    const check = document.querySelector('#id_tiene_beneficio');
    const campo = document.querySelector('#id_cual_beneficio');

    function toggleField() {
        if (check.checked) {
            campo.removeAttribute('disabled');
            campo.parentElement.style.opacity = '1';
        } else {
            campo.setAttribute('disabled', 'true');
            campo.parentElement.style.opacity = '0.6';
        }
    }

    // Ejecutar al cargar
    toggleField();

    // Escuchar cambios
    check.addEventListener('change', toggleField);
});
