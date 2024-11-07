document.addEventListener("DOMContentLoaded", function() {
    const modal = document.getElementById('modalCarrito');
    const abrirModalBtn = document.getElementById('abrirModalBtn');
    const cerrarModalBtn = document.querySelector('.close-btn');
    const containerCarrito = document.querySelector('.container-icono-carrito'); // Seleccionamos el contenedor

    // Abrir el modal cuando se haga clic en "Ver carrito"
    abrirModalBtn.addEventListener('click', function() {
        modal.style.display = 'flex'; // Mostrar el modal
        containerCarrito.style.transition = "transform 1s ease"; // Asegura que haya una transición suave
        containerCarrito.style.transform = "rotate(180deg)"; // Aplica la rotación al contenedor
    });

    // Cerrar el modal cuando se haga clic en la "X"
    cerrarModalBtn.addEventListener('click', function() {
        modal.style.display = 'none'; // Ocultar el modal
        containerCarrito.style.transform = "rotate(0deg)"; // Eliminar la rotación
    });

    // Cerrar el modal si se hace clic fuera de la ventana del modal
    window.addEventListener('click', function(event) {
        if (event.target === modal) { // Verifica si el clic fue fuera del contenido del modal
            modal.style.display = 'none'; // Ocultar el modal
            containerCarrito.style.transform = "rotate(0deg)"; // Eliminar la rotación
        }
    });

    // Delegación de eventos para los enlaces de acción del carrito
    // Seleccionamos la tabla del carrito y agregamos un único evento para los enlaces
    const carritoTable = document.querySelector('.carrito-table');
    carritoTable.addEventListener('click', function(event) {
        // Verificamos si el clic fue en un enlace con la clase 'accion-carrito'
        if (event.target && event.target.classList.contains('accion-carrito')) {
            event.stopPropagation(); // Detiene la propagación del clic para que no cierre el modal
            // Aquí puedes agregar la lógica para actualizar el carrito, por ejemplo:
            // 1. Incrementar o disminuir la cantidad de productos
            // 2. Realizar un fetch para actualizar la base de datos o el carrito en el servidor
        }
    });
});
