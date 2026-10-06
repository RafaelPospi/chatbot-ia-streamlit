# python -m streamlit run codigo.py ( para rodar o codigo)

# 1- Importação das bibliotecas

import streamlit as st
from openai import OpenAI

# 2 - Configuração do modelo

modelo_ia = OpenAI(
        api_key="Sua Chave Api Aqui",
        base_url="https://generativelanguage.googleapis.com/v1beta/openai"
        )

# 3 - Criação do título

st.write("## ChatBot de IA")

# 4 - Criação do histórico

if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# 5 - Entrada do usuário

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui...")

# 6 - Exibição do histórico

for mensagem in st.session_state["lista_mensagens"]:
    quem_enviou = mensagem["role"]
    texto_mensagem = mensagem["content"]

    st.chat_message(quem_enviou).write(texto_mensagem)

# 7 - Envio da mensagem

if mensagem_usuario:
    st.chat_message("user").write(mensagem_usuario)
    mensagem1 = {
        "role":"user",
        "content":mensagem_usuario
        }
    st.session_state["lista_mensagens"].append(mensagem1)

# 8 - Comunicação com a Inteligência Artificial

    resposta_modelo = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gemini-flash-lite-latest"
    )

# 9  Obtendo a resposta

    resposta_ia = resposta_modelo.choices[0].message.content

    st.chat_message("assistant").write(resposta_ia)

# 10 - Salvando a resposta

    mensagem2 = {
        "role":"assistant",    
        "content": resposta_ia
        }
    st.session_state["lista_mensagens"].append(mensagem2)
