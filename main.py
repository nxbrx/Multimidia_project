import os
from openai import OpenAI
from pathlib import Path

client =  OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_story(character: str, setting: str) -> str:
    prompt = f"""
        Tell a fun, imaginative short story about {character} in {setting}.
        Make it creative and engaging for the reader.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    story = response.choices[0].message["content"]
    return story

def text_to_speech(story: str, character: str) -> None:
    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=story
    )

    audio_path = Path(f"{character}.mp3")
    audio_path.write_bytes(response.audio)

if __name__ == "__main__":
    character = input("Enter a main character: ")
    setting = input("Enter a setting: ")

    story = generate_story(character, setting)
    text_to_speech(story, character)

    print(f"Your story was saved in {character}.mp3!")
