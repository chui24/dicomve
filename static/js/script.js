// Función para animar la transición al cambiar de vista
function animateTransition() {
    // Agregamos una clase para animar la transición
    document.body.classList.add('transition');
    // Esperamos un corto tiempo para que la clase de transición se aplique antes de redirigir
    setTimeout(() => {
        // Redirigimos a la página de login
        window.location.href = '/login';
    }, 500); // Esperamos 500 milisegundos (0.5 segundos) antes de redirigir
}

// Asociamos la función de animación al botón de login en el home
const loginButton = document.querySelector('.login-button');
loginButton.addEventListener('click', animateTransition);

// Evento para eliminar la clase de transición después de que se complete la animación
document.body.addEventListener('transitionend', () => {
    // Verificamos si la clase de transición está presente en el cuerpo
    if (document.body.classList.contains('transition')) {
        // Eliminamos la clase de transición
        document.body.classList.remove('transition');
    }
});
