from model_loader import ModelLoader
from chat_memory import ChatMemory
import textwrap

class ChatbotInterface:
    def __init__(self, model_name="google/gemma-2b-it", memory_window=4):  
        self.model_loader = ModelLoader(model_name)
        self.memory = ChatMemory(memory_window)
        self.is_running = False
        
    def setup(self):
        """Initialize the chatbot"""
        print("ATG Technical Assignment - Local Chatbot")
        print("=" * 50)
        print(f"Model: {self.model_loader.model_name}")
        print(f"Memory window: {self.memory.window_size} exchanges")
        print("=" * 50)
        
        # Load model
        if not self.model_loader.load_model():
            print("Failed to load model. Trying fallback...")
            self.model_loader.model_name = "microsoft/DialoGPT-medium"
            if not self.model_loader.load_model():
                return False
            
        print("Commands:")
        print("  /exit   - Quit the chatbot")
        print("  /clear  - Clear conversation memory") 
        print("  /history - Show conversation history")
        print("-" * 50)
        return True
    
    def format_response(self, response):
        """Format the bot response for better readability"""
        if not response:
            return "Bot: (No response generated)"
            
        wrapped_response = textwrap.fill(
            response, 
            width=70, 
            subsequent_indent='    ',
            break_long_words=False,
            break_on_hyphens=False
        )
        return wrapped_response
    
    def process_user_input(self, user_input):
        """Process user input and generate response"""
        if user_input.lower() == '/exit':
            return None
            
        if user_input.lower() == '/clear':
            self.memory.clear_history()
            print("Memory cleared!")
            return ""
        
        if user_input.lower() == '/history':
            history = self.memory.get_context()
            if history:
                print("\nConversation History:")
                print("-" * 40)
                print(history)
                print("-" * 40)
            else:
                print("No conversation history yet.")
            return ""
        
        # Generate response
        conversation_history = self.memory.get_conversation_history()
        response = self.model_loader.generate_response(user_input, conversation_history)
        
        # Update memory
        if response and not response.startswith("Error"):
            self.memory.add_exchange(user_input, response)
        
        return response
    
    def run_chat(self):
        """Main chat loop"""
        if not self.setup():
            return
            
        self.is_running = True
        print("\nChat started! Type your message below:\n")
        
        while self.is_running:
            try:
                # Get user input
                user_input = input("User: ").strip()
                
                if not user_input:
                    continue
                
                # Process input
                response = self.process_user_input(user_input)
                
                # Handle exit command
                if response is None:
                    break
                
                # Print bot response if not empty
                if response and not response.startswith("Error"):
                    formatted_response = self.format_response(response)
                    print(f"Bot: {formatted_response}\n")
                elif response.startswith("Error"):
                    print(f"{response}\n")
                elif not response:
                    print("Bot: (No response generated)\n")
                    
            except KeyboardInterrupt:
                print("\n\nInterrupted by user.")
                break
            except Exception as e:
                print(f"\nUnexpected error: {e}")
                continue
        
        print("\nExiting chatbot. Goodbye!")

def main():
    chatbot = ChatbotInterface(
        model_name="Qwen/Qwen1.5-0.5B-Chat",
        memory_window=4
    )
    chatbot.run_chat()
if __name__ == "__main__":
    main()