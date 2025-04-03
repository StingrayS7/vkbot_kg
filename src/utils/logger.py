import logging

def setup_loggers():
    # Форматтер для обоих логгеров
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # Системный логгер
    system_logger = logging.getLogger('system')
    system_logger.setLevel(logging.INFO)
    
    system_handler = logging.FileHandler('logs/system.log', encoding='utf-8')
    system_handler.setFormatter(formatter)
    system_logger.addHandler(system_handler)
    system_logger.addHandler(logging.StreamHandler())
    
    # Чат-логгер
    chat_logger = logging.getLogger('chat')
    chat_logger.setLevel(logging.INFO)
    
    chat_handler = logging.FileHandler('logs/chat.log', encoding='utf-8')
    chat_handler.setFormatter(formatter)
    chat_logger.addHandler(chat_handler)
    chat_logger.addHandler(logging.StreamHandler())
    
    return system_logger, chat_logger

system_logger, chat_logger = setup_loggers()
