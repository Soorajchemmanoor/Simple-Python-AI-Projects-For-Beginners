from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key securely
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError(" OpenAI API key not found. Please set it in your .env file.")

client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM = "You are a precise grammar corrector. Return only the corrected sentence."

def build_prompt(text):
    return f'Correct the grammar in the following text:\n\n"{text}"'


def check_grammar(sentence):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": build_prompt(sentence)},
        ],
        temperature=0.2,
        max_tokens=200
    )

    return (response.choices[0].message.content or "").strip()


def safe_correct(text):
    text = text.strip()
    if not text:
        return "Error: No text provided to correct."
    return check_grammar(text)


def main():
    print("AI Grammar Checker (Type 'q' to quit)\n")

    while True:
        sentence = input("Enter a sentence: ").strip()

        if sentence.lower() == "q":
            print("Goodbye!")
            break

        result = safe_correct(sentence)

        print("Corrected version:")
        print(result, "\n")


if __name__ == "__main__":
    main()
