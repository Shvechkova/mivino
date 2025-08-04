# Mivino

Проект для работы с вином и винными сервисами.

## Структура проекта

```
mivino/
├── frontend/          # Фронтенд приложение
├── services/          # Микросервисы
│   ├── bff-service/   # Backend for Frontend сервис
│   └── wine-service/  # Сервис для работы с вином
├── shared/            # Общие модули и утилиты
├── docker-compose.yml # Конфигурация Docker Compose
├── Makefile          # Команды для управления проектом
└── .gitignore        # Исключения для Git
```

## Быстрый старт

1. Убедитесь, что у вас установлены Docker и Docker Compose
2. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/your-username/mivino.git
   cd mivino
   ```
3. Запустите проект:
   ```bash
   docker-compose up -d
   ```

## Разработка

Для разработки используйте команды из Makefile:

```bash
# Запуск всех сервисов
make up

# Остановка всех сервисов
make down

# Просмотр логов
make logs
```

## Технологии

- **Frontend**: React/Next.js
- **Backend**: Python (FastAPI)
- **Контейнеризация**: Docker & Docker Compose
- **База данных**: PostgreSQL (предположительно)

## Лицензия

MIT 