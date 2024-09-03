import os
from openai import OpenAI
import json

def generate_summary_via_chatgpt(latest_d_summary_text,summary_text):

    user_message = f"Please summarize these two texts.Please answer in one sentence, no headings.:\n\nText 1:{latest_d_summary_text}\n\nText 2:{summary_text}"

    my_api_key = os.getenv("OPENAI_API_KEY")
    if not my_api_key:
        print("Error: OPENAI_API_KEY environment variable is not set.")
        return None
    
    MODEL = "gpt-3.5-turbo"
    client = OpenAI(api_key=my_api_key)

    try:
        responce = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content":"You are a helpfull assistant."},
            {"role": "user", "content": user_message},
        ],
        temperature=0.7
        )
        ai_generated_summary_pre = json.loads(responce.model_dump_json())
        ai_generated_summary = ai_generated_summary_pre['choices'][0]['message']['content']
        return ai_generated_summary
    except Exception as e:
        print(f"Unexpected Error: {e}")