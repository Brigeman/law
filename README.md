# Law Firm Management System

Система управления юридической фирмой с веб-интерфейсом для клиентов и административной панелью.

## 🏗️ Архитектура

```
┌─────────────────┐    HTTP/API     ┌─────────────────┐    SQL     ┌─────────────────┐
│   React Frontend│ ──────────────► │  Django Backend │ ─────────► │   PostgreSQL    │
│   Port: 3000    │                 │   Port: 8000    │            │   Port: 5432    │
└─────────────────┘                 └─────────────────┘            └─────────────────┘
```

### Компоненты:
- **Backend**: Django 5.0 + Django REST Framework
- **Frontend**: React 18 + Axios
- **Database**: PostgreSQL 13
- **Containerization**: Docker + Docker Compose

## 🚀 Быстрый запуск

### Предварительные требования

- [Docker](https://docs.docker.com/get-docker/) и [Docker Compose](https://docs.docker.com/compose/install/)
- Или Python 3.11+ и Node.js 18+ для локальной разработки

### 1. Клонирование и настройка

```bash
git clone <repository-url>
cd law
```

### 2. Настройка переменных окружения

```bash
# Скопируйте пример конфигурации
cp env.example .env

# Отредактируйте .env файл с вашими настройками
# Обязательно измените SECRET_KEY!
```

### 3. Запуск через Docker (рекомендуется)

```bash
# Запуск всех сервисов
docker-compose up --build

# Или в фоновом режиме
docker-compose up -d --build
```

Сервисы будут доступны по адресам:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/swagger/
- **Django Admin**: http://localhost:8000/admin/

### 4. Запуск для разработки (локально)

#### Backend:
```bash
# Активация виртуального окружения
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows

# Установка зависимостей
pip install -r requirements.txt

# Применение миграций
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser

# Запуск сервера
python manage.py runserver
```

#### Frontend:
```bash
cd frontend

# Установка зависимостей
npm install
# или
yarn install

# Настройка переменных окружения
cp env.example .env

# Запуск в режиме разработки
npm start
# или
yarn start
```

## 📋 Функциональность

### Для клиентов:
- Просмотр услуг компании
- Информация о сотрудниках
- Отправка заявок через форму обратной связи
- Информация о компании

### Для администраторов:
- Управление услугами
- Управление сотрудниками
- Просмотр и обработка заявок
- Управление делами и встречами
- Система уведомлений по email

## 🔧 API Endpoints

### Основные эндпоинты:
- `GET /services/` - Получение списка услуг
- `GET /staff/` - Получение списка сотрудников
- `GET /about/` - Информация о компании
- `POST /requests/` - Отправка заявки
- `GET /cases/` - Список дел (требует аутентификации)
- `POST /appointments/` - Создание встречи (требует аутентификации)

### Документация API:
- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/

## 🛠️ Разработка

### Структура проекта

```
law/
├── app/                    # Django приложение
│   ├── models.py          # Модели данных
│   ├── views.py           # API views
│   ├── serializers.py     # DRF сериализаторы
│   ├── urls.py            # URL маршруты
│   └── admin.py           # Django admin
├── frontend/              # React приложение
│   ├── src/
│   │   ├── components/    # React компоненты
│   │   ├── config/        # Конфигурация API
│   │   └── App.js         # Главный компонент
│   └── package.json       # Зависимости фронтенда
├── main/                  # Настройки Django
│   ├── settings.py        # Основные настройки
│   └── urls.py            # Корневые URL
├── requirements.txt       # Python зависимости
├── docker-compose.yml     # Docker конфигурация
└── .env                   # Переменные окружения
```

### Добавление новых функций

1. **Backend**: Добавьте модель в `app/models.py`, создайте миграцию, добавьте API endpoint
2. **Frontend**: Создайте компонент в `frontend/src/components/`, используйте `apiClient` для запросов
3. **Тестирование**: Добавьте тесты в `app/tests.py`

### Переменные окружения

#### Backend (.env):
```bash
# Обязательные
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=law_firm
DB_USER=postgres
DB_PASSWORD=your-password

# Опциональные
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

#### Frontend (.env):
```bash
# Для локальной разработки
REACT_APP_API_URL=http://127.0.0.1:8000

# Для Docker
REACT_APP_API_URL=http://backend:8000
```

## 🐛 Устранение неполадок

### Проблемы с подключением к базе данных
```bash
# Проверьте статус контейнеров
docker-compose ps

# Пересоздайте базу данных
docker-compose down -v
docker-compose up --build
```

### Проблемы с CORS
Убедитесь, что в `.env` файле правильно указан `CORS_ALLOWED_ORIGINS`:
```bash
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### Проблемы с API подключением
Проверьте, что в `frontend/.env` правильно указан `REACT_APP_API_URL`:
```bash
# Для локальной разработки
REACT_APP_API_URL=http://127.0.0.1:8000

# Для Docker
REACT_APP_API_URL=http://backend:8000
```

### Очистка кэша
```bash
# Очистка Docker
docker-compose down
docker system prune -f

# Очистка npm/yarn кэша
cd frontend
npm cache clean --force
# или
yarn cache clean
```

## 🔒 Безопасность

### Настройки для production:
1. Установите `DEBUG=False` в `.env`
2. Сгенерируйте новый `SECRET_KEY`
3. Настройте `ALLOWED_HOSTS` для вашего домена
4. Включите `SECURE_SSL_REDIRECT=True`
5. Настройте HTTPS

### Генерация SECRET_KEY:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## 📝 Лицензия

Этот проект разработан для демонстрационных целей.

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для новой функции
3. Внесите изменения
4. Создайте Pull Request

## 📞 Поддержка

При возникновении проблем создайте issue в репозитории или обратитесь к разработчикам.
