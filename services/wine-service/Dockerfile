FROM python:3.13-slim

# Установка локали (избегаем предупреждений)
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Рабочая директория
WORKDIR /app

# Копируем и устанавливаем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


COPY . .

# Открываем порт
EXPOSE 8002

# Запуск приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]