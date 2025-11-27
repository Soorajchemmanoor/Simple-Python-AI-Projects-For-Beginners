from openai import OpenAI


client = OpenAI(api_key="_YOUR_OPEN_AI_API_KEY_HERE_")

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
     temperature = 0.2,
     max_tokens=200
)

    return (response.choices[0].message.content or "").strip()

def safe_correct(text):
    """Validate input and delegate to check_grammar; return friendly error on blank input."""
    text = (text).strip()
    if not text:
        return "Error: No text provided to correct."
    return check_grammar(text)

while True:
        sentence = input("Enter a sentence: ").strip()
        if sentence.lower() == "q":
            print("Goodbye!")
            break
        result = safe_correct(sentence)
        print("Corrected version:")
        print(result, "\n")

