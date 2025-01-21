document.getElementById('register-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const email = document.getElementById('register-email').value;
    const password = document.getElementById('register-password').value;

    const response = await fetch('/auth/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({email, password})
    });

    const message = document.getElementById('message');

    if (response.ok) {
        message.textContent = 'Регистрация прошла успешно!';
        message.style.color = 'green';
        document.getElementById('register-form').reset();
    } else {
        const error = await response.json();
        message.textContent = error.detail || 'Ошибка регистрации.';
        message.style.color = 'red';
    }
});

document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;

    const response = await fetch('/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({email, password})
    });

    const message = document.getElementById('message');

    if (response.ok) {
        const data = await response.json();
        message.textContent = 'Вход выполнен успешно!';
        message.style.color = 'green';

        // Сохраняем токен в localStorage
        localStorage.setItem('access_token', data.access_token);

        // Перенаправление на страницу управления отелями
        window.location.href = 'http://localhost:8000/static/hotels/hotels.html'; // Замените '/hotels' на нужный путь
    } else {
        const error = await response.json();
        message.textContent = error.detail || 'Ошибка входа.';
        message.style.color = 'red';
    }
});

// Обработчик для кнопки "Выйти"
document.getElementById('logout-button').addEventListener('click', async () => {
    const response = await fetch('/auth/logout', {
        method: 'POST',
        credentials: 'include' // Включаем куки при запросе
    });

    if (response.ok) {
        localStorage.removeItem('access_token'); // Удаляем токен из localStorage
        document.getElementById('message').textContent = 'Вы вышли из системы.';
        document.getElementById('message').style.color = 'green';

        // Скрываем кнопку выхода
        document.getElementById('logout-button').style.display = 'none';

        // Можно перенаправить на страницу входа или главную
        window.location.href = '/';
    } else {
        const error = await response.json();
        document.getElementById('message').textContent = error.detail || 'Ошибка выхода.';
        document.getElementById('message').style.color = 'red';
    }
});
