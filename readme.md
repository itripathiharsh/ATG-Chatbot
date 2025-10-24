ATG Technical Assignment - Local Chatbot

Model: Qwen/Qwen1.5-0.5B-Chat
Memory window: 4 exchanges

Commands:
  /exit   - Quit the chatbot
  /clear  - Clear conversation memory
  /history - Show conversation history


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



How It Works

Model Loading:
Uses Hugging Face pipeline for efficient model management
Automatically handles tokenization and generation
Supports both CPU and GPU inference

Memory Management:
Implements sliding window mechanism
Maintains context across multiple conversation turns
Prevents infinite memory growth while preserving recent context

Text Generation:
Optimized generation parameters for conversational AI
Temperature: 0.7 (balanced creativity vs consistency)
Top-p sampling: 0.9 (nucleus sampling)
Repetition penalty: 1.1 (prevents looping)

Performance:
Model Size: 1.24GB (Qwen1.5-0.5B-Chat)
Memory Usage: ~2GB RAM during inference
Response Time: 2-5 seconds on CPU
Context Window: 4 conversation exchanges