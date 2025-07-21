import requests
import json
import os
import pyfiglet
import random
import time
from rich.console import Console
from rich.theme import Theme
from rich.text import Text

# === Config ===
LM_STUDIO_API_URL = os.getenv("LM_STUDIO_API_URL", "http://localhost:1234/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "liquid/lfm2-1.2b")

# === Rich Theme ===
custom_theme = Theme({
    "banner": "bold magenta",
    "info": "cyan",
    "label": "bold bright_green",
    "user": "bold yellow",
    "kira": "bold magenta",
    "error": "bold red"
})
console = Console(theme=custom_theme)

# === Terminal Effects ===
def glitch_text(text):
    glitched = ''.join(c + (random.choice(['', '', '', '.', '*', '~']) if c != ' ' else ' ')
                       for c in text)
    return glitched

def slow_type(text, speed=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()

# === KIRA ASCII Logo ===
def print_banner():
    banner = pyfiglet.figlet_format("KIRA", font="slant")
    console.print(banner, style="banner")
    console.print("⚡ [label]Knowledge Integration & Response Agent v1.3[/]")
    console.print("💬 [label]Type your message below. Type 'exit' to disconnect.[/]\n")

# === Talk to LM Studio with Token Streaming ===
def get_kira_response(prompt, history=[]):
    headers = {
        "Content-Type": "application/json",
    }

    messages = [
        {
            "role": "system",
            "content": (
                "Your name is KIRA.\n"
                "Your version is 1.3.\n"
                "Your creator is Alan Cyril Sunny.\n"
                "You are based on the model liquid/lfm2-1.2b."
            )
        }
    ]
    for human_message, ai_message in history:
        messages.append({"role": "user", "content": human_message})
        messages.append({"role": "assistant", "content": ai_message})
    messages.append({"role": "user", "content": prompt})

    data = {
        "model": MODEL_NAME,
        "messages": messages,
        "temperature": 0.7,
        "stream": True,
    }

    try:
        with requests.post(
            f"{LM_STUDIO_API_URL}/chat/completions",
            headers=headers,
            data=json.dumps(data),
            stream=True
        ) as response:
            response.raise_for_status()
            collected = ""
            console.print("\n[kira]KIRA >[/] ", end="", highlight=False)
            for line in response.iter_lines(decode_unicode=True):
                if line.startswith("data: "):
                    data_str = line[6:].strip()
                    if data_str == "[DONE]" or not data_str:
                        continue
                    try:
                        chunk = json.loads(data_str)
                        delta = chunk["choices"][0]["delta"].get("content", "")
                        collected += delta
                        print(delta, end="", flush=True)
                        time.sleep(0.005)
                    except json.JSONDecodeError:
                        continue
            print()
            return collected
    except requests.exceptions.RequestException as e:
        return f"[error][ERROR][/error] Communication failure: {e}"

# === Main Loop ===
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()

    chat_history = []

    while True:
        try:
            user_input = console.input("[user]You > [/]")
            if user_input.strip().lower() == 'exit':
                console.print("\n[kira]KIRA >[/] Disconnecting... [italic]May the shadows keep you safe.[/italic]")
                break

            response = get_kira_response(user_input, chat_history)
            chat_history.append((user_input, response))

        except KeyboardInterrupt:
            console.print("\n[error][!] Forced exit by Operator. KIRA shutting down.[/error]")
            break

if __name__ == "__main__":
    main()
