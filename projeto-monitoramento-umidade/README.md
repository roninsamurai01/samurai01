# Projeto: Monitoramento de Umidade com Alerta Inteligente

## Objetivo
Monitorar a umidade do ambiente escolar e exibir alertas e gráficos em tempo real.

## Ferramentas
- Python 3.13.1
- Streamlit
- GitHub
- Streamlit Cloud
- WordPress (para embutir o app com iframe)

## Como Rodar Localmente
1. Instale as dependências:
```bash
pip install -r requisitos.txt
```

2. Execute o app:
```bash
streamlit run app.py
```

## Como Publicar Online com Streamlit Cloud
1. Crie um repositório no GitHub e envie esses arquivos.
2. Acesse https://streamlit.io/cloud, conecte sua conta do GitHub.
3. Escolha o repositório e deploye o app.
https://samurai-projetomonitoramento.streamlit.app
## Como Integrar no WordPress
1. Copie este código e cole em um bloco HTML do WordPress:

```html
<iframe src="https://samurai-projetomonitoramento.streamlit.app" width="100%" height="600" frameborder="0"></iframe>
```
