// Получаем ID отеля из URL
const urlParams = new URLSearchParams(window.location.search);
const hotelId = urlParams.get('hotel_id'); // Предполагается, что вы передаете hotel_id в URL

document.addEventListener('DOMContentLoaded', () => {
    fetchRooms(); // Загружаем номера при загрузке страницы

    document.getElementById('save-room').addEventListener('click', async (e) => {
        e.preventDefault();

        const title = document.getElementById('room-title').value;
        const description = document.getElementById('room-description').value;
        const price = document.getElementById('room-price').value;
        const quantity = document.getElementById('room-quantity').value;

        const roomId = document.getElementById('room-id').value;

        const method = roomId ? 'PUT' : 'POST';
        const url = roomId ? `/hotels/${hotelId}/rooms/${roomId}` : `/hotels/${hotelId}/rooms`;

        const response = await fetch(url, {
            method,
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({title, description, price, quantity})
        });

        if (response.ok) {
            Swal.fire('Успех!', roomId ? 'Номер обновлен успешно!' : 'Номер добавлен успешно!', 'success');
            clearForm();
            fetchRooms();
        } else {
            const error = await response.json();
            Swal.fire('Ошибка!', error.detail || 'Ошибка добавления/обновления номера.', 'error');
        }
    });
});

async function fetchRooms() {
    const response = await fetch(`/hotels/${hotelId}/rooms`); // Получаем список номеров

    if (response.ok) {
        const rooms = await response.json(); // Преобразуем ответ в JSON
        displayRooms(rooms); // Отображаем номера
    } else {
        console.error('Ошибка при получении списка номеров.');
        Swal.fire('Ошибка!', 'Ошибка при получении списка номеров.', 'error');
    }
}

function displayRooms(rooms) {
    const roomsList = document.getElementById('room-list');
    roomsList.innerHTML = '';

    rooms.forEach(room => {
        const tr = document.createElement('tr');

        tr.innerHTML = `
           <td>${room.title}</td>
           <td>${room.description || 'Нет описания'}</td>
           <td>${room.price}</td>
           <td>${room.quantity}</td>
           <td>
               <button onclick="editRoom(${room.id}, '${room.title}', '${room.description || ''}', ${room.price}, ${room.quantity})">Редактировать</button>
               <button onclick="deleteRoom(${room.id})">Удалить</button>
           </td>
       `;

        roomsList.appendChild(tr);
    });

    if (rooms.length === 0) {
        roomsList.innerHTML = '<tr><td colspan="5">Нет доступных номеров.</td></tr>';
    }
}

function clearForm() {
    document.getElementById('room-id').value = '';
    document.getElementById('room-title').value = '';
    document.getElementById('room-description').value = '';
    document.getElementById('room-price').value = '';
    document.getElementById('room-quantity').value = '';
}

function editRoom(id, title, description, price, quantity) {
    document.getElementById('room-id').value = id;
    document.getElementById('room-title').value = title;
    document.getElementById('room-description').value = description;
    document.getElementById('room-price').value = price;
    document.getElementById('room-quantity').value = quantity;
}

async function deleteRoom(id) {
    if (confirm("Вы уверены, что хотите удалить этот номер?")) {
        const response = await fetch(`/hotels/${hotelId}/rooms/${id}`, {method: 'DELETE'});

        if (response.ok) {
            fetchRooms();
            Swal.fire('Успех!', 'Номер удален успешно!', 'success');
        } else {
            Swal.fire('Ошибка!', 'Ошибка при удалении номера.', 'error');
        }
    }
}
