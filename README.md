🤖 Prompt-Based AI Assistant (Hugging Face)

A lightweight, terminal-based AI assistant built using Hugging Face Inference API.
This project demonstrates how system prompting, conversation memory, and API-based LLM interaction work together to create a controlled, user-friendly AI assistant.

The assistant follows strict response rules defined in a system prompt to reduce hallucinations and enforce consistent output structure.

🚀 Features

Uses Hugging Face hosted LLMs via InferenceClient

Maintains conversation context using message history

Custom system prompt for controlled behavior

Free-tier friendly setup

Simple terminal-based chat interface

Clean separation of logic and prompt configuration

🧠 Model Used

Qwen/Qwen2.5-72B-Instruct (default)

Provider: Hugging Face Inference API (auto routing)

If the default model fails, you can switch to smaller or licensed models like:

meta-llama/Llama-3.2-3B-Instruct (license required)

🗂 Project Structure
.
├── main.py        # Main application logic
├── prompt.py      # System prompt configuration
├── .env           # Environment variables (not committed)
└── README.md

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3️⃣ Install Dependencies
pip install huggingface_hub python-dotenv

4️⃣ Set Environment Variables

Create a .env file in the root directory:

HF_TOKEN=your_huggingface_api_token


Make sure your Hugging Face token has Inference API access enabled. 

main

▶️ How to Run
python main.py


You’ll see:

🤖 Connected to Qwen/Qwen2.5-72B-Instruct (Free Tier)
You:


Type your message and press Enter.
To exit:

exit


or

quit

🧩 System Prompt Design

The assistant behavior is strictly controlled via prompt.py.
Key rules include:

Short, concise answers (max 3–4 sentences)

No hallucinated or assumed data

No real-world/live data generation

Structured responses when multiple options exist

Clean formatting without special characters

This helps demonstrate why prompt engineering matters, even when using the same model. 

prompt

🎯 Learning Objectives

This project is useful if you want to learn:

How chat-based LLM APIs work

The impact of system prompts on output quality

Message role management (system, user, assistant)

Safe and controlled AI responses

Hugging Face Inference API basics

🔮 Future Improvements

Add streaming responses

Add retry and rate-limit handling

Support multiple models via config

Convert to web UI using Streamlit

Logging and conversation export

🧑‍💻 Author

Keval Vachhani
B.Tech IT | AI & Generative AI Learner
GitHub: https://github.com/kevalvachhani
