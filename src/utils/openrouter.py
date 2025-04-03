import requests
from config import OPENROUTER_API_KEY, OPENROUTER_API_URL, MODEL, temperature, max_tokens, top_p, frequency_penalty, presence_penalty

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY не настроен. Проверьте .env файл")

def generate_response(question: str, context: str) -> str:
    """
    Генерирует ответ на вопрос пользователя с использованием OpenRouter API
    и модели DeepSeek v3 с учетом контекста из knowledge graph
    
    :param question: Вопрос пользователя
    :param context: Релевантный контекст из knowledge graph
    :return: Сгенерированный ответ
    """
    prompt = f"""
    Ты - помощник автономного учреждения дополнительного образования. Отвечай точно и по делу на вопросы родителей и учеников,
    которые там учатся или планируют учиться в будущем 
    строго на основе предоставленной информации. Если информации недостаточно, 
    вежливо попроси уточнить вопрос. Не выдумывай информацию.

    Контекст:
    {context}

    Вопрос:
    {question}

    Ответ должен быть кратким и содержательным:
    """

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
            "max_tokens": max_tokens,
            "top_p": top_p,
            "frequency_penalty":frequency_penalty,
            "presence_penalty": presence_penalty
        }

    try:
        response = requests.post(
            OPENROUTER_API_URL,
            headers=headers,
            json=payload,
            timeout=10
        )
        response.raise_for_status()
        
        result = response.json()
            
        return result['choices'][0]['message']['content'].strip()
    
    except requests.exceptions.HTTPError as e:
        error_msg = f"Ошибка OpenRouter API ({e.response.status_code}): {e.response.text}"
        print(error_msg)
        return "Извините, временные технические проблемы. Попробуйте задать вопрос позже."
    except Exception as e:
        error_msg = f"Ошибка при запросе к OpenRouter: {str(e)}"
        print(error_msg)
        return "Извините, произошла ошибка при обработке вашего вопроса. Пожалуйста, попробуйте позже."
