import speech_recognition as sr
import pyttsx3
import requests
import subprocess
import pyautogui
import datetime
import time

# ========================================
# AURA + GROQ (PERFEITO!)
# ========================================
GROQ_API_KEY = "SUA API AQUI"  # console.groq.com/keys

voz = pyttsx3.init()
voz.setProperty('rate', 170)
voz.setProperty('volume', 0.9)

# CORRIGIDO: energy_threshold como parâmetro
rec = sr.Recognizer()
rec.energy_threshold = 450  # ← ASSIM CORRETO!

print("🚀 AURA ")

# ========================================
# GROQ AI
# ========================================
def groq_responder(pergunta):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "messages": [{"role": "user", "content": pergunta}],
        "model": "llama-3.1-8b-instant",
        "stream": False,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            texto = data['choices'][0]['message']['content'].strip()
            if len(texto) > 120:
                texto = texto[:115] + "..."
            falar(texto)
            print(f"✅ {texto}")
            return True
        else:
            print(f"❌ {response.text}")
            falar("Erro Groq")
    except Exception as e:
        print(f"❌ {e}")
        falar("Sem conexão")
    return False

# ========================================
# FUNÇÕES
# ========================================
def falar(texto):
    print(f"✨ Aura: {texto}")
    voz.say(texto)
    voz.runAndWait()

def ouvir():
    try:
        print("🎤 Aura...")
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic, 0.3)
            audio = rec.listen(mic, timeout=4, phrase_time_limit=4)
        cmd = rec.recognize_google(audio, language='pt-BR')
        print(f"✅ '{cmd}'")
        return cmd.lower()
    except:
        return ""

def abrir_app(nome):
    apps = {"calc": "calc", "chrome": "chrome", "bloco": "notepad"}
    nome = nome.replace("abre ", "").replace("abrir ", "")
    try:
        subprocess.Popen(nome)
        falar(f"{nome}!")
    except:
        falar("Erro app")

# ========================================
# EXECUTAR
# ========================================
def executar(comando):
    print(f"🔍 '{comando}'")
    
    if "?" in comando or "quem" in comando or "como" in comando:
        groq_responder(comando)
    elif "abre" in comando:
        abrir_app(comando)
    elif "screenshot" in comando:
        pyautogui.screenshot(f"groq_{int(time.time())}.png")
        falar("Screenshot!")
    elif "hora" in comando:
        agora = datetime.datetime.now().strftime("%H:%M")
        falar(f"São {agora}")
    else:
        falar("Pergunte ou abra app")

# ========================================
# LOOP PRINCIPAL
# ========================================
falar("Aura ativada!")
print("\n🎯 Funções:")
print("• Perguntas")
print("• Abre Apps\n")

while True:
    cmd = ouvir()
    if "aura" in cmd:
        falar("Sim?")
        novo = ouvir()
        if novo:
            executar(novo)
    elif "sair" in cmd:
        falar("Tchau!")
        break