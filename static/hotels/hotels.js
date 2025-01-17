// script.js
document.addEventListener('DOMContentLoaded', () => {

    const hotelForm = document.getElementById('hotel-form');

    // Fetch and display hotels on page load
    fetchHotels();

    // Handle form submission
    hotelForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const title = document.getElementById('hotel-title').value;
        const location = document.getElementById('hotel-location').value;

        const response = await fetch('/hotels', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({title, location})
        });

        if (response.ok) {
            document.getElementById('message').textContent = 'Отель добавлен успешно!';
            document.getElementById('message').style.color = 'green';
            hotelForm.reset();
            fetchHotels(); // Refresh the hotel list
        } else {
            const error = await response.json();
            document.getElementById('message').textContent = error.detail || 'Ошибка добавления отеля.';
            document.getElementById('message').style.color = 'red';
        }
    });
});

// Function to fetch hotels from the API
async function fetchHotels() {
    const response = await fetch('/hotels');

    if (response.ok) {
        const hotels = await response.json();
        const hotelsList = document.getElementById('hotels');
        hotelsList.innerHTML = ''; // Clear existing list

        hotels.forEach(hotel => {
            const li = document.createElement('li');
            li.textContent = `${hotel.title} - ${hotel.location}`;
            hotelsList.appendChild(li);
        });

        if (hotels.length === 0) {
            hotelsList.innerHTML = '<li>Нет доступных отелей.</li>';
        }

    } else {
        console.error('Ошибка при получении списка отелей.');
        document.getElementById('message').textContent = 'Ошибка при получении списка отелей.';
        document.getElementById('message').style.color = 'red';
    }
}
