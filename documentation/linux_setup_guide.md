# Terminal Chatbot Setup Guide for Linux Mint

This guide will walk you through setting up the terminal chatbot on your Linux Mint system, integrating it with LM Studio and leveraging your RTX 2050 GPU.

## Prerequisites:
1.  **Linux Mint:** Ensure you have Linux Mint installed (Ubuntu 20.04 or newer is required for LM Studio).
2.  **NVIDIA RTX 2050 GPU:** The chatbot is optimized for NVIDIA RTX GPUs. Ensure your NVIDIA drivers are up to date.
3.  **Python 3.8+:** Linux Mint typically comes with Python pre-installed. Verify by running `python3 --version` in the terminal.
4.  **LM Studio:** Download and install LM Studio from [lmstudio.ai](https://lmstudio.ai/).

## Step-by-Step Setup:

### 1. Install NVIDIA Drivers (if not already installed):
   a. Open a terminal.
   b. Update your package list:
      ```bash
      sudo apt update
      ```
   c. Install the NVIDIA driver:
      ```bash
      sudo apt install nvidia-driver-470
      ```
      (Replace `470` with the latest available driver version if needed).
   d. Reboot your system:
      ```bash
      sudo reboot
      ```
   e. Verify the installation by running:
      ```bash
      nvidia-smi
      ```
      This should display information about your RTX 2050 GPU.

### 2. Install LM Studio:
   a. Download the LM Studio AppImage from the official website.
   b. Make the AppImage executable:
      ```bash
      chmod +x LMStudio-*.AppImage
      ```
   c. Run LM Studio:
      ```bash
      ./LMStudio-*.AppImage
      ```

### 3. Download LFM2 Model in LM Studio:
   a. Open LM Studio. Navigate to the "Search" tab.
   b. Search for `lfm2-1.2b` (or a smaller variant like `lfm2-700m` if you experience performance issues).
   c. Download the desired LFM2 model. It is recommended to choose a quantized version (e.g., Q4_K_M) for better performance on RTX 2050.

### 4. Configure LM Studio for GPU Acceleration:
   a. In LM Studio, go to the "Local Inference Server" tab.
   b. Load the LFM2 model you downloaded.
   c. In the right-hand sidebar, locate the "GPU Offload" slider. Drag it all the way to the right (or set it to -1) to offload as many layers as possible to your RTX 2050 GPU.
   d. Ensure that the CUDA backend is selected if available. LM Studio typically auto-detects and uses CUDA for NVIDIA GPUs.
   e. Start the local inference server by clicking the "Start Server" button.
   f. Note the API URL, which is usually `http://localhost:1234`.

### 5. Set up the Chatbot Project:
   a. Create a directory for your chatbot project:
      ```bash
      mkdir ~/chatbot_project
      cd ~/chatbot_project
      ```
   b. Download the `chatbot.py` and `requirements.txt` files into this directory.

### 6. Install Python Dependencies:
   a. Install pip if not already installed:
      ```bash
      sudo apt install python3-pip
      ```
   b. Install the required Python libraries:
      ```bash
      pip3 install -r requirements.txt
      ```

### 7. Run the Chatbot:
   a. Ensure LM Studio's local inference server is running with the LFM2 model loaded.
   b. In your terminal, run the chatbot:
      ```bash
      python3 chatbot.py
      ```
   c. If your LM Studio API URL is different from `http://localhost:1234`, you can set it as an environment variable before running:
      ```bash
      export LM_STUDIO_API_URL="http://your_lm_studio_ip:port"
      python3 chatbot.py
      ```
      (Replace `http://your_lm_studio_ip:port` with your actual LM Studio API URL).

## Troubleshooting:
- **"Error communicating with LM Studio":** Ensure LM Studio is running and the local inference server is started. Check if the API URL in `chatbot.py` (or `LM_STUDIO_API_URL` environment variable) matches your LM Studio's API URL.
- **Slow Performance:** Verify that GPU offloading is maximized in LM Studio. Consider downloading a smaller or more quantized LFM2 model. Use `nvidia-smi` to monitor GPU utilization.
- **Python not found:** Use `python3` instead of `python` on Linux systems.
- **Permission denied for AppImage:** Ensure the LM Studio AppImage has execute permissions (`chmod +x LMStudio-*.AppImage`).

