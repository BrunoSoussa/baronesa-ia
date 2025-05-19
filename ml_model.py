# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()
client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
)
model_name = "gemini-2.0-flash"


def generate_text(user_input: str, prompt: str) -> str:
    """
    Generates text from Gemini model by concatenating user_input and prompt.

    Returns the full generated string.
    """
    contents = [
        types.Content(
            role="user",
            parts=[ types.Part.from_text(text=f"{user_input}{prompt}") ],
        ),
    ]
    config = types.GenerateContentConfig(response_mime_type="text/plain")

    output = []
    for chunk in client.models.generate_content_stream(
        model=model_name,
        contents=contents,
        config=config,
    ):
        output.append(chunk.text)
    return "".join(output)


if __name__ == "__main__":
    print(generate_text('oi','tudo bem? me fale o ino do brasil'))
