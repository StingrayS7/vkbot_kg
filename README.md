# VK Бот для Матрешки

Бот для ответов на вопросы абитуриентов в ВКонтакте с использованием OpenRouter и Knowledge Graphs.
Формирует базу из файлов txt, docx, pdf, json форматов.
Есть простое логирование (логи системы и чатов разделены).

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/StingrayS7/vkbot_kg.git
cd vkbot_kg
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Настройка

1. Создайте файл `.env` в корне проекта и заполните его:
```
VK_GROUP_TOKEN=ваш_токен_группы
VK_GROUP_ID=ваш_id_группы
OPENROUTER_API_KEY=ваш_api_ключ_openrouter
```

2. Добавьте документы в папку `src/data/documents`:
- PDF, DOCX, TXT, JSON файлы с информацией

3. Настройки модели хранятся в src/config.py
- по умолчанию используется модель deepseek/deepseek-chat-v3-0324:free

## Запуск

```bash
python src/main.py
```

## Добавление новых документов

1. Поместите файлы в `src/data/documents`
2. Бот автоматически обработает их при следующем запуске