// static/js/login.js

$(document).ready(function() {
    $('#login-form').on('submit', function(e) {
        e.preventDefault();
        $.ajax({
            url: '{% url "login_view" %}',  // Asegúrate de que este nombre coincide con el nombre en urls.py
            type: 'POST',
            data: $(this).serialize(),
            headers: {'X-CSRFToken': '{{ csrf_token }}'},
            success: function(response) {
                if (response.success) {
                    window.location.href = '{% url "logged_in" %}';  // Redirige a la página de inicio de sesión o estado de usuario conectado
                } else {
                    $('#error-message').text(response.error);
                }
            },
            error: function() {
                $('#error-message').text('Login failed. Please try again.');
            }
        });
    });
});
