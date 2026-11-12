# ide-configure

## Запуск API

Для запуска необходимы **Python** и работающий **PostgreSQL**.

1. Создайте в PostgreSQL базу данных, например `books_catalog`.
2. В корне проекта создайте файл `.env` и укажите параметры подключения:

   ```env
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=books_catalog
   DB_USER=postgres
   DB_PASSWORD=your_password
   ```

3. Создайте и активируйте виртуальное окружение, затем установите зависимости:

   ```bash
   python -m venv .venv
   ```

   Linux / macOS:
   ```bash
   source .venv/bin/activate
   ```

   Windows PowerShell:
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   ```bash
   pip install -r requirements.txt
   ```

4. Инициализируйте базу данных и добавьте демонстрационные записи:

   ```bash
   python -m app.init_db
   ```

5. Запустите API из корневой папки проекта:

   ```bash
   uvicorn app.main:app --reload
   ```

После запуска API будет доступно по адресу `http://127.0.0.1:8000`.

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
- Проверка состояния: `http://127.0.0.1:8000/health`

При старте API таблицы создаются автоматически. Шаг инициализации (`app.init_db`) дополнительно заполняет базу начальными категориями и книгами.
