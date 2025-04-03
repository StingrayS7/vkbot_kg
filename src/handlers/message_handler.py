from typing import Dict, Any
from utils.openrouter import generate_response
from utils.knowledge_graph import get_relevant_knowledge

def handle_message(event: Dict[str, Any]) -> str:
    """
    Обрабатывает входящее сообщение от пользователя
    
    :param event: Событие от VK API
    :return: Текст ответа
    """
    message = event.object.message
    text = message.get('text', '').strip()
    user_id = message.get('from_id')
    
    if not text:
        return "Пожалуйста, задайте ваш вопрос."
    
    # Получаем релевантный контекст
    context = get_relevant_knowledge(text)
    
    # Генерируем ответ с помощью OpenRouter
    response = generate_response(text, context)
    
    # Логируем запрос и ответ
    log_interaction(user_id, text, response)
    
    return response

def log_interaction(user_id: int, question: str, answer: str):
    """
    Логирует взаимодействие с пользователем
    
    :param user_id: ID пользователя ВК
    :param question: Вопрос пользователя
    :param answer: Ответ бота
    """
    # # TODO: Реализовать сохранение логов в файл или БД
    # print(f"User {user_id} asked: {question}")
    # print(f"Bot answered: {answer}")
