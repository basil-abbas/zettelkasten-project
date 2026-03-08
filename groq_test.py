import os
from dotenv import load_dotenv
from groq import Groq

# 1. Load the "Vault" (.env)
# Get access to the API key and model from the .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
ai_model = os.getenv("GROQ_MODEL")

# 2. Check if the key exists
if not api_key:
    print("❌ Error: GROQ_API_KEY not found in .env file!")
else:
    print("✅ API Key detected. Sending request to Groq...")

    # 3. Initialize the Groq client
    client = Groq(api_key=api_key)

    # 4. Ask a simple question
    completion = client.chat.completions.create(
        model = ai_model, # (llama-3.3-70b-versatile is great for logic)
        messages=[{"role": "user", "content": "Tell me what is the capital of France?"}]
    )

    # 5. Print the "Brain's" response
    print("\nGroq says:")
    print(completion.choices[0].message.content)