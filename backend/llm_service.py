import openai

openai_api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(input_text: str) -> str:
    """
    Generate a summary of the given text using GPT-4.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant summarizing MLB game highlights."},
                {"role": "user", "content": input_text},
            ],
            temperature=0.7,
            max_tokens=300
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"An error occurred while generating the summary: {str(e)}"
