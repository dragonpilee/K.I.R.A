# Terminal Chatbot Setup Guide for Windows 11

This guide will walk you through setting up the terminal chatbot on your Windows 11 system, integrating it with LM Studio and leveraging your RTX 2050 GPU.

## Prerequisites:
1.  **Windows 11:** Ensure you have Windows 11 installed.
2.  **NVIDIA RTX 2050 GPU:** The chatbot is optimized for NVIDIA RTX GPUs. Ensure your NVIDIA drivers are up to date.
3.  **Python 3.8+:** Download and install Python 3.8 or newer from [python.org](https://www.python.org/downloads/windows/). Make sure to check the option "Add Python to PATH" during installation.
4.  **LM Studio:** Download and install LM Studio from [lmstudio.ai](https://lmstudio.ai/).

## Step-by-Step Setup:

### 1. Install LM Studio and Download LFM2 Model:
   a. Download and install LM Studio from the official website.
   b. Open LM Studio. Navigate to the "Search" tab.
   c. Search for `lfm2-1.2b` (or a smaller variant like `lfm2-700m` if you experience performance issues).
   d. Download the desired LFM2 model. It is recommended to choose a quantized version (e.g., Q4_K_M) for better performance on RTX 2050.

### 2. Configure LM Studio for GPU Acceleration:
   a. In LM Studio, go to the "Local Inference Server" tab (usually represented by a chat bubble icon).
   b. Load the LFM2 model you downloaded.
   c. In the right-hand sidebar, locate the "GPU Offload" slider. Drag it all the way to the right (or set it to -1) to offload as many layers as possible to your RTX 2050 GPU.
   d. Ensure that the CUDA backend is selected if available. LM Studio typically auto-detects and uses CUDA for NVIDIA GPUs.
   e. Start the local inference server by clicking the "Start Server" button.
   f. Note the API URL, which is usually `http://localhost:1234`.

### 3. Set up the Chatbot Project:
   a. Create a directory for your chatbot project, for example, `C:\chatbot_project`.
   b. Download the `chatbot.py` and `requirements.txt` files into this directory.

### 4. Install Python Dependencies:
   a. Open PowerShell or Command Prompt.
   b. Navigate to your chatbot project directory:
      ```bash
      cd C:\chatbot_project
      ```
   c. Install the required Python libraries:
      ```bash
      pip install -r requirements.txt
      ```

### 5. Run the Chatbot:
   a. Ensure LM Studio's local inference server is running with the LFM2 model loaded.
   b. In your PowerShell or Command Prompt, run the chatbot:
      ```bash
      python chatbot.py
      ```
   c. If your LM Studio API URL is different from `http://localhost:1234`, you can set it as an environment variable before running:
      ```bash
      $env:LM_STUDIO_API_URL="http://your_lm_studio_ip:port"
      python chatbot.py
      ```
      (Replace `http://your_lm_studio_ip:port` with your actual LM Studio API URL).

## Troubleshooting:
- **"Error communicating with LM Studio":** Ensure LM Studio is running and the local inference server is started. Check if the API URL in `chatbot.py` (or `LM_STUDIO_API_URL` environment variable) matches your LM Studio's API URL.
- **Slow Performance:** Verify that GPU offloading is maximized in LM Studio. Consider downloading a smaller or more quantized LFM2 model.
- **Python not found:** Ensure Python is correctly installed and added to your system's PATH environment variable.


