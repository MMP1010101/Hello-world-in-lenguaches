<!DOCTYPE html>
<html>
<head>
    <title>Fecha y Hora Actual</title>
    <style>
        /* Estilo para hacer la fecha grande y centrada */
        #fecha {
            font-family: "Poppins", sans-serif; /* Fuente Poppins */
            font-size: 36px; /* Tamaño de fuente grande */
            text-align: center; /* Centro de texto horizontal */
            margin-top: 100px; /* Margen superior para centrar verticalmente */
        }
    </style>
    <script>
        function actualizarFechaHora() {
            // Obtiene un elemento HTML con el ID "fecha"
            var elementoFecha = document.getElementById("fecha");
            
            // Obtiene la fecha y hora actual en JavaScript
            var fechaActual = new Date();
            
            // Formatea la fecha y hora como "DD/MM/YYYY HH:MM:SS"
            var fechaFormateada = fechaActual.toLocaleString();
            
            // Actualiza el contenido del elemento con la fecha y hora actual
            elementoFecha.innerHTML = fechaFormateada;
        }

        // Llama a la función para actualizar la fecha y hora cada segundo
        setInterval(actualizarFechaHora, 1000);
    </script>
</head>
<body>
    <div id="fecha">Fecha y Hora Actual</div>
</body>
</html>
