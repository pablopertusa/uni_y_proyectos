function buscarAutocompletado() {
    var input = document.getElementById('searchInput');
    var autocompleteContainer = document.getElementById('autocomplete');
    var inputValue = input.value;

    // Limpiar la lista de autocompletado
    autocompleteContainer.innerHTML = '';

    // Realizar la solicitud al servidor solo si la entrada tiene al menos 1 caracteres
    if (inputValue.length >= 1) {

        // Realizar la solicitud al servidor para obtener autocompletado
        fetch('http://127.0.0.1:5001/autocompletar/' + encodeURIComponent(inputValue))
            .then(response => response.json())
            .then(data => {

                // Verificar si 'resultado' está presente y es un array
                if ('resultado' in data && Array.isArray(data.resultado)) {
                    var opciones = data.resultado;

                    // Mostrar los resultados del autocompletado
                    opciones.forEach(opcion => {
                        var autocompleteItem = document.createElement('div');
                        autocompleteItem.className = 'autocomplete-item';
                        autocompleteItem.textContent = opcion;

                        // Asignar el clic del usuario para seleccionar el elemento
                        autocompleteItem.onclick = function() {
                            input.value = opcion;

                            // Limpiar la lista de autocompletado
                            autocompleteContainer.innerHTML = ''; 
                        };
                        autocompleteContainer.appendChild(autocompleteItem);
                    });
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
}

function buscarAccion() {
    var input = document.getElementById('searchInput');
    var inputValue = input.value;

    if (inputValue == 'Añadir alumno'){
        // Crear una instancia de XMLHttpRequest
        var xhr = new XMLHttpRequest();

        // Configurar la solicitud al servidor
        xhr.open('GET', 'http://127.0.0.1:5001/opciones/nuevo_alumno', true);

        // Manejar el evento onload (cuando la solicitud se completa)
        xhr.onload = function () {
            // Verificar si la solicitud fue exitosa (código de estado 200)
            if (xhr.status === 200) {
                // Obtener el contenido HTML de la respuesta
                var nuevoHTML = xhr.responseText;

                // Crear un nuevo documento HTML usando el contenido obtenido
                var nuevoDocumento = new DOMParser().parseFromString(nuevoHTML, 'text/html');

                // Abrir el nuevo documento en una ventana o pestaña
                var nuevaVentana = window.open('', '_blank');
                nuevaVentana.document.write(nuevoDocumento.documentElement.outerHTML);
            } else {
                console.error('Error al cargar el HTML');
            }
        };

        // Enviar la solicitud
        xhr.send();
    }

    if (inputValue == 'Añadir trabajador'){
        // Crear una instancia de XMLHttpRequest
        var xhr = new XMLHttpRequest();

        // Configurar la solicitud al servidor
        xhr.open('GET', 'http://127.0.0.1:5001/opciones/nuevo_trabajador', true);

        // Manejar el evento onload (cuando la solicitud se completa)
        xhr.onload = function () {
            // Verificar si la solicitud fue exitosa (código de estado 200)
            if (xhr.status === 200) {
                // Obtener el contenido HTML de la respuesta
                var nuevoHTML = xhr.responseText;

                // Crear un nuevo documento HTML usando el contenido obtenido
                var nuevoDocumento = new DOMParser().parseFromString(nuevoHTML, 'text/html');

                // Abrir el nuevo documento en una ventana o pestaña
                var nuevaVentana = window.open('', '_blank');
                nuevaVentana.document.write(nuevoDocumento.documentElement.outerHTML);
            } else {
                console.error('Error al cargar el HTML');
            }
        };

        // Enviar la solicitud
        xhr.send();
    }

    if (inputValue == 'Registrar asistencia'){
        // Crear una instancia de XMLHttpRequest
        var xhr = new XMLHttpRequest();

        // Configurar la solicitud al servidor
        xhr.open('GET', 'http://127.0.0.1:5001/opciones/registrar_asistencia', true);

        // Manejar el evento onload (cuando la solicitud se completa)
        xhr.onload = function () {
            // Verificar si la solicitud fue exitosa (código de estado 200)
            if (xhr.status === 200) {
                // Obtener el contenido HTML de la respuesta
                var nuevoHTML = xhr.responseText;

                // Crear un nuevo documento HTML usando el contenido obtenido
                var nuevoDocumento = new DOMParser().parseFromString(nuevoHTML, 'text/html');

                // Abrir el nuevo documento en una ventana o pestaña
                var nuevaVentana = window.open('', '_blank');
                nuevaVentana.document.write(nuevoDocumento.documentElement.outerHTML);
            } else {
                console.error('Error al cargar el HTML');
            }
        };

        // Enviar la solicitud
        xhr.send();
    }

    if (inputValue == 'Consultar alumno'){
        // Crear una instancia de XMLHttpRequest
        var xhr = new XMLHttpRequest();

        // Configurar la solicitud al servidor
        xhr.open('GET', 'http://127.0.0.1:5001/opciones/consultar_alumno', true);

        // Manejar el evento onload (cuando la solicitud se completa)
        xhr.onload = function () {
            // Verificar si la solicitud fue exitosa (código de estado 200)
            if (xhr.status === 200) {
                // Obtener el contenido HTML de la respuesta
                var nuevoHTML = xhr.responseText;

                // Crear un nuevo documento HTML usando el contenido obtenido
                var nuevoDocumento = new DOMParser().parseFromString(nuevoHTML, 'text/html');

                // Abrir el nuevo documento en una ventana o pestaña
                var nuevaVentana = window.open('', '_blank');
                nuevaVentana.document.write(nuevoDocumento.documentElement.outerHTML);
            } else {
                console.error('Error al cargar el HTML');
            }
        };

        // Enviar la solicitud
        xhr.send();
    }


    if (inputValue == 'Crear Excel con datos'){
        fetch('http://127.0.0.1:5001/opciones/crear_excel_con_datos')
            .then(response => response.json())
            .then(data => {
                if (data.respuesta == 'Datos creados correctamente') {
                    var enlace = document.createElement('a');
                    enlace.href = 'http://127.0.0.1:5001/datos';
                    enlace.download = 'datos_exportados.xlsx';
                    enlace.click();
                    alert(data.respuesta);
                }
                else {
                    alert(data.respuesta);
                }
            })
            .catch(error => {
                console.error('Error:', error);
        });
    }
}