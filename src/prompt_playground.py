import os
import json
from typing import List, Dict, Any
import openai

class PromptEngineeringPlayground:
    def __init__(self, api_key: str = None):
        """
        Initialize the Prompt Engineering Playground
        
        :param api_key: OpenAI API key for accessing GPT models
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key must be provided")
        
        openai.api_key = self.api_key
        
        self.prompting_techniques = {
            "Zero-Shot Prompting": self.zero_shot_prompting,
            "Few-Shot Prompting": self.few_shot_prompting,
            "Chain-of-Thought Prompting": self.chain_of_thought_prompting,
            "Role-Playing Prompting": self.role_playing_prompting,
            "Persona-Based Prompting": self.persona_based_prompting
        }
        
        # Ensure output directory exists
        os.makedirs("outputs", exist_ok=True)
    
    def zero_shot_prompting(self, prompt: str) -> str:
        """
        Demonstrate zero-shot prompting without any examples
        
        :param prompt: Input prompt
        :return: AI-generated response
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error in zero-shot prompting: {str(e)}"
    
    def few_shot_prompting(self, prompt: str, examples: List[Dict[str, str]] = None) -> str:
        """
        Demonstrate few-shot prompting with a few examples
        
        :param prompt: Input prompt
        :param examples: List of example interactions
        :return: AI-generated response
        """
        if examples is None:
            examples = [
                {"input": "Translate to French:", "output": "Bonjour, comment ça va?"},
                {"input": "Translate to Spanish:", "output": "Hola, ¿cómo estás?"}
            ]
        
        messages = [{"role": "system", "content": "You are a helpful translation assistant."}]
        
        # Add few-shot examples
        for example in examples:
            messages.append({"role": "user", "content": example["input"]})
            messages.append({"role": "assistant", "content": example["output"]})
        
        # Add current prompt
        messages.append({"role": "user", "content": prompt})
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error in few-shot prompting: {str(e)}"
    
    def chain_of_thought_prompting(self, problem: str) -> str:
        """
        Demonstrate chain-of-thought prompting for complex reasoning
        
        :param problem: Input problem requiring step-by-step reasoning
        :return: Detailed reasoning and solution
        """
        prompt = f"""Let's solve this problem step by step:
        {problem}

        Break down your reasoning into clear, logical steps:
        1. First, identify the key components of the problem.
        2. Then, outline the approach to solve it.
        3. Show the detailed calculation or reasoning.
        4. Provide the final solution.
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert problem solver who explains reasoning clearly."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error in chain-of-thought prompting: {str(e)}"
    
    def role_playing_prompting(self, role: str, task: str) -> str:
        """
        Demonstrate role-playing prompting by assigning a specific role
        
        :param role: The role the AI should assume
        :param task: The task to be completed
        :return: Response from the specified role
        """
        prompt = f"""
        You are a {role}. 
        Task: {task}
        
        Please respond as if you were truly in this role, using appropriate language, 
        expertise, and perspective of the assigned persona.
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are a {role}."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error in role-playing prompting: {str(e)}"
    
    def persona_based_prompting(self, persona: str, query: str) -> str:
        """
        Demonstrate persona-based prompting with specific characteristics
        
        :param persona: Description of the persona
        :param query: User's query
        :return: Response tailored to the persona
        """
        prompt = f"""
        You are a {persona}. 
        Consider your unique background, knowledge, and communication style.
        
        Respond to the following query:
        {query}
        
        Ensure your response reflects the specific perspective of this persona.
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are a {persona}"},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error in persona-based prompting: {str(e)}"
    
    def run_demonstration(self, technique: str, **kwargs) -> Dict[str, Any]:
        """
        Run a demonstration of a specific prompting technique
        
        :param technique: Name of the prompting technique
        :param kwargs: Parameters for the specific technique
        :return: Dictionary with technique details and result
        """
        if technique not in self.prompting_techniques:
            return {"error": f"Technique {technique} not found"}
        
        result = self.prompting_techniques[technique](**kwargs)
        
        # Save the demonstration
        demo_data = {
            "technique": technique,
            "input": kwargs,
            "output": result
        }
        
        # Save to a JSON file
        filename = f"outputs/{technique.lower().replace(' ', '_')}_demo.json"
        with open(filename, 'w') as f:
            json.dump(demo_data, f, indent=2)
        
        return demo_data

def main():
    """
    Main function to demonstrate the Prompt Engineering Playground
    """
    # Replace with your actual OpenAI API key or use environment variable
    api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")
    
    playground = PromptEngineeringPlayground(api_key)
    
    # Demonstrations of different prompting techniques
    demonstrations = [
        {
            "technique": "Zero-Shot Prompting",
            "params": {"prompt": "Explain quantum computing to a 5-year-old"}
        },
        {
            "technique": "Few-Shot Prompting",
            "params": {
                "prompt": "Translate to German:", 
                "examples": [
                    {"input": "Hello, how are you?", "output": "Hallo, wie geht es dir?"}
                ]
            }
        },
        {
            "technique": "Chain-of-Thought Prompting",
            "params": {"problem": "A train travels 120 miles in 2 hours. What is its speed?"}
        },
        {
            "technique": "Role-Playing Prompting",
            "params": {
                "role": "Shakespearean poet", 
                "task": "Write a sonnet about modern technology"
            }
        },
        {
            "technique": "Persona-Based Prompting",
            "params": {
                "persona": "A curious 10-year-old science enthusiast", 
                "query": "Explain how rockets work in space"
            }
        }
    ]
    
    # Run and store demonstrations
    results = []
    for demo in demonstrations:
        result = playground.run_demonstration(
            demo["technique"], 
            **demo["params"]
        )
        results.append(result)
    
    # Print results
    for result in results:
        print(f"Technique: {result.get('technique', 'N/A')}")
        print("Output:", result.get('output', 'No output'))
        print("---")

if __name__ == "__main__":
    main()