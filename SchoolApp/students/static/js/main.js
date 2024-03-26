document.addEventListener('DOMContentLoaded', function() {
    // Zarejestrowanie nasłuchiwania kliknięcia dla wszystkich ikon usuwania.
    const deleteIcons = document.querySelectorAll('.fa-trash');
    
    deleteIcons.forEach(icon => {
        icon.addEventListener('click', function() {
            // Pobranie identyfikatora ucznia z atrybutu dataset.
            const studentId = this.dataset.studentId;
            console.log('ID ucznia:', studentId);
            
            // Wyświetlenie potwierdzenia przed usunięciem ucznia.
            const confirmation = confirm('Czy na pewno chcesz usunąć tego ucznia?');
            
            // Jeśli użytkownik potwierdzi, usuń ucznia za pomocą żądania fetch.
            if (confirmation) {
                // Pobranie tokena CSRF z ciasteczka.
                const csrftoken = getCookie('csrftoken');
                
                // Wysłanie żądania DELETE do odpowiedniego adresu URL.
                fetch(`/students/delete/${studentId}/`, {
                    method: 'DELETE',
                    headers: {
                        'X-CSRFToken': csrftoken
                    },
                })
                .then(response => {
                    // Obsługa odpowiedzi z serwera po próbie usunięcia ucznia.
                    if (response.ok) {
                        alert('Uczeń został pomyślnie usunięty.');
                        location.reload(); // Przeładowanie strony po pomyślnym usunięciu.
                    } else {
                        alert('Wystąpił błąd podczas usuwania ucznia.');
                    }
                })
                .catch(error => {
                    console.error('Wystąpił błąd podczas wysyłania żądania:', error);
                });
            }
        });
    });

    // Funkcja do pobierania wartości ciasteczka na podstawie jego nazwy.
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
