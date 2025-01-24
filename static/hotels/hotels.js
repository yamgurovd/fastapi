// Ждем загрузки DOM, чтобы начать выполнение скрипта
document.addEventListener('DOMContentLoaded', () => {

   // Загружаем и отображаем список отелей при загрузке страницы
   fetchHotels();

   // Обработка отправки формы для добавления нового отеля
   document.getElementById('save-hotel').addEventListener('click', async (e) => {
       e.preventDefault(); // Предотвращаем стандартное поведение кнопки

       const title = document.getElementById('hotel-title').value; // Получаем название отеля
       const location = document.getElementById('hotel-location').value; // Получаем локацию

       const hotelId = document.getElementById('hotel-id').value; // Получаем ID отеля (если редактируем)

       const method = hotelId ? 'PUT' : 'POST'; // Определяем метод (PUT если редактируем)
       const url = hotelId ? `/hotels/${hotelId}` : '/hotels'; // Замените на актуальный путь

       // Отправляем запрос для создания или обновления отеля
       const response = await fetch(url, {
           method,
           headers: { 'Content-Type': 'application/json' },
           body: JSON.stringify({ title, location }) // Преобразуем данные в JSON
       });

       if (response.ok) {
           Swal.fire('Успех!', hotelId ? 'Отель обновлен успешно!' : 'Отель добавлен успешно!', 'success');
           hotelForm.reset(); // Очищаем форму после успешного запроса
           fetchHotels(); // Обновляем список отелей
       } else {
           const error = await response.json();
           Swal.fire('Ошибка!', error.detail || 'Ошибка добавления/обновления отеля.', 'error');
       }
   });

   // Обработка клика по кнопке поиска
   document.getElementById('search-button').addEventListener('click', async () => {
       const query = document.getElementById('search-input').value; // Получаем текст запроса из поля поиска

       // Отправляем GET-запрос на сервер с параметрами поиска
       const response = await fetch(`/hotels?query=${encodeURIComponent(query)}`);

       if (response.ok) {
           const hotels = await response.json(); // Преобразуем ответ в JSON
           displayHotels(hotels); // Отображаем найденные отели
       } else {
           Swal.fire('Ошибка!', 'Ошибка при выполнении поиска.', 'error');
       }
   });
});

// Функция для получения списка отелей из API
async function fetchHotels() {
   const response = await fetch('/hotels'); // Отправляем GET-запрос для получения списка отелей

   if (response.ok) {
       const hotels = await response.json(); // Преобразуем ответ в JSON
       displayHotels(hotels); // Отображаем все отели

   } else {
       console.error('Ошибка при получении списка отелей.'); // Выводим ошибку в консоль
       Swal.fire('Ошибка!', 'Ошибка при получении списка отелей.', 'error');
   }
}

// Функция для отображения списка отелей в таблице
function displayHotels(hotels) {
   const hotelsList = document.getElementById('hotel-list'); // Получаем элемент списка отелей
   hotelsList.innerHTML = ''; // Очищаем существующий список

   hotels.forEach(hotel => {
       const tr = document.createElement('tr');

       tr.innerHTML = `
           <td onclick="goToRooms(${hotel.id})" style="cursor: pointer; color: blue; text-decoration: underline;">${hotel.title}</td>
           <td>${hotel.location}</td>
           <td>
               <button onclick="editHotel(${hotel.id}, '${hotel.title}', '${hotel.location}')">Редактировать</button>
               <button onclick="deleteHotel(${hotel.id})">Удалить</button>
           </td>
       `;

       hotelsList.appendChild(tr);
   });

   if (hotels.length === 0) {
       hotelsList.innerHTML = '<tr><td colspan="3">Нет доступных отелей.</td></tr>';
   }
}

// Функция для перехода на страницу номеров для выбранного отеля
function goToRooms(hotelId) {
   window.location.href = `http://localhost:8000/hotels/${hotelId}/rooms.html`; // Замените на нужный путь к статической странице номеров
}

// Функция для редактирования информации об отеле
function editHotel(id, title, location) {
   document.getElementById('hotel-id').value = id;
   document.getElementById('hotel-title').value = title;
   document.getElementById('hotel-location').value = location;
}

// Функция для удаления отеля
async function deleteHotel(id) {
   if (confirm("Вы уверены, что хотите удалить этот отель?")) {
       const response = await fetch(`/hotels/${id}`, { method:'DELETE' });

       if (response.ok) {
           fetchHotels();
           Swal.fire('Успех!', 'Отель удален успешно!', 'success');
       } else {
           Swal.fire('Ошибка!', 'Ошибка при удалении отеля.', 'error');
       }
   }
}
