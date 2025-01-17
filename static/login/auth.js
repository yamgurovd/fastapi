// script.js
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
        // You can redirect or perform other actions here
        console.log(data.access_token); // Store token if needed
    } else {
        const error = await response.json();
        message.textContent = error.detail || 'Ошибка входа.';
        message.style.color = 'red';
    }
});
