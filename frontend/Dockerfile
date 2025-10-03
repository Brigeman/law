FROM node:18-alpine

WORKDIR /app

# Копируем package файлы для кэширования слоев
COPY package*.json ./

# Устанавливаем зависимости
RUN yarn install --frozen-lockfile

# Копируем исходный код
COPY . .

# Создаем .env файл для production
RUN echo "REACT_APP_API_URL=http://backend:8000" > .env

# Собираем приложение
RUN yarn build

# Устанавливаем serve для production
RUN yarn global add serve

EXPOSE 3000

CMD ["serve", "-s", "build", "-l", "3000"]
