# ATG Technical Assignment - Local Chatbot

A fully functional local chatbot interface built with Python and Hugging Face transformers. This project demonstrates the integration of language models into a CLI environment with conversational memory management using a sliding window mechanism.

## Features

- **Local Inference**: Runs completely offline using Hugging Face models
- **Conversational Memory**: Maintains context across 4 previous exchanges
- **Modular Architecture**: Clean, maintainable code structure
- **Dual Interfaces**: Both CLI and Streamlit web interface
- **Smart Model Selection**: Uses Qwen1.5-0.5B-Chat for optimal performance
- **Command Handling**: Built-in commands for conversation management

## Tech Stack

- **Python 3.7+**
- **Hugging Face Transformers**
- **PyTorch**
- **Streamlit** (for web interface)
- **Hugging Face Hub**

## Project Structure

```
chatbot/
├── model_loader.py      # Model loading and text generation
├── chat_memory.py       # Conversation memory management
├── interface.py         # CLI interface and main chat loop
├── app.py              # Streamlit web interface (optional)
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Quick Start

### Prerequisites

- Python 3.7 or higher
- 2GB+ RAM
- 2GB+ disk space for model caching

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd chatbot
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the CLI chatbot**
   ```bash
   python interface.py
   ```

### Optional: Streamlit Web Interface

1. **Install Streamlit**
   ```bash
   pip install streamlit
   ```

2. **Launch web interface**
   ```bash
   streamlit run app.py
   ```

## Usage

### CLI Interface

Start chatting immediately after running `python interface.py`:

```
ATG Technical Assignment - Local Chatbot
==================================================
Model: Qwen/Qwen1.5-0.5B-Chat
Memory window: 4 exchanges
==================================================
Commands:
  /exit   - Quit the chatbot
  /clear  - Clear conversation memory
  /history - Show conversation history
--------------------------------------------------

Chat started! Type your message below:

User: hi
Bot: Hello! How can I help you today? Is there something specific you would
    like to know or discuss? I'm here to provide information and
    answer any questions you may have.

User: what is capital of india
Bot: The capital of India is New Delhi, which is located in the northern
    part of the country.

User: /history
Conversation History:
Turn 1:
  User: hi
  Bot: Hello! How can I help you today? Is there something specific you would like to know or discuss? I'm here to provide information and answer any questions you may have.
Turn 2:
  User: what is capital of india
  Bot: The capital of India is New Delhi, which is located in the northern part of the country.

User: /exit
Exiting chatbot. Goodbye!
```

### Available Commands

- `/exit` - Gracefully terminate the chatbot
- `/clear` - Clear conversation history and memory
- `/history` - Display current conversation history

## Configuration

### Model Selection

The chatbot is configured to use `Qwen/Qwen1.5-0.5B-Chat` by default, which provides an excellent balance of performance and resource usage. To change the model, modify the `model_name` parameter in `interface.py`:

```python
def main():
    chatbot = ChatbotInterface(
        model_name="Your-Model-Name-Here",  # Change this
        memory_window=4
    )
```

### Memory Window Size

Adjust the conversation memory length by changing the `memory_window` parameter:

```python
def main():
    chatbot = ChatbotInterface(
        model_name="Qwen/Qwen1.5-0.5B-Chat",
        memory_window=6  # Keep last 6 exchanges
    )
```

## How It Works

### Model Loading
- Uses Hugging Face `pipeline` for efficient model management
- Automatically handles tokenization and generation
- Supports both CPU and GPU inference

### Memory Management
- Implements sliding window mechanism
- Maintains context across multiple conversation turns
- Prevents infinite memory growth while preserving recent context

### Text Generation
- Optimized generation parameters for conversational AI
- Temperature: 0.7 (balanced creativity vs consistency)
- Top-p sampling: 0.9 (nucleus sampling)
- Repetition penalty: 1.1 (prevents looping)

## 📊 Performance

- **Model Size**: 1.24GB (Qwen1.5-0.5B-Chat)
- **Memory Usage**: ~2GB RAM during inference
- **Response Time**: 2-5 seconds on CPU
- **Context Window**: 4 conversation exchanges

## Troubleshooting

### Common Issues

1. **Model loading fails**
   - Ensure internet connection for first-time download
   - Check available disk space (2GB+ required)
   - Verify Hugging Face token if using gated models

2. **Slow response times**
   - Close other memory-intensive applications
   - Consider using a smaller model
   - Ensure adequate RAM availability

3. **Memory errors**
   - Reduce `memory_window` size
   - Restart the application
   - Check system resource usage

### Logs and Debugging

Enable verbose logging by setting environment variables:
```bash
export TRANSFORMERS_VERBOSITY=info
python interface.py
```

## Future Enhancements

- [ ] GPU acceleration support
- [ ] Multiple model support with fallbacks
- [ ] Conversation export functionality
- [ ] Custom prompt templates
- [ ] Rate limiting and usage statistics
- [ ] Plugin system for extended functionality

## License

This project is created for the ATG Technical Assignment. Please refer to the specific licensing requirements of the Hugging Face models used in this application.

## Contributing

This is a technical assignment submission. For questions or issues, please refer to the assignment guidelines.

## Learning Outcomes

Through this project, I demonstrated:

- **Model Integration**: Successful local deployment of Hugging Face models
- **Memory Management**: Effective implementation of sliding window conversation memory
- **Software Architecture**: Modular, maintainable code structure
- **User Experience**: Intuitive CLI interface with helpful features
- **Problem Solving**: Iterative improvement from initial DialoGPT to optimal Qwen model

---
