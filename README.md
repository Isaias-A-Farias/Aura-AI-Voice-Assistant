# 🎙️ Aura: Assistente de Voz com IA (Llama 3)

Aura é um projeto de assistente virtual desenvolvido em Python. Ela utiliza reconhecimento de voz para captar comandos, processa a inteligência através da API da Groq (Llama 3.1) e responde por voz, além de executar automações no Windows.

## 🚀 Funcionalidades
- **Respostas Inteligentes:** Integração com o modelo Llama-3.1 via Groq Cloud.
- **Comandos de Voz:** Reconhecimento em Português (pt-BR).
- **Automação de Apps:** Abre aplicativos como Bloco de Notas, Chrome e Calculadora.
- **Utilidades:** Captura de screenshots e anúncio da hora atual.

## 🛠️ Tecnologias Utilizadas
- [Python](https://www.python.org/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) (Google Web Speech API)
- [Pyttsx3](https://pypi.org/project/pyttsx3/) (Síntese de voz offline)
- [Groq API](https://groq.com/) (LLM de baixa latência)
- [PyAutoGUI](https://pyautogui.readthedocs.io/) (Automação de interface)

## 🔧 Como Rodar o Projeto
1. Instale as dependências:
   ```bash
   pip install speech_recognition pyttsx3 requests pyautogui python-dotenv
