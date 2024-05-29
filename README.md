# Установка
Клонировать репозиторий:  
```bash
git clone https://github.com/MixidFinder/stepik_final_task_selenium.git
```

Создать `.venv` и активировать его:  
```bash
python -m venv .venv
.venv\Scripts\activate
```

Установить зависимости:  
```bash
pip install -r requirements.txt
```

# Использование
Запуск для ревью:  
```bash
pytest -v --tb=line --language=en -m need_review
```
