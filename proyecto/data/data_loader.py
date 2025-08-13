from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import yaml
import os

# Cargar configuración desde config.yaml y la API key desde .env
from dotenv import load_dotenv

CONFIG_PATH = 'proyecto/config.yaml'
ENV_PATH = 'proyecto/.env'

def get_openai_api_key():
    load_dotenv(ENV_PATH)
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env")
    return api_key

def load_config():
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def initialize_vector_store(data, persist_dir="proyecto/data/vector_store"):
    """
    Crea un almacén vectorial desde datos iniciales.
    """
    if not data:
        raise ValueError("No data provided to initialize the vector store.")
    try:
        api_key = get_openai_api_key()
        embeddings = OpenAIEmbeddings(openai_api_key=api_key)
        # Divide los textos en párrafos pequeños
        texts = []
        for item in data:
            # Si item es string, dividir por doble salto de línea o punto
            if isinstance(item, str):
                texts.extend([p.strip() for p in item.split('\n') if p.strip()])
            else:
                texts.append(str(item))
        # Crear y persistir el vector store
        vector_store = Chroma.from_texts(texts, embeddings, persist_directory=persist_dir)
        vector_store.persist()
        return vector_store
    except Exception as e:
        print(f"Error initializing vector store: {e}")
        raise


def load_vector_store(persist_dir="proyecto/data/vector_store"):
    """
    Carga un vector store persistido.
    """
    try:
        api_key = get_openai_api_key()
        embeddings = OpenAIEmbeddings(openai_api_key=api_key)
        vector_store = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
        return vector_store
    except Exception as e:
        print(f"Error loading vector store: {e}")
        raise