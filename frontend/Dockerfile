# Используем официальный образ Node.js в качестве базового
FROM node:18-alpine

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и yarn.lock
COPY package*.json ./

# Устанавливаем зависимости
RUN yarn install

# Копируем остальные файлы
COPY . .

# Собираем проект
RUN yarn build

# Устанавливаем глобально serve для запуска собранного приложения
RUN yarn global add serve

# Объявляем порт, на котором будет работать приложение
EXPOSE 3000

# Запускаем приложение
CMD ["serve", "-s", "build"]
