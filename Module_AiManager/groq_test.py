import os
from dotenv import load_dotenv
from groq import Groq

# 1. Load the "Vault" (.env)
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# 2. Check if the key exists
if not api_key:
    print("❌ Error: GROQ_API_KEY not found in .env file!")
else:
    print("✅ API Key detected. Sending request to Groq...")

    # 3. Initialize the Groq client
    client = Groq(api_key=api_key)

    # 4. Ask a simple question
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile", # This is a fast, reliable model
        messages=[{"role": "user", "content": "Explain the Zettelkasten method in 1 sentence."}]
    )

    # 5. Print the "Brain's" response
    print("\nGroq says:")
    print(completion.choices[0].message.content)