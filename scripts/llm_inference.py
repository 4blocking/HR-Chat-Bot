from openai import OpenAI

# Directly define your API key here
OPENAI_API_KEY = "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"

if not OPENAI_API_KEY:
    raise ValueError("Error: Missing OpenAI API Key.")

# Initialize the OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)


def generate_response(model, prompt):
    """
    Generate a response using OpenAI API with Structured Outputs.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI assistant trained on HDFS data. Identify the most relevant data sources."
                },
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"OpenAI API Error: {str(e)}"
