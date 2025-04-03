import os
import json
from config import DOCUMENTS_DIR
from utils.logger import system_logger

class KnowledgeGraph:
    def __init__(self):
        self.graph = {}
        self.load_knowledge_graphs()

    def load_knowledge_graphs(self):
        """Загружает все knowledge graphs, обрабатывает документы и историю чатов"""        
        if not os.path.exists(DOCUMENTS_DIR):
            os.makedirs(DOCUMENTS_DIR)

        # Обрабатываем новые документы
        for filename in os.listdir(DOCUMENTS_DIR):
            filepath = os.path.join(DOCUMENTS_DIR, filename)
            if filename.lower().endswith(('.pdf', '.docx', '.txt', '.json')):
                if self.add_document(filepath):
                    system_logger.info(f"Документ {filename} успешно обработан")

    def get_relevant_knowledge(self, question: str) -> str:
        """
        Возвращает релевантный контекст для вопроса из knowledge graph
        
        :param question: Вопрос пользователя
        :return: Релевантный контекст
        """
        # TODO: Реализовать более сложный поиск по ключевым словам
        # Пока возвращаем весь граф знаний (для демонстрации)
        context = []
        for topic, facts in self.graph.items():
            context.append(f"{topic}:")
            for fact in facts:
                context.append(f"- {fact}")
        
        return "\n".join(context) if context else "Информация не найдена"

    def add_document(self, filepath: str):
        """Добавляет документ в knowledge graph, парсит и извлекает информацию"""
        from PyPDF2 import PdfReader
        from docx import Document
        import os

        try:
            text = ""
            ext = os.path.splitext(filepath)[1].lower()
            
            if ext == '.pdf':
                reader = PdfReader(filepath)
                text = "\n".join(page.extract_text() for page in reader.pages)
            elif ext == '.docx':
                doc = Document(filepath)
                text = "\n".join(para.text for para in doc.paragraphs)
            elif ext == '.txt':
                with open(filepath, 'r', encoding='utf-8') as f:
                    text = f.read()
            elif ext == '.json':
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, dict):
                        # Обработка JSON словаря
                        for key, values in data.items():
                            if isinstance(values, list):
                                self.graph[key] = [str(v) for v in values]
                            else:
                                self.graph[key] = [str(values)]
                    else:
                        # Обработка других JSON структур (массивов и т.д.)
                        self.graph[os.path.basename(filepath)] = [str(data)]
                    return True
            else:
                system_logger.info(f"Неподдерживаемый формат файла: {ext}")
                return False
                
            # Простая обработка текста - можно улучшить
            if isinstance(text, str):
                sections = text.split('\n\n')  # Разделяем по двойным переносам строк
                for section in sections:
                    if ':' in section:
                        key, *values = section.split(':')
                        self.graph[key.strip()] = [v.strip() for v in values if v.strip()]
                    
            return True
            
        except Exception as e:
            system_logger.info(f"Ошибка обработки документа {filepath}: {str(e)}")
            return False

# Глобальный экземпляр knowledge graph
knowledge_graph = KnowledgeGraph()

def get_relevant_knowledge(question: str) -> str:
    """Интерфейсная функция для получения релевантного контекста"""
    return knowledge_graph.get_relevant_knowledge(question)
