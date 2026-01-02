import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from prompt import system_prompt

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise ValueError("HF_TOKEN not found in .env")
REPO_ID = "Qwen/Qwen2.5-72B-Instruct"
client = InferenceClient(token=HF_TOKEN, provider="auto")
print(f"🤖 Connected to {REPO_ID} (Free Tier)\n")

messages = [{"role": "system", "content": system_prompt}]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("See you soon.")
        break
    
    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat_completion(
            model=REPO_ID,
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )
        
        ai_reply = response.choices[0].message.content
        print(f"AI: {ai_reply}\n")

        messages.append({"role": "assistant", "content": ai_reply})

    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Tip: If the model fails, try 'meta-llama/Llama-3.2-3B-Instruct' (requires license agreement).")