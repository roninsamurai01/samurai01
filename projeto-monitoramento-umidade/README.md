# 🌦️ Projeto: Monitoramento Ambiental com Simulação de Dados

## 🎯 Objetivo
Simular um sistema de monitoramento ambiental em tempo real, exibindo informações como:
- Umidade
- Temperatura
- Sensação térmica
- Vento
- Precipitação

Com visualização em gráficos e alertas inteligentes, integrado a um site WordPress.

---

## 🛠️ Ferramentas Utilizadas

- Python 3.13.1
- [Streamlit](https://streamlit.io)
- VSCode
- WordPress (para incorporar via `<iframe>`)
- Navegador (para auto atualização via HTML)

---

## 🚀 Como Executar Localmente

1. Instale as dependências:

```bash
pip install streamlit pandas
```

2. Execute o aplicativo:

```bash
streamlit run app.py
```

3. O app será aberto automaticamente no navegador.

---

## 🔁 Atualização Automática

O app utiliza o recurso HTML:

```html
<meta http-equiv="refresh" content="10">
```

Esse comando recarrega a página automaticamente a cada 10 segundos, permitindo simular dados em tempo real **sem usar bibliotecas externas**.

---

## 🌍 Como Publicar com Streamlit Cloud (Gratuito)

1. Suba o projeto no GitHub.
2. Acesse: https://streamlit.io/cloud
3. Conecte sua conta GitHub e selecione o repositório.
4. Defina `app.py` como arquivo principal e clique em **Deploy**.

---

## 🌐 Como Incorporar no WordPress

No painel do WordPress, adicione um bloco HTML com o seguinte código:

```html
<iframe src="https://SEU_APP.streamlit.app" width="100%" height="700" frameborder="0"></iframe>
```

Substitua o link pelo gerado na Streamlit Cloud.

---

## 🧠 Extensões Futuras

- Conectar sensores físicos reais (IoT)
- Enviar alertas por e-mail ou WhatsApp
- Armazenar dados em CSV ou banco de dados

---

## 📍 Local do Projeto

**Escola Vivendo e Aprendendo – 604 Norte, Brasília – DF**  
**Coordenadas:** -15.7833, -47.9167

---
