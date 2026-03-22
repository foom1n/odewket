import os
import threading
from flask import Flask
import asyncio

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running"

@app.route('/health')
def health():
    return "OK", 200

# Функция запуска основного бота
def run_bot():
    # Импортируем main из твоего файла
    from main import main
    # Запускаем асинхронную функцию main()
    asyncio.run(main())

if __name__ == "__main__":
    # Запускаем бота в отдельном потоке
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    # Запускаем Flask-сервер на порту, который даёт Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
