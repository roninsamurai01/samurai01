import streamlit as st
import pandas as pd
import random
import time
from streamlit_autorefresh import st_autorefresh

# Configuração da página
st.set_page_config(page_title="Monitoramento Ambiental", layout="centered")

# Cabeçalho
st.title("🌦️ Monitoramento Ambiental em Tempo Real")
st.markdown("📍 **Local:** Escola Vivendo e Aprendendo - 604 Norte, Brasília - DF")
st.markdown("🗺️ **Coordenadas:** -15.7833, -47.9167")

# Atualiza a página automaticamente a cada 10 segundos
count = st_autorefresh(interval=10 * 1000, limit=None, key="refresh")

# Inicializa os dados na sessão
if 'dados' not in st.session_state:
    st.session_state.dados = pd.DataFrame(columns=["Tempo", "Umidade", "Temperatura", "Sensação Térmica", "Vento", "Precipitação"])

# Função para simular dados ambientais
def gerar_dados():
    tempo = time.strftime("%H:%M:%S")
    umidade = round(random.uniform(20, 60), 2)
    temperatura = round(random.uniform(20, 35), 1)
    sensacao = temperatura + random.uniform(-2, 2)
    vento = round(random.uniform(0, 15), 1)
    precipitacao = round(random.uniform(0, 10), 2)
    return {
        "Tempo": tempo,
        "Umidade": umidade,
        "Temperatura": temperatura,
        "Sensação Térmica": round(sensacao, 1),
        "Vento": vento,
        "Precipitação": precipitacao
    }

# Adiciona nova linha aos dados
novo_dado = gerar_dados()
st.session_state.dados = pd.concat([st.session_state.dados, pd.DataFrame([novo_dado])], ignore_index=True)

# Exibir métricas
col1, col2, col3 = st.columns(3)
col1.metric("🌡️ Temperatura", f"{novo_dado['Temperatura']}°C")
col2.metric("💧 Umidade", f"{novo_dado['Umidade']}%")
col3.metric("🌬️ Vento", f"{novo_dado['Vento']} km/h")

col4, col5, col6 = st.columns(3)
col4.metric("🥵 Sensação", f"{novo_dado['Sensação Térmica']}°C")
col5.metric("☔ Precipitação", f"{novo_dado['Precipitação']} mm")
if novo_dado['Umidade'] < 30:
    col6.error("⚠️ Umidade muito baixa!")

# Gráficos de linha para os dados
st.subheader("📈 Histórico Ambiental")
st.line_chart(st.session_state.dados.set_index("Tempo"))
