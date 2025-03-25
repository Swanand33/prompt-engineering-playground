import streamlit as st
import os
from src.prompt_playground import PromptEngineeringPlayground

def create_streamlit_app():
    """
    Create an interactive Streamlit app for the Prompt Engineering Playground
    """
    st.title("🧠 Prompt Engineering Playground")
    
    # Sidebar for technique selection
    technique = st.sidebar.selectbox(
        "Select Prompting Technique",
        [
            "Zero-Shot Prompting",
            "Few-Shot Prompting",
            "Chain-of-Thought Prompting",
            "Role-Playing Prompting",
            "Persona-Based Prompting"
        ]
    )
    
    # API Key input
    api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")
    
    # Technique-specific inputs
    if technique == "Zero-Shot Prompting":
        prompt = st.text_input("Enter your prompt")
        if st.button("Generate Response"):
            if api_key:
                try:
                    playground = PromptEngineeringPlayground(api_key)
                    result = playground.zero_shot_prompting(prompt)
                    st.success("Response Generated!")
                    st.write(result)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
            else:
                st.warning("Please enter an API key")
    
    elif technique == "Few-Shot Prompting":
        prompt = st.text_input("Enter translation prompt")
        example_input = st.text_input("Example Input")
        example_output = st.text_input("Example Output")
        
        if st.button("Generate Translation"):
            if api_key:
                try:
                    playground = PromptEngineeringPlayground(api_key)
                    examples = [{"input": example_input, "output": example_output}]
                    result = playground.few_shot_prompting(prompt, examples)
                    st.success("Translation Generated!")
                    st.write(result)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
            else:
                st.warning("Please enter an API key")
    
    # Additional technique-specific sections can be added here
    
    # About section
    st.sidebar.markdown("## About")
    st.sidebar.info("""
    Prompt Engineering Playground demonstrates various 
    prompting techniques for large language models.
    
    Created by: Swanand Potnis
    GitHub: [Your GitHub Profile]
    """)

def main():
    create_streamlit_app()

if __name__ == "__main__":
    main()
