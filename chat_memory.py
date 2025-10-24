class ChatMemory:
    def __init__(self, window_size=4):
        self.window_size = window_size
        self.conversation_history = []
        
    def add_exchange(self, user_input, bot_response):
        self.conversation_history.append({
            'user': user_input,
            'bot': bot_response
        })
        
        if len(self.conversation_history) > self.window_size:
            self.conversation_history = self.conversation_history[-self.window_size:]
    
    def get_conversation_history(self):
        return self.conversation_history
    
    def get_context(self):
        if not self.conversation_history:
            return ""
        
        context = ""
        for i, exchange in enumerate(self.conversation_history, 1):
            context += f"Turn {i}:\n"
            context += f"  User: {exchange['user']}\n"
            context += f"  Bot: {exchange['bot']}\n\n"
        
        return context.strip()
    
    def clear_history(self):
        self.conversation_history = []
    
    def get_history_length(self):
        return len(self.conversation_history)