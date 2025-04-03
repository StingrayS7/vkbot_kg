import os
from dotenv import load_dotenv
from utils.logger import system_logger


system_logger.info("Загрузка переменных окружения...")
load_dotenv()

# Проверка загрузки переменных окружения
system_logger.info(f"OPENROUTER_API_KEY загружен: {'да' if os.getenv('OPENROUTER_API_KEY') else 'нет'}")
if not os.getenv('OPENROUTER_API_KEY'):
    raise ValueError("OPENROUTER_API_KEY не найден в переменных окружения. Проверьте .env файл")

# VK API settings
VK_GROUP_TOKEN = os.getenv('VK_GROUP_TOKEN')
VK_GROUP_ID = int(os.getenv('VK_GROUP_ID', 0))

# OpenRouter settings
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Knowledge Graph settings
DOCUMENTS_DIR = "src/data/documents"

# Model sitings
MODEL = "deepseek/deepseek-chat-v3-0324:free"

temperature = 0.3
max_tokens = 500
top_p = 0.9
frequency_penalty = 0.2
presence_penalty = 0.2
