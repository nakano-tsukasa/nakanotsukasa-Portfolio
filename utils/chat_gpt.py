import os
import openai

def generate_summary_via_chatgpt(latest_d_summary_text,summary_text):

    user_message = f"Please summarize these two texts.No response text other than a summary statement is required.:\n\nText 1:{latest_d_summary_text}\n\nText 2:{summary_text}"

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable is not set.")
        return None
    client = openai.OpenAI(api_key=api_key)
    MODEL = "gpt-3.5-turbo"

    try:
        completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content":"You are a helpfull assistant."},
            {"role": "user", "content": user_message},
        ],
        temperature=0.7
        )
        ai_generated_summary = completion.choices[0].message['content'].strip()
        return ai_generated_summary
    except openai.OpenAIError as e:
        print(f"OpenAI API Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None