# Law Firm Frontend

React frontend для системы управления юридической фирмой.

## 🚀 Быстрый запуск

### Предварительные требования
- Node.js 18+
- npm или yarn

### Установка и запуск

```bash
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

Приложение будет доступно по адресу http://localhost:3000

## 🔧 Конфигурация

### Переменные окружения (.env)

```bash
# API URL для локальной разработки
REACT_APP_API_URL=http://127.0.0.1:8000

# API URL для Docker
REACT_APP_API_URL=http://backend:8000

# API URL для production
REACT_APP_API_URL=https://yourdomain.com
```

## 📁 Структура проекта

```
src/
├── components/           # React компоненты
│   ├── About/           # Компонент "О компании"
│   ├── Body/            # Главная страница
│   ├── Footer/          # Подвал сайта
│   ├── Header/          # Шапка сайта
│   ├── Navbar/          # Навигационное меню
│   ├── RequestForm/     # Форма обратной связи
│   ├── Services/        # Список услуг
│   └── Staff/           # Список сотрудников
├── config/              # Конфигурация
│   └── api.js          # Настройки API клиента
├── App.js              # Главный компонент
└── index.js            # Точка входа
```

## 🌐 API Интеграция

Проект использует централизованную конфигурацию API в `src/config/api.js`:

```javascript
import { apiClient } from './config/api';

// GET запрос
const services = await apiClient.get('/services/');

// POST запрос
const response = await apiClient.post('/requests/', data);
```

## 🎨 Стили

Проект использует CSS Modules для изоляции стилей:
- Каждый компонент имеет свой `.module.css` файл
- Стили импортируются как `styles.className`

## 📦 Доступные скрипты

### `npm start` / `yarn start`
Запускает приложение в режиме разработки.

### `npm run build` / `yarn build`
Собирает приложение для production в папку `build`.

### `npm test` / `yarn test`
Запускает тесты в интерактивном режиме.

### `npm run eject` / `yarn eject`
**Не рекомендуется!** Извлекает конфигурацию из Create React App.

## 🐳 Docker

Для запуска в Docker используйте:

```bash
# Сборка образа
docker build -t law-frontend .

# Запуск контейнера
docker run -p 3000:3000 \
  -e REACT_APP_API_URL=http://backend:8000 \
  law-frontend
```

## 🔗 Связь с Backend

Frontend взаимодействует с Django backend через REST API:
- Все запросы идут через `apiClient`
- Автоматическая обработка ошибок
- Поддержка различных окружений (dev/prod)

## 🐛 Устранение неполадок

### Проблемы с API подключением
1. Проверьте `REACT_APP_API_URL` в `.env`
2. Убедитесь, что backend запущен
3. Проверьте CORS настройки backend

### Проблемы со стилями
1. Убедитесь, что CSS Modules правильно импортированы
2. Проверьте, что стили не конфликтуют

### Проблемы с зависимостями
```bash
# Очистка кэша
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

## 📝 Разработка

### Добавление нового компонента
1. Создайте папку в `src/components/`
2. Добавьте `.jsx` и `.module.css` файлы
3. Импортируйте и используйте в `App.js`

### Добавление нового API endpoint
1. Обновите `src/config/api.js` при необходимости
2. Используйте `apiClient` в компонентах
3. Добавьте обработку состояний loading/error

## 🚀 Деплой

### Production сборка
```bash
npm run build
```

### Проверка сборки локально
```bash
npx serve -s build -l 3000
```

### Оптимизации
- Код автоматически минифицируется
- Статические файлы оптимизируются
- Неиспользуемый код удаляется (tree shaking)

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
