# DevOps Webapp

Простое веб-приложение, использующее `http.server` и `nginx`

**Требования**
- Docker (версия >= 20.10)
- Docker Compose (встроенный в Docker Engine или standalone)

**Шаги запуска (локально)**
1. Открыть терминал в корне проекта
2. Собрать и запустить контейнеры в фоне:

```bash
docker compose up --build -d
```

**Команды для проверки работоспособности**
- Проверить корневой путь через NGINX (порт 80 на хосте):

```bash
curl -i http://localhost/
```

- Проверить health: (NGINX проксирует запрос на backend; можно также проверить напрямую backend:8080 внутри сети контейнеров)

```bash
curl -s http://localhost/health
```

Если всё работает, `curl http://localhost/` вернёт "Hello from Effective Mobile!", а `/health` - JSON с полем `status: "healthy"`.

**Краткое описание архитектуры**
Проект состоит из простого Python-HTTP сервера (`backend`), упакованного в Docker-образ, и `nginx` как обратный прокси. `docker-compose.yml` создаёт общую сеть `webapp-network`, поднимает `backend` и `nginx`. `nginx` слушает на порту 80 хоста и проксирует запросы к контейнеру `backend:8080`.


**Список технологий**
- Python 3 (встроенный `http.server` в `backend/app.py`)
- Docker
- Docker Compose
- NGINX
- bash / curl (healthcheck)


