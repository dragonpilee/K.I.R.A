# Terminal Chatbot User Manual

This manual provides instructions on how to use the terminal chatbot after it has been successfully set up with LM Studio.

## Running the Chatbot:
To start the chatbot, open your terminal (Command Prompt/PowerShell on Windows, or any terminal on Linux) and navigate to the `chatbot_project` directory. Then, run the following command:

```bash
python chatbot.py
```

If you are on Linux, you might need to use `python3`:

```bash
python3 chatbot.py
```

If your LM Studio API is running on a different address or port than the default `http://localhost:1234`, you can specify it using an environment variable:

**Windows (PowerShell):**
```powershell
$env:LM_STUDIO_API_URL="http://your_lm_studio_ip:port"
python chatbot.py
```

**Linux (Bash/Zsh):**
```bash
export LM_STUDIO_API_URL="http://your_lm_studio_ip:port"
python3 chatbot.py
```

## Interacting with the Chatbot:
Once the chatbot starts, you will see a welcome message and a prompt `You: `.

- **To chat:** Type your message after the `You: ` prompt and press Enter. The chatbot will send your message to LM Studio, and the LFM2 model will generate a response, which will then be displayed in the terminal.

- **Conversation History:** The chatbot maintains a conversation history, allowing for multi-turn dialogues. The model will consider previous turns when generating new responses.

- **To exit:** Type `exit` (case-insensitive) at the `You: ` prompt and press Enter. The chatbot will close.

## Example Interaction:

```
Welcome to the Terminal Chatbot!
Using LM Studio API at: http://localhost:1234
Using model: liquid/lfm2-1.2b
Type 'exit' to quit.

You: Hello, how are you today?
AI: I am an AI, I do not have feelings, but I am ready to assist you.
You: Can you tell me a story?
AI: Once upon a time, in a land far away...
You: exit
Exiting chatbot. Goodbye!
```

Enjoy your conversation with the LFM2 model!

