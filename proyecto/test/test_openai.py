
from langchain_openai import ChatOpenAI
import yaml
import os
from dotenv import load_dotenv


# Cargar configuración desde el archivo YAML (si necesitas otros datos)
with open('proyecto/config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# Cargar variables de entorno desde .env
load_dotenv(dotenv_path='proyecto/.env')
openai_api_key = os.getenv('OPENAI_API_KEY')


# Inicializar el modelo de lenguaje
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key=openai_api_key
)


# Realizar una pregunta simple
question = "What is a chatbot?"
response = llm.invoke(question)
print("Q:", question)
print("A:", response.content)