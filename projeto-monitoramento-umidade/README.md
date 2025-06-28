# Projeto Monitoramento Ambiental - Escola Vivendo e Aprendendo

Este projeto consiste em um sistema de monitoramento ambiental em tempo real para a Escola Vivendo e Aprendendo, localizada na 604 Norte, Brasília - DF. Ele exibe dados reais de temperatura, umidade, vento, sensação térmica e precipitação, coletados via API OpenWeatherMap, com atualizações automáticas.

---

## Funcionalidades

- Consulta dados climáticos reais e atualizados para as coordenadas da escola.
- Exibição das principais métricas ambientais: temperatura, umidade, sensação térmica, vento e precipitação.
- Alerta visual para níveis críticos de umidade (abaixo de 30%).
- Gráfico histórico com as leituras feitas durante a execução do app.
- Atualização automática dos dados a cada 60 segundos.

---

## Tecnologias Utilizadas

- Python 3.13.1
- [Streamlit](https://streamlit.io/) para interface web interativa.
- [OpenWeatherMap API](https://openweathermap.org/api) para dados meteorológicos reais.
- Pandas para manipulação e organização dos dados.

---

## Como Usar

### 1. Pré-requisitos

- Python 3.13.1 instalado na máquina.
- Instalar as bibliotecas necessárias:
  
  ```bash
  pip install streamlit pandas requests

---
