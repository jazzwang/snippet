# coding: utf-8
import google.cloud.texttospeech as tts
import argparse
import soundfile as sf
import numpy as np
from pydub import AudioSegment

def text_to_mp3(voice_name: str, text: str, output_name: str):
    language_code = "-".join(voice_name.split("-")[:2])
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )
    audio_config = tts.AudioConfig(
        audio_encoding=tts.AudioEncoding.MP3,
        speaking_rate=0.5,
    )
    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input,
        voice=voice_params,
        audio_config=audio_config,
    )
    filename = f"{output_name}.mp3"
    with open(filename, "wb") as out:
        out.write(response.audio_content)
        print(f'Generated speech saved to "{filename}"')

def word_to_spell(word: str):
    spell = str.upper(word[0])
    for i in range(1, len(word)):
        spell += ".." + str.upper(word[i])
    return spell

def say_spell_say(word: str):
    spell = word_to_spell(word)
    return f"{word}...{spell}...{word}"

def spelling_bee(word: str):
    text_to_mp3("en-US-Studio-O",say_spell_say(word), word)

def blank_mp3(seconds: int):
    # Define parameters for the blank audio
    duration = seconds  # seconds
    samplerate = 44100  # samples per second
    channels = 2  # stereo

    # Create an array of zeros for the audio data
    audio_data = np.zeros((samplerate * duration, channels))

    # Write the audio data to a file
    sf.write('blank_audio.mp3', audio_data, samplerate)

def question(word: str):
    text_to_mp3("en-US-Studio-O",f"{word}..{word}..{word}", f"_{word}")
    combined_audio = AudioSegment.from_mp3(f"_{word}.mp3") + AudioSegment.from_mp3("blank_audio.mp3")
    combined_audio.export(f"Q_{word}.mp3", format="mp3")

def main():
    # parsing CLI arguments
    parser = argparse.ArgumentParser(description="Generate Spelling Bee .")
    parser.add_argument("input_file", help="input file with words.")
    parser.add_argument("--question", "-q", type=int, help="generate questions")
    args = parser.parse_args()

    input_file = args.input_file

    with open(input_file, 'r') as f:
        words = f.readlines()
        for word in words:
            if (args.question):
                blank_mp3(args.question)
                question(word.strip())
            else:
                spelling_bee(word.strip())

if __name__ == "__main__":
    main()