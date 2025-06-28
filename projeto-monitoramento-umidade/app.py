import streamlit as st
import pandas as pd
import requests
import time

# Configuração da página
st.set_page_config(page_title="Monitoramento Ambiental", layout="centered")

# Cabeçalho
st.title("🌦️ Monitoramento Ambiental em Tempo Real")
st.markdown("📍 **Local:** Escola Vivendo e Aprendendo - 604 Norte, Brasília - DF")
st.markdown("🗺️ **Coordenadas:** -15.7833, -47.9167")

# Sua API Key do OpenWeatherMap (substitua aqui)
API_KEY = "b8c6ada7e962ac3be2e0eb1343c0d928"

# Coordenadas da escola
LATITUDE = -15.7833
LONGITUDE = -47.9167

# Função para obter dados reais da API OpenWeatherMap
def obter_dados_clima():
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"lat={LATITUDE}&lon={LONGITUDE}&appid={API_KEY}&units=metric&lang=pt_br"
    )
    resposta = requests.get(url)
    
    if resposta.status_code != 200:
        st.error(f"Erro na API: Código {resposta.status_code} - {resposta.text}")
        return None

    dados = resposta.json()
    
    if 'main' not in dados:
        st.error(f"Resposta da API sem dados 'main': {dados}")
        return None

    temperatura = dados['main']['temp']
    umidade = dados['main']['humidity']
    vento = dados['wind']['speed'] * 3.6  # m/s para km/h
    sensacao = dados['main'].get('feels_like', temperatura)
    precipitacao = 0

    if 'rain' in dados and '1h' in dados['rain']:
        precipitacao = dados['rain']['1h']
    elif 'snow' in dados and '1h' in dados['snow']:
        precipitacao = dados['snow']['1h']

    return {
        "Temperatura": round(temperatura, 1),
        "Umidade": umidade,
        "Vento": round(vento, 1),
        "Sensação Térmica": round(sensacao, 1),
        "Precipitação": round(precipitacao, 2),
    }

# Atualiza automaticamente a cada 60 segundos
st.markdown(f'<meta http-equiv="refresh" content="60">', unsafe_allow_html=True)

# Inicializa os dados na sessão
if 'dados' not in st.session_state:
    st.session_state.dados = pd.DataFrame(columns=[
        "Tempo", "Umidade", "Temperatura", "Sensação Térmica", "Vento", "Precipitação"
    ])

# Obter dados reais da API
try:
    dados_atuais = obter_dados_clima()
except Exception as e:
    st.error(f"Erro ao obter dados da API: {e}")
    # Em caso de erro, usar valores simulados
    dados_atuais = {
        "Temperatura": 25.0,
        "Umidade": 50,
        "Vento": 5.0,
        "Sensação Térmica": 25.0,
        "Precipitação": 0,
    }

# Obter hora atual formatada
tempo_atual = time.strftime("%H:%M:%S")

# Montar o novo dado com timestamp
novo_dado = {
    "Tempo": tempo_atual,
    "Umidade": dados_atuais["Umidade"],
    "Temperatura": dados_atuais["Temperatura"],
    "Sensação Térmica": dados_atuais["Sensação Térmica"],
    "Vento": dados_atuais["Vento"],
    "Precipitação": dados_atuais["Precipitação"],
}

# Atualizar dados na sessão (acrescenta o novo)
st.session_state.dados = pd.concat(
    [st.session_state.dados, pd.DataFrame([novo_dado])],
    ignore_index=True
)

# Mostrar métricas
col1, col2, col3 = st.columns(3)
col1.metric("🌡️ Temperatura", f"{novo_dado['Temperatura']}°C")
col2.metric("💧 Umidade", f"{novo_dado['Umidade']}%")
col3.metric("🌬️ Vento", f"{novo_dado['Vento']} km/h")

col4, col5, col6 = st.columns(3)
col4.metric("🥵 Sensação", f"{novo_dado['Sensação Térmica']}°C")
col5.metric("☔ Precipitação", f"{novo_dado['Precipitação']} mm")

if novo_dado['Umidade'] < 30:
    col6.error("⚠️ Umidade muito baixa! Risco à saúde.")

# Gráfico histórico
st.subheader("📈 Histórico Ambiental")
st.line_chart(st.session_state.dados.set_index("Tempo"))





