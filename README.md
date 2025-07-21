
# ⚡ KIRA - Knowledge Integration & Response Agent v1.3

![KIRA Banner](https://img.shields.io/badge/KIRA-v1.3-magenta?style=flat-square)
![Model](https://img.shields.io/badge/Model-liquid%2Flfm2--1.2b-blue?style=flat-square)
![Creator](https://img.shields.io/badge/Creator-Alan%20Cyril%20Sunny-green?style=flat-square)

> 🧠 A terminal-based AI assistant powered by `liquid/lfm2-1.2b` running on [LM Studio](https://lmstudio.ai). Built with love, `pyfiglet`, and `rich`, KIRA is a fast, elegant, and responsive local chatbot for hackers and enthusiasts.

---

## 🎯 Features

- 🧬 Identity-aware AI (Name: KIRA, Version: 1.3, Creator: Alan Cyril Sunny)
- 💬 Real-time token-by-token **streamed output**
- 🎨 Styled and colorful terminal UI using `rich`
- 🧠 Retains multi-turn conversation memory
- ⌨️ Terminal UX with glitchy effects and slow typing
- ⚙️ Fully configurable API and model settings

---

## 🛠️ Requirements

- Python 3.8+
- LM Studio running locally at `http://localhost:1234`
- Installed model: `liquid/lfm2-1.2b` or compatible

### 📦 Python Dependencies

```bash
pip install requests rich pyfiglet
```

---

## 🚀 Run the Bot

```bash
python kira.py
```

When KIRA launches, you'll see the stylized ASCII banner and be able to chat live in your terminal.

Type `'exit'` to gracefully disconnect.

---

## 🔧 Environment Variables (Optional)

| Variable            | Description                              | Default                      |
|---------------------|------------------------------------------|------------------------------|
| `LM_STUDIO_API_URL` | LM Studio API endpoint                   | `http://localhost:1234/v1`   |
| `MODEL_NAME`        | Model name used for completions          | `liquid/lfm2-1.2b`           |

---

## 📸 Demo

![KIRA Terminal UI](Screenshot.png)

---

## 📁 Project Structure

```
📦 kira-terminal-chatbot/
 ┣ kira.py                # Main chatbot script
 ┗ README.md              # Project README
```

---

## 🧠 Identity Prompt

KIRA is always aware of her identity:

```text
Your name is KIRA.
Your version is 1.3.
Your creator is Alan Cyril Sunny.
You are based on the model liquid/lfm2-1.2b.
```

---

## 🧑‍💻 Creator

**Alan Cyril Sunny**  
🔗 [GitHub](https://github.com/dragonpilee) | 📫 alancyrilsunny@protonmail.com

---

## 📜 License

MIT License. Free to use, modify, and share.

---

> ✨ “May the shadows keep you safe.” — KIRA
