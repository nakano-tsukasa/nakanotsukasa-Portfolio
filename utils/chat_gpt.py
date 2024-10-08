import os
from openai import OpenAI
import json
from dotenv import load_dotenv

def generate_summary_via_chatgpt(latest_d_summary_text,summary_text):

    # user_message = f"Please summarize these two texts.Please answer in one sentence, no headings.:\n\nText 1:{latest_d_summary_text}\n\nText 2:{summary_text}"
    user_message = f"二つの文章をより抽象的な概念に結合し、一文に要約してください。前置きは無しで、それが要約文であるということの明示もしないでください。日本語でお願いします。:\n\n文章 1:{latest_d_summary_text}\n\n文章 2:{summary_text}"

    load_dotenv()
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