# 🧠 Prompt Engineering Playground

## 🌟 Project Overview
A comprehensive demonstration of advanced prompting techniques for large language models, showcasing the art and science of prompt engineering.

### 🚀 Key Features
- Interactive Streamlit web application
- Demonstration of 5 advanced prompting techniques:
  1. Zero-Shot Prompting
  2. Few-Shot Prompting
  3. Chain-of-Thought Prompting
  4. Role-Playing Prompting
  5. Persona-Based Prompting

## 📦 Installation

### Prerequisites
- Python 3.8+
- OpenAI API Key

### Setup Steps
1. Clone the repository
```bash
git clone https://github.com/Swanand33/prompt-engineering-playground.git
cd prompt-engineering-playground
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up OpenAI API Key
```bash
export OPENAI_API_KEY='your-api-key-here'
```

## 🖥️ Running the Application

### Streamlit App
```bash
streamlit run src/streamlit_app.py
```

### Command Line Demo
```bash
python -m src.prompt_playground
```

## 🧪 Running Tests
```bash
pytest tests/
```

## 📝 Key Techniques Explained

### 1. Zero-Shot Prompting
Generate responses without specific examples, testing the model's base knowledge.

### 2. Few-Shot Prompting
Provide a few examples to guide the model's response, improving context understanding.

### 3. Chain-of-Thought Prompting
Break down complex reasoning into step-by-step processes.

### 4. Role-Playing Prompting
Assign specific roles to generate contextually rich responses.

### 5. Persona-Based Prompting
Tailor responses by adopting specific personas and communication styles.

## 🤝 Contributing
Contributions are welcome! Please read the CONTRIBUTING.md for details.

## 📄 License
 MIT

## 💡 About the Author
**Swanand Potnis**
- LinkedIn: www.linkedin.com/in/swanandpotnis
- GitHub: https://github.com/Swanand33

## 🌐 Connect & Learn More
Explore the fascinating world of prompt engineering and AI interaction!