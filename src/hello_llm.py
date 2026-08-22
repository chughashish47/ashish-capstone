import sys
from dotenv import load_dotenv
from openai import OpenAI

#load openai key from environment
load_dotenv()

# Create the OpenAI client 
client = OpenAI()

def askQuestion(question:str):
    """Send one question to the LLM and return the answer text."""
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a brilliant but impatient data scientist. You explain accurately but you don't have time for niceties."},
            {"role": "user",   "content": question},
        ],
        temperature = 0.3
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) or "Say Welcome!!"
    print(askQuestion(q))