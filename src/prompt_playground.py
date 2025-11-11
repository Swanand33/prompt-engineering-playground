import os
import json
from typing import List, Dict, Any
from openai import OpenAI
import tiktoken

class PromptEngineeringPlayground:
    def __init__(self, api_key: str = None):
        """
        Initialize the Prompt Engineering Playground

        :param api_key: OpenAI API key for accessing GPT models
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key must be provided")

        self.client = OpenAI(api_key=self.api_key)
        self.tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")
        
        self.prompting_techniques = {
            "Zero-Shot Prompting": self.zero_shot_prompting,
            "Few-Shot Prompting": self.few_shot_prompting,
            "Chain-of-Thought Prompting": self.chain_of_thought_prompting,
            "Role-Playing Prompting": self.role_playing_prompting,
            "Persona-Based Prompting": self.persona_based_prompting,
            "ReAct Prompting": self.react_prompting,
            "Self-Consistency Prompting": self.self_consistency_prompting,
            "Tree-of-Thoughts Prompting": self.tree_of_thoughts_prompting
        }
        
        # Ensure output directory exists
        os.makedirs("outputs", exist_ok=True)
    
    def zero_shot_prompting(self, prompt: str) -> Dict[str, Any]:
        """
        Demonstrate zero-shot prompting without any examples

        :param prompt: Input prompt
        :return: Dict with response, tokens, and cost
        """
        try:
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            result = response.choices[0].message.content
            tokens_used = response.usage.total_tokens
            cost = self.calculate_cost(tokens_used, "gpt-3.5-turbo")

            return {
                "response": result,
                "tokens": tokens_used,
                "cost": cost
            }
        except Exception as e:
            return {
                "response": f"Error in zero-shot prompting: {str(e)}",
                "tokens": 0,
                "cost": 0.0
            }
    
    def few_shot_prompting(self, prompt: str, examples: List[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        Demonstrate few-shot prompting with a few examples

        :param prompt: Input prompt
        :param examples: List of example interactions
        :return: Dict with response, tokens, and cost
        """
        if examples is None:
            examples = [
                {"input": "Translate to French: Hello", "output": "Bonjour"},
                {"input": "Translate to French: Goodbye", "output": "Au revoir"}
            ]

        messages = [{"role": "system", "content": "You are a helpful translation assistant."}]

        # Add few-shot examples
        for example in examples:
            messages.append({"role": "user", "content": example["input"]})
            messages.append({"role": "assistant", "content": example["output"]})

        # Add current prompt
        messages.append({"role": "user", "content": prompt})

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            result = response.choices[0].message.content
            tokens_used = response.usage.total_tokens
            cost = self.calculate_cost(tokens_used, "gpt-3.5-turbo")

            return {
                "response": result,
                "tokens": tokens_used,
                "cost": cost
            }
        except Exception as e:
            return {
                "response": f"Error in few-shot prompting: {str(e)}",
                "tokens": 0,
                "cost": 0.0
            }
    
    def chain_of_thought_prompting(self, problem: str) -> Dict[str, Any]:
        """
        Demonstrate chain-of-thought prompting for complex reasoning

        :param problem: Input problem requiring step-by-step reasoning
        :return: Dict with response, tokens, and cost
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
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert problem solver who explains reasoning clearly."},
                    {"role": "user", "content": prompt}
                ]
            )

            result = response.choices[0].message.content
            tokens_used = response.usage.total_tokens
            cost = self.calculate_cost(tokens_used, "gpt-3.5-turbo")

            return {
                "response": result,
                "tokens": tokens_used,
                "cost": cost
            }
        except Exception as e:
            return {
                "response": f"Error in chain-of-thought prompting: {str(e)}",
                "tokens": 0,
                "cost": 0.0
            }
    
    def role_playing_prompting(self, role: str, task: str) -> Dict[str, Any]:
        """
        Demonstrate role-playing prompting by assigning a specific role

        :param role: The role the AI should assume
        :param task: The task to be completed
        :return: Dict with response, tokens, and cost
        """
        prompt = f"""
        You are a {role}.
        Task: {task}

        Please respond as if you were truly in this role, using appropriate language,
        expertise, and perspective of the assigned persona.
        """

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are a {role}."},
                    {"role": "user", "content": prompt}
                ]
            )

            result = response.choices[0].message.content
            tokens_used = response.usage.total_tokens
            cost = self.calculate_cost(tokens_used, "gpt-3.5-turbo")

            return {
                "response": result,
                "tokens": tokens_used,
                "cost": cost
            }
        except Exception as e:
            return {
                "response": f"Error in role-playing prompting: {str(e)}",
                "tokens": 0,
                "cost": 0.0
            }
    
    def persona_based_prompting(self, persona: str, query: str) -> Dict[str, Any]:
        """
        Demonstrate persona-based prompting with specific characteristics

        :param persona: Description of the persona
        :param query: User's query
        :return: Dict with response, tokens, and cost
        """
        prompt = f"""
        You are a {persona}.
        Consider your unique background, knowledge, and communication style.

        Respond to the following query:
        {query}

        Ensure your response reflects the specific perspective of this persona.
        """

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are a {persona}"},
                    {"role": "user", "content": prompt}
                ]
            )

            result = response.choices[0].message.content
            tokens_used = response.usage.total_tokens
            cost = self.calculate_cost(tokens_used, "gpt-3.5-turbo")

            return {
                "response": result,
                "tokens": tokens_used,
                "cost": cost
            }
        except Exception as e:
            return {
                "response": f"Error in persona-based prompting: {str(e)}",
                "tokens": 0,
                "cost": 0.0
            }

    def react_prompting(self, task: str) -> Dict[str, Any]:
        """
        Demonstrate ReAct (Reasoning + Acting) prompting

        :param task: Task requiring reasoning and actions
        :return: Dict with response, tokens, and cost
        """
        prompt = f"""
        Task: {task}

        Use the ReAct framework to solve this task:
        1. Thought: What do I need to think about?
        2. Action: What action should I take?
        3. Observation: What did I observe?
        4. (Repeat as needed)
        5. Answer: Final solution

        Format your response with clear Thought, Action, and Observation steps.
        """

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an AI assistant that uses the ReAct framework (Reasoning + Acting) to solve problems step by step."},
                    {"role": "user", "content": prompt}
                ]
            )

            result = response.choices[0].message.content
            tokens_used = response.usage.total_tokens
            cost = self.calculate_cost(tokens_used, "gpt-3.5-turbo")

            return {
                "response": result,
                "tokens": tokens_used,
                "cost": cost
            }
        except Exception as e:
            return {
                "response": f"Error in ReAct prompting: {str(e)}",
                "tokens": 0,
                "cost": 0.0
            }

    def self_consistency_prompting(self, problem: str, num_samples: int = 3) -> Dict[str, Any]:
        """
        Demonstrate Self-Consistency prompting by generating multiple reasoning paths

        :param problem: Problem to solve
        :param num_samples: Number of reasoning paths to generate
        :return: Dict with multiple responses and aggregated result
        """
        prompt = f"""
        Solve this problem and explain your reasoning:
        {problem}

        Show your step-by-step thinking process.
        """

        try:
            responses = []
            total_tokens = 0

            for i in range(num_samples):
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are an expert problem solver. Think step by step and show your reasoning."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7  # Higher temperature for diversity
                )

                responses.append(response.choices[0].message.content)
                total_tokens += response.usage.total_tokens

            # Aggregate responses
            aggregated = f"Self-Consistency Analysis ({num_samples} reasoning paths):\n\n"
            for i, resp in enumerate(responses, 1):
                aggregated += f"--- Path {i} ---\n{resp}\n\n"

            aggregated += "\n--- Consensus ---\nMultiple reasoning paths generated. Review the different approaches above."

            cost = self.calculate_cost(total_tokens, "gpt-3.5-turbo")

            return {
                "response": aggregated,
                "tokens": total_tokens,
                "cost": cost,
                "num_paths": num_samples
            }
        except Exception as e:
            return {
                "response": f"Error in self-consistency prompting: {str(e)}",
                "tokens": 0,
                "cost": 0.0
            }

    def tree_of_thoughts_prompting(self, problem: str) -> Dict[str, Any]:
        """
        Demonstrate Tree-of-Thoughts prompting by exploring multiple solution branches

        :param problem: Complex problem to solve
        :return: Dict with response, tokens, and cost
        """
        prompt = f"""
        Problem: {problem}

        Use Tree-of-Thoughts approach:
        1. Generate 3 initial solution approaches
        2. For each approach, evaluate its strengths and weaknesses
        3. Select the most promising approach
        4. Develop that approach with detailed steps
        5. Provide the final solution

        Format your response clearly showing:
        - Initial Branches (3 approaches)
        - Evaluation of each branch
        - Selected branch with reasoning
        - Detailed solution
        """

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert at exploring multiple solution paths and selecting the best approach."},
                    {"role": "user", "content": prompt}
                ]
            )

            result = response.choices[0].message.content
            tokens_used = response.usage.total_tokens
            cost = self.calculate_cost(tokens_used, "gpt-3.5-turbo")

            return {
                "response": result,
                "tokens": tokens_used,
                "cost": cost
            }
        except Exception as e:
            return {
                "response": f"Error in Tree-of-Thoughts prompting: {str(e)}",
                "tokens": 0,
                "cost": 0.0
            }

    def calculate_cost(self, tokens: int, model: str = "gpt-3.5-turbo") -> float:
        """
        Calculate the cost of API usage

        :param tokens: Total tokens used
        :param model: Model name
        :return: Cost in USD
        """
        # Pricing as of 2024 (per 1M tokens)
        pricing = {
            "gpt-3.5-turbo": {"input": 0.50, "output": 1.50},  # Average
            "gpt-4": {"input": 30.00, "output": 60.00},
            "gpt-4-turbo": {"input": 10.00, "output": 30.00}
        }

        # Use average pricing for simplicity (actual cost varies by input/output ratio)
        if model in pricing:
            avg_price = (pricing[model]["input"] + pricing[model]["output"]) / 2
            cost = (tokens / 1_000_000) * avg_price
        else:
            cost = (tokens / 1_000_000) * 1.00  # Default fallback

        return round(cost, 6)

    def compare_techniques(self, prompt: str, techniques: List[str] = None) -> Dict[str, Any]:
        """
        Compare multiple prompting techniques side-by-side

        :param prompt: The same prompt to test across techniques
        :param techniques: List of technique names to compare
        :return: Dict with comparison results
        """
        if techniques is None:
            techniques = ["Zero-Shot Prompting", "Few-Shot Prompting", "Chain-of-Thought Prompting"]

        comparison_results = {}
        total_tokens = 0
        total_cost = 0.0

        for technique in techniques:
            if technique not in self.prompting_techniques:
                comparison_results[technique] = {"error": "Technique not found"}
                continue

            try:
                if technique == "Zero-Shot Prompting":
                    result = self.zero_shot_prompting(prompt)
                elif technique == "Few-Shot Prompting":
                    result = self.few_shot_prompting(f"Translate to French: {prompt}")
                elif technique == "Chain-of-Thought Prompting":
                    result = self.chain_of_thought_prompting(prompt)
                elif technique == "Role-Playing Prompting":
                    result = self.role_playing_prompting("expert consultant", prompt)
                elif technique == "Persona-Based Prompting":
                    result = self.persona_based_prompting("experienced professional", prompt)
                else:
                    result = {"response": "Not implemented for comparison", "tokens": 0, "cost": 0.0}

                comparison_results[technique] = result
                total_tokens += result.get("tokens", 0)
                total_cost += result.get("cost", 0.0)

            except Exception as e:
                comparison_results[technique] = {"error": str(e)}

        return {
            "prompt": prompt,
            "techniques_compared": len(techniques),
            "results": comparison_results,
            "total_tokens": total_tokens,
            "total_cost": round(total_cost, 6)
        }

    def get_prompt_templates(self) -> Dict[str, Dict[str, str]]:
        """
        Get a library of pre-built prompt templates

        :return: Dict of prompt templates by category
        """
        return {
            "Translation": {
                "Simple": "Translate the following text to {language}: {text}",
                "Formal": "Provide a formal translation of this text to {language}, maintaining professional tone: {text}",
                "Context": "Translate this {context} text to {language}: {text}"
            },
            "Summarization": {
                "Brief": "Summarize this in 2-3 sentences: {text}",
                "Bullet Points": "Summarize the key points as a bullet list: {text}",
                "Executive": "Provide an executive summary highlighting main insights: {text}"
            },
            "Code": {
                "Explain": "Explain what this code does in simple terms: {code}",
                "Debug": "Find and explain the bug in this code: {code}",
                "Optimize": "Suggest optimizations for this code: {code}",
                "Convert": "Convert this code from {from_lang} to {to_lang}: {code}"
            },
            "Creative Writing": {
                "Story": "Write a {length} story about {topic} in the style of {style}",
                "Poem": "Write a {type} poem about {topic}",
                "Dialogue": "Write a dialogue between {character1} and {character2} about {topic}"
            },
            "Analysis": {
                "Pros and Cons": "Analyze the pros and cons of {topic}",
                "Compare": "Compare and contrast {item1} and {item2}",
                "SWOT": "Perform a SWOT analysis of {topic}"
            },
            "Business": {
                "Email": "Write a {tone} email about {topic} to {recipient}",
                "Proposal": "Draft a business proposal for {project}",
                "Report": "Create an executive report on {topic}"
            }
        }

    def use_template(self, category: str, template_name: str, **kwargs) -> str:
        """
        Use a prompt template with provided variables

        :param category: Template category
        :param template_name: Name of template
        :param kwargs: Variables to fill in template
        :return: Formatted prompt
        """
        templates = self.get_prompt_templates()

        if category not in templates:
            return f"Category '{category}' not found"

        if template_name not in templates[category]:
            return f"Template '{template_name}' not found in category '{category}'"

        template = templates[category][template_name]

        try:
            return template.format(**kwargs)
        except KeyError as e:
            return f"Missing variable: {str(e)}"

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