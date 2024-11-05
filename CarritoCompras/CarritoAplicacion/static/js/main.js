document.addEventListener("DOMContentLoaded", function() {
    const modal = document.getElementById('modalCarrito');
    const abrirModalBtn = document.getElementById('abrirModalBtn');
    const cerrarModalBtn = document.querySelector('.close-btn');

    // Abrir el modal cuando se haga clic en "Ver carrito"
    abrirModalBtn.addEventListener('click', function() {
        modal.style.display = 'flex'; // Mostrar el modal
    });

    // Cerrar el modal cuando se haga clic en la "X"
    cerrarModalBtn.addEventListener('click', function() {
        modal.style.display = 'none'; // Ocultar el modal
    });

    // Cerrar el modal si se hace clic fuera de la ventana del modal
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none'; // Ocultar el modal si se hace clic fuera de él
        }
    });
});
