import streamlit as st
import os
from src.prompt_playground import PromptEngineeringPlayground

def create_streamlit_app():
    """
    Create an interactive Streamlit app for the Prompt Engineering Playground
    """
    st.set_page_config(
        page_title="🧠 Prompt Engineering Playground",
        page_icon="🧠",
        layout="wide"
    )

    st.title("🧠 Prompt Engineering Playground")
    st.markdown("**Learn and experiment with advanced prompting techniques for LLMs**")

    # Sidebar for global settings
    st.sidebar.header("⚙️ Settings")

    # API Key input
    api_key = st.sidebar.text_input("OpenAI API Key", type="password", help="Your OpenAI API key")

    if not api_key:
        st.warning("⚠️ Please enter your OpenAI API key in the sidebar to begin")
        st.info("""
        ### Getting Started:
        1. Enter your OpenAI API key in the sidebar
        2. Choose a mode: Single Technique, Compare, or Templates
        3. Experiment with different prompting techniques!
        """)
        return

    # Initialize playground
    try:
        playground = PromptEngineeringPlayground(api_key)
    except Exception as e:
        st.error(f"Error initializing playground: {str(e)}")
        return

    # Mode selection
    mode = st.sidebar.radio(
        "Select Mode",
        ["🎯 Single Technique", "🆚 Compare Techniques", "📚 Prompt Templates"]
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 About")
    st.sidebar.info("""
    This tool demonstrates 8 prompting techniques:

    **Basic:**
    - Zero-Shot
    - Few-Shot
    - Chain-of-Thought
    - Role-Playing
    - Persona-Based

    **Advanced:**
    - ReAct (Reasoning + Acting)
    - Self-Consistency
    - Tree-of-Thoughts
    """)

    # Mode-specific UI
    if mode == "🎯 Single Technique":
        show_single_technique_mode(playground)
    elif mode == "🆚 Compare Techniques":
        show_comparison_mode(playground)
    else:
        show_template_mode(playground)


def show_single_technique_mode(playground):
    """Show single technique experimentation mode"""
    st.header("🎯 Single Technique Mode")

    technique = st.selectbox(
        "Select Prompting Technique",
        list(playground.prompting_techniques.keys())
    )

    # Technique-specific inputs
    if technique == "Zero-Shot Prompting":
        st.markdown("**Zero-Shot**: No examples provided, testing model's base knowledge")
        prompt = st.text_area("Enter your prompt", height=100)

        if st.button("🚀 Generate", key="zero_shot"):
            if prompt:
                with st.spinner("Generating response..."):
                    result = playground.zero_shot_prompting(prompt)
                    display_result(result, technique)
            else:
                st.warning("Please enter a prompt")

    elif technique == "Few-Shot Prompting":
        st.markdown("**Few-Shot**: Provide examples to guide the model")
        st.markdown("**Example**: Translation task")

        col1, col2 = st.columns(2)
        with col1:
            ex1_input = st.text_input("Example 1 Input", value="Translate to French: Hello")
            ex1_output = st.text_input("Example 1 Output", value="Bonjour")
        with col2:
            ex2_input = st.text_input("Example 2 Input", value="Translate to French: Goodbye")
            ex2_output = st.text_input("Example 2 Output", value="Au revoir")

        prompt = st.text_area("Your prompt", height=80)

        if st.button("🚀 Generate", key="few_shot"):
            if prompt:
                with st.spinner("Generating response..."):
                    examples = [
                        {"input": ex1_input, "output": ex1_output},
                        {"input": ex2_input, "output": ex2_output}
                    ]
                    result = playground.few_shot_prompting(prompt, examples)
                    display_result(result, technique)
            else:
                st.warning("Please enter a prompt")

    elif technique == "Chain-of-Thought Prompting":
        st.markdown("**Chain-of-Thought**: Break down complex reasoning step-by-step")
        problem = st.text_area("Enter a problem requiring reasoning", height=100,
                               placeholder="Example: If a train travels 120 miles in 2 hours, how fast is it going in miles per minute?")

        if st.button("🚀 Solve", key="cot"):
            if problem:
                with st.spinner("Solving step-by-step..."):
                    result = playground.chain_of_thought_prompting(problem)
                    display_result(result, technique)
            else:
                st.warning("Please enter a problem")

    elif technique == "Role-Playing Prompting":
        st.markdown("**Role-Playing**: Assign a specific role to the AI")

        role = st.text_input("Role", placeholder="Example: experienced software engineer, marketing expert, historian")
        task = st.text_area("Task", height=100, placeholder="What should they help with?")

        if st.button("🚀 Generate", key="role"):
            if role and task:
                with st.spinner(f"Generating as {role}..."):
                    result = playground.role_playing_prompting(role, task)
                    display_result(result, technique)
            else:
                st.warning("Please enter both role and task")

    elif technique == "Persona-Based Prompting":
        st.markdown("**Persona-Based**: Use a specific persona with unique characteristics")

        persona = st.text_input("Persona", placeholder="Example: enthusiastic teacher who loves analogies")
        query = st.text_area("Query", height=100)

        if st.button("🚀 Generate", key="persona"):
            if persona and query:
                with st.spinner("Generating response..."):
                    result = playground.persona_based_prompting(persona, query)
                    display_result(result, technique)
            else:
                st.warning("Please enter both persona and query")

    elif technique == "ReAct Prompting":
        st.markdown("**ReAct**: Reasoning + Acting framework for problem-solving")
        st.markdown("*The model will think, act, and observe iteratively*")

        task = st.text_area("Task", height=100, placeholder="Example: Plan a trip to Paris for 3 days")

        if st.button("🚀 Generate", key="react"):
            if task:
                with st.spinner("Using ReAct framework..."):
                    result = playground.react_prompting(task)
                    display_result(result, technique)
            else:
                st.warning("Please enter a task")

    elif technique == "Self-Consistency Prompting":
        st.markdown("**Self-Consistency**: Generate multiple reasoning paths and find consensus")

        problem = st.text_area("Problem", height=100)
        num_paths = st.slider("Number of reasoning paths", 2, 5, 3)

        if st.button("🚀 Generate", key="self_cons"):
            if problem:
                with st.spinner(f"Generating {num_paths} reasoning paths..."):
                    result = playground.self_consistency_prompting(problem, num_paths)
                    display_result(result, technique)
            else:
                st.warning("Please enter a problem")

    elif technique == "Tree-of-Thoughts Prompting":
        st.markdown("**Tree-of-Thoughts**: Explore multiple solution branches before selecting the best")

        problem = st.text_area("Complex Problem", height=100,
                               placeholder="Example: Design a sustainable urban transportation system")

        if st.button("🚀 Generate", key="tot"):
            if problem:
                with st.spinner("Exploring solution tree..."):
                    result = playground.tree_of_thoughts_prompting(problem)
                    display_result(result, technique)
            else:
                st.warning("Please enter a problem")


def show_comparison_mode(playground):
    """Show technique comparison mode"""
    st.header("🆚 Compare Techniques")
    st.markdown("Test the same prompt across multiple techniques to see how they differ!")

    prompt = st.text_area("Enter a prompt to compare", height=100,
                         placeholder="Example: Explain quantum computing")

    techniques = st.multiselect(
        "Select techniques to compare",
        list(playground.prompting_techniques.keys()),
        default=["Zero-Shot Prompting", "Few-Shot Prompting", "Chain-of-Thought Prompting"]
    )

    if st.button("🆚 Compare", key="compare"):
        if prompt and techniques:
            with st.spinner("Comparing techniques..."):
                result = playground.compare_techniques(prompt, techniques)

                # Display comparison
                st.success(f"✅ Compared {result['techniques_compared']} techniques")

                # Show metrics
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Total Tokens", result['total_tokens'])
                with col2:
                    st.metric("Total Cost", f"${result['total_cost']}")

                # Show each result
                for tech, res in result['results'].items():
                    st.markdown(f"### {tech}")
                    if 'error' in res:
                        st.error(f"Error: {res['error']}")
                    else:
                        st.write(res.get('response', 'No response'))

                        col1, col2 = st.columns(2)
                        with col1:
                            st.caption(f"Tokens: {res.get('tokens', 0)}")
                        with col2:
                            st.caption(f"Cost: ${res.get('cost', 0.0)}")

                    st.markdown("---")
        else:
            st.warning("Please enter a prompt and select techniques")


def show_template_mode(playground):
    """Show prompt template library mode"""
    st.header("📚 Prompt Templates")
    st.markdown("Use pre-built templates for common tasks")

    templates = playground.get_prompt_templates()

    category = st.selectbox("Select Category", list(templates.keys()))
    template_name = st.selectbox("Select Template", list(templates[category].keys()))

    # Show template
    template = templates[category][template_name]
    st.code(template, language="text")

    # Extract variables from template
    import re
    variables = re.findall(r'\{(\w+)\}', template)

    if variables:
        st.markdown("### Fill in the variables:")
        var_values = {}
        for var in variables:
            var_values[var] = st.text_input(f"{var.replace('_', ' ').title()}", key=f"var_{var}")

        if st.button("🎨 Create Prompt", key="template"):
            prompt = playground.use_template(category, template_name, **var_values)
            st.success("✅ Prompt created!")
            st.code(prompt, language="text")

            # Option to run with selected technique
            st.markdown("### Run with technique:")
            technique = st.selectbox("Select Technique",
                                   ["Zero-Shot Prompting", "Chain-of-Thought Prompting"])

            if st.button("🚀 Run", key="run_template"):
                with st.spinner("Generating..."):
                    if technique == "Zero-Shot Prompting":
                        result = playground.zero_shot_prompting(prompt)
                    else:
                        result = playground.chain_of_thought_prompting(prompt)

                    display_result(result, technique)


def display_result(result, technique):
    """Display result with metrics"""
    if 'error' in result or (isinstance(result, dict) and 'response' in result):
        response = result.get('response', str(result))

        st.markdown("### 💬 Response:")
        st.write(response)

        if 'tokens' in result and 'cost' in result:
            st.markdown("### 📊 Metrics:")
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Tokens Used", result['tokens'])
            with col2:
                st.metric("Cost (USD)", f"${result['cost']}")
            with col3:
                st.metric("Technique", technique)

            # Additional metrics for special techniques
            if 'num_paths' in result:
                st.metric("Reasoning Paths", result['num_paths'])
    else:
        st.write(result)


def main():
    create_streamlit_app()


if __name__ == "__main__":
    main()
