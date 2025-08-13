
import streamlit as st
from data.data_loader import load_config, initialize_vector_store

# Configuración de la página
st.set_page_config(page_title="Gym Assistant Bot", page_icon="🤖", layout="centered")

# Agregar CSS personalizado (paleta suave y moderna)
st.markdown(
    """
    <style>
    body {
        background: #f8fafc;
    }
    .main {
        background: #f8fafc;
    }
    .chat-message {
        border-radius: 16px;
        padding: 1rem;
        margin-bottom: 1rem;
        max-width: 80%;
        font-size: 1.08rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        border: none;
    }
    .user-message {
        background: linear-gradient(90deg, #f1f5f9 0%, #e0e7ef 100%);
        color: #334155;
        margin-left: auto;
        border: 1px solid #cbd5e1;
    }
    .bot-message {
        background: linear-gradient(90deg, #f0fdfa 0%, #dbeafe 100%);
        color: #2563eb;
        margin-right: auto;
        border: 1px solid #bae6fd;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        margin-top: 2rem;
    }
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 0.5em;
    }
    .logo-img {
        width: 70px;
        height: 70px;
        border-radius: 50%;
        box-shadow: 0 2px 8px rgba(37,99,235,0.08);
        margin-right: 1rem;
        background: #fff;
        object-fit: cover;
        border: 2px solid #dbeafe;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo y título
st.markdown(
    '''
    <div class="logo-container">
        <img src="https://www.shutterstock.com/image-vector/chat-bot-icon-virtual-smart-600nw-2478937553.jpg" class="logo-img" alt="Gym Logo" />
        <span style="font-size:2.2rem; color:#2563eb; font-weight:700;">Gym Assistant Bot</span>
    </div>
    ''', unsafe_allow_html=True
)

# Cargar y procesar datos
st.write("Cargando datos...")
data = None
try:
    config = load_config()
    data = config.get('data', [])
    if data:
        st.success("Datos cargados correctamente.")
    else:
        st.warning("No se encontraron datos en la configuración.")
except Exception as e:
    st.error(f"Error al cargar los datos: {e}")

# Inicializar vector store si hay datos
vector_store = None
if data:
    try:
        st.write("Inicializando vector store...")
        vector_store = initialize_vector_store(data)
        st.success("Vector store inicializado correctamente.")
    except Exception as e:
        st.error(f"Error al inicializar el vector store: {e}")
else:
    st.error("No se puede inicializar el vector store sin datos válidos.")

# Inicializar historial en la sesión
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    role = msg.get('role', 'user')
    content = msg.get('content', '')
    if role == 'user':
        st.markdown(f'<div class="chat-message user-message"><b>You:</b> {content}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-message bot-message"><b>Bot:</b> {content}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Input del usuario
user_input = st.chat_input("Type your message...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    # Aquí podrías agregar la lógica para obtener la respuesta del bot
    bot_response = "I'm a helpful gym assistant! (Bot response)"
    st.session_state.messages.append({"role": "bot", "content": bot_response})