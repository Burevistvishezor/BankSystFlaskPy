# Создаём папку проекта
mkdir BankSystemFlask
cd BankSystemFlask

# Инициализируем git
git init

# Копируем туда файлы:
# bank.py, app.py, accounts.json, templates/, static/
# Создаём виртуальное окружение
python -m venv venv

# Активируем (Windows)
venv\Scripts\activate

# Активируем (Mac/Linux)
source venv/bin/activate

# Устанавливаем Flask
pip install Flask
# Добавляем все файлы
git add .

# Первый коммит
git commit -m "Initial commit - BankSystem Flask v5.0"

# Привязываем репозиторий
git remote add origin https://github.com/<username>/BankSystemFlask.git

# Отправляем на GitHub
git push -u origin main
python -m venv venv
venv\Scripts\activate
source venv/bin/activate
pip install Flask
python app.pyhttp://127.0.0.1:5000/

