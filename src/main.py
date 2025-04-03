import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import VK_GROUP_TOKEN, VK_GROUP_ID
from handlers.message_handler import handle_message
from utils.logger import system_logger, chat_logger

def main():
    # Инициализация VK API
    vk_session = vk_api.VkApi(token=VK_GROUP_TOKEN)
    vk = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, VK_GROUP_ID)

    system_logger.info("Бот запущен и ожидает сообщений...")

    # Основной цикл обработки событий
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            message = event.object.message
            user_id = message['from_id']
            text = message['text']

            # Обрабатываем сообщение и получаем ответ
            try:
                chat_logger.info(f"Получено сообщение от {user_id}: {text}")
                response = handle_message(event)
            except Exception as e:
                system_logger.error(f"Ошибка обработки сообщения: {e}")
                response = "Произошла ошибка при обработке вашего сообщения"
            
            # Отправляем ответ пользователю
            if response:
                chat_logger.info(f"Отправка ответа пользователю {user_id}: {response}")
                vk.messages.send(
                    user_id=user_id,
                    message=response,
                    random_id=0
                )

if __name__ == "__main__":
    main()
