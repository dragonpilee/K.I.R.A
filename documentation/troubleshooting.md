# Terminal Chatbot Troubleshooting Guide

This guide provides general troubleshooting tips for common issues you might encounter while using the terminal chatbot. For more specific issues related to your operating system, please refer to the [Windows 11 Setup Guide](windows_setup_guide.md) or [Linux Mint Setup Guide](linux_setup_guide.md).

## Common Issues and Solutions:

### 1. Error: "Error communicating with LM Studio"
   - **Cause:** The chatbot cannot connect to the LM Studio local inference server.
   - **Solutions:**
     - **Verify LM Studio is Running:** Ensure LM Studio is open and the local inference server is actively running with the LFM2 model loaded.
     - **Check API URL:** Confirm that the `LM_STUDIO_API_URL` environment variable (or the default in `chatbot.py`) matches the actual API URL displayed in LM Studio (usually `http://localhost:1234`).
     - **Firewall:** Check if your firewall is blocking the connection to LM Studio. You might need to create an exception for LM Studio or its port.

### 2. Slow Performance or High CPU Usage:
   - **Cause:** The LFM2 model is not fully utilizing your RTX 2050 GPU, or the model is too large for your available VRAM.
   - **Solutions:**
     - **Maximize GPU Offloading:** In LM Studio, ensure the "GPU Offload" slider is set to its maximum value (e.g., -1) to push as many layers as possible to your RTX 2050.
     - **Update NVIDIA Drivers:** Make sure your NVIDIA graphics drivers are up to date.
     - **Choose Smaller Model:** Consider downloading a smaller LFM2 model variant (e.g., 350M or 700M) or a more aggressively quantized version (e.g., Q4_K_M) from LM Studio.
     - **Monitor GPU Usage:** Use `nvidia-smi` (Linux) or Task Manager (Windows) to verify that your RTX 2050 is being utilized during inference.

### 3. Python Errors (e.g., `ModuleNotFoundError`):
   - **Cause:** Required Python libraries are not installed.
   - **Solutions:**
     - **Install `requirements.txt`:** Navigate to your `chatbot_project` directory in the terminal and run `pip install -r requirements.txt` (or `pip3 install -r requirements.txt` on Linux).
     - **Correct Python Version:** Ensure you are using Python 3.8 or newer.

### 4. Chatbot Not Responding or Crashing:
   - **Cause:** Various issues, including invalid model responses, unexpected input, or resource exhaustion.
   - **Solutions:**
     - **Restart Chatbot and LM Studio:** Sometimes, simply restarting both the chatbot and LM Studio can resolve transient issues.
     - **Check LM Studio Logs:** LM Studio often provides detailed logs that can help identify the root cause of model-related issues.
     - **Simplify Prompt:** Try a simpler prompt to see if the issue is related to complex input.

If you continue to experience issues, please consult the specific setup guide for your operating system or seek assistance from relevant online communities.

