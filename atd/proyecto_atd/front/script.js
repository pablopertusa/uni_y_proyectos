function buscarAutocompletado() {
    var input = document.getElementById('searchInput');
    var autocompleteContainer = document.getElementById('autocomplete');
    var inputValue = input.value;

    // Limpiar la lista de autocompletado
    autocompleteContainer.innerHTML = '';

    // Realizar la solicitud al servidor solo si la entrada tiene al menos 1 caracteres
    if (inputValue.length >= 1) {

        // Realizar la solicitud al servidor para obtener autocompletado
        fetch('http://127.0.0.1:5000/autocompletar/' + encodeURIComponent(inputValue))
            .then(response => response.json())
            .then(data => {

                // Verificar si 'resultado' está presente y es un array
                if ('resultado' in data && Array.isArray(data.resultado)) {
                    var jugadoresEncontrados = data.resultado;

                    // Mostrar los resultados del autocompletado
                    jugadoresEncontrados.forEach(jugador => {
                        var autocompleteItem = document.createElement('div');
                        autocompleteItem.className = 'autocomplete-item';
                        autocompleteItem.textContent = jugador;

                        // Asignar el clic del usuario para seleccionar el elemento
                        autocompleteItem.onclick = function() {
                            input.value = jugador;

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

function buscarJugador() {
    var nombreJugador = document.getElementById('searchInput').value;

    // Realizar la solicitud al servidor
    fetch('/info/' + encodeURIComponent(nombreJugador))
        .then(response => response.json())
        .then(data => {

            // Mostrar la información del jugador en el elemento con id 'playerInfo'
            var playerInfoElement = document.getElementById('playerInfo');
            playerInfoElement.innerHTML = '<h2>Información de ' + nombreJugador + '</h2>';

            playerInfoElement.innerHTML += "<img src=" + data.result[0].player_logo + ">"

            // Agregar más detalles según la estructura de datos devuelta por el servidor
            playerInfoElement.innerHTML += '<p><b>Ranking actual: </b>' + data.result[0].ranking + '</p>';
            playerInfoElement.innerHTML += '<p><b>Puntos: </b>' + data.result[0].points + '</p>';
            playerInfoElement.innerHTML += '<p><b>Fecha de nacimiento: </b>' + data.result[0].player_bday + '</p>';
            playerInfoElement.innerHTML += '<p><b>País: </b>' + data.result[0].player_country + '</p>';

            var listaTorneos = data.result[0].tournaments;
            
            for (var i = 0; i < listaTorneos.length; i++) {
                var torneo = listaTorneos[i];
                
                // Algo que ocurre solo en la primera iteración
                if (i === 0) {
                    playerInfoElement.innerHTML += '<p><b>Torneos ganados:</b></p>';
                    playerInfoElement.innerHTML += '<p>'+ torneo.name + '(' + torneo.season + ')' + '</p>';
                } else {
                    playerInfoElement.innerHTML += '<p>' + torneo.name + '('+ torneo.season + ')'+ '</p>';
                }
              }

        })
        .catch(error => {
            console.error('Error:', error);

            // Manejar el error, por ejemplo, mostrar un mensaje al usuario
            var playerInfoElement = document.getElementById('playerInfo');
            playerInfoElement.innerHTML = '<p>Error al buscar el jugador.</p>';
        });
}
