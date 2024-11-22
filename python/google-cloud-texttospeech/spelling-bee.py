# coding: utf-8
import google.cloud.texttospeech as tts

def text_to_mp3(voice_name: str, text: str, output_name: str):
    language_code = "-".join(voice_name.split("-")[:2])
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )
    audio_config = tts.AudioConfig(
        audio_encoding=tts.AudioEncoding.MP3,  
        speaking_rate=0.75,
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

word = "shoemaker"
print(say_spell_say(word))
text_to_mp3("en-US-Standard-C",say_spell_say(word), word)