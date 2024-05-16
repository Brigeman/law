# Используем официальный образ Python в качестве базового
FROM python:3.11.6

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы
COPY . .

# Объявляем порт, на котором будет работать приложение
EXPOSE 8000

# Запускаем сервер с миграциями и сбором статики
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn main.wsgi:application --bind 0.0.0.0:8000"]
