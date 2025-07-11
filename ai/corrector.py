from openai import OpenAI
client = OpenAI()

def auto_correct_text(partial_text):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Fix incomplete words or STT errors."},
            {"role": "user", "content": f"The text: '{partial_text}'"}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content.strip()
