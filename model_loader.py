from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

class ModelLoader:
    def __init__(self, model_name="google/gemma-2b-it"):
        self.model_name = model_name
        self.tokenizer = None
        self.model = None
        self.pipeline = None
        
    def load_model(self):
        try:
            print(f"Loading model {self.model_name}...")
            
            self.pipeline = pipeline(
                "text-generation",
                model=self.model_name,
                device=-1, 
                dtype=torch.float32
            )
            
            print("Model loaded successfully!")
            return True
            
        except Exception as e:
            print(f"Error loading model {self.model_name}: {e}")
            return False
    
    def generate_response(self, user_input, conversation_history=None):
        if self.pipeline is None:
            return "Error: Model not loaded"
        
        try:
            if conversation_history and len(conversation_history) > 0:
                messages = []
                for exchange in conversation_history[-3:]:  
                    messages.append({"role": "user", "content": exchange['user']})
                    messages.append({"role": "assistant", "content": exchange['bot']})
                messages.append({"role": "user", "content": user_input})
                
                prompt = self.pipeline.tokenizer.apply_chat_template(
                    messages, 
                    tokenize=False, 
                    add_generation_prompt=True
                )
            else:
                
                messages = [{"role": "user", "content": user_input}]
                prompt = self.pipeline.tokenizer.apply_chat_template(
                    messages, 
                    tokenize=False, 
                    add_generation_prompt=True
                )
            
            outputs = self.pipeline(
                prompt,
                max_new_tokens=150,
                temperature=0.3, 
                do_sample=True,
                top_p=0.9,
                repetition_penalty=1.1,
                num_return_sequences=1
            )
            
            generated_text = outputs[0]['generated_text']
            
            if "<start_of_turn>model\n" in generated_text:
                response = generated_text.split("<start_of_turn>model\n")[-1].strip()
            elif "assistant\n" in generated_text:
                response = generated_text.split("assistant\n")[-1].strip()
            else:
                response = generated_text[len(prompt):].strip()
            
            response = response.split("<end_of_turn>")[0].strip()
            response = response.split("\nUser:")[0].strip()
            response = response.split("\n\n")[0].strip()
            
            return response
            
        except Exception as e:
            return f"Error: {e}"