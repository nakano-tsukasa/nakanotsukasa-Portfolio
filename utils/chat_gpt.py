import os
import openai

def generate_summary_via_chatgpt(combined_texts):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Error: OPENAI_API_KEY environment variable is not set.")
        return None

    openai.api_key = api_key

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "あなたは要約を作成するアシスタントです。"},
            {"role": "user", "content": f"次の2つの要約を基に、2～3文で抽象的な要約を作成してください。要約以外の返答は一切含めないでください。：\n\n{combined_texts}"}
        ],
        "max_tokens": 100,  # 要約の長さを制限
        "temperature": 0.5  # 生成されるテキストのランダム性
    }

    try:
        response = openai.Completion.create(**data)
        ai_generated_summary = response.choices[0].message['content'].strip()
        return ai_generated_summary
    except openai.OpenAIError as e:
        print(f"OpenAI API Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None