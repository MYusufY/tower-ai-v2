from gtts import gTTS
from pydub import AudioSegment
from pydub.generators import WhiteNoise
from pydub.effects import compress_dynamic_range
from playsound import playsound
from ollama import chat
from ollama import ChatResponse
import os
import speech_recognition as sr

class ask_AIr:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen_to_audio(self):
        with self.microphone as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio, language='en')
                print(f"You Said: {text}")
                return text
            except sr.UnknownValueError:
                print("Didnt understand!")
                return None
            except sr.RequestError:
                print("An error ocurred.")
                return None

    def ask_ai(self, question):
        response: ChatResponse = chat(model='tower-ai', messages=[
        {
            'role': 'user',
            'content': '{qstn}'.format(qstn=question),
        },
        ])
        return response.message.content

    def text_to_speech(self, text, file_name='output.mp3'):
        tts = gTTS(text=text, lang='en')
        tts.save(file_name)

    def add_radio_effect(self, input_file, output_file):
        sound = AudioSegment.from_file(input_file)

        sound = sound.low_pass_filter(3000)
        sound = sound.high_pass_filter(300)

        noise = WhiteNoise().to_audio_segment(duration=len(sound), volume=-35)
        combined = sound.overlay(noise)

        combined = compress_dynamic_range(combined)

        def add_distortion(audio, gain=20):
            distorted = audio + gain
            distorted = distorted.set_frame_rate(44100)
            distorted = distorted.apply_gain_stereo(gain, gain)
            return distorted

        combined = add_distortion(combined, gain=10)

        combined.export(output_file, format="mp3")

    def run(self):
        question = self.listen_to_audio()
        if question:
            response_text = self.ask_ai(question)
            self.text_to_speech(response_text)
            self.add_radio_effect('output.mp3', 'radio_effect_output.mp3')
            playsound("radio_effect_output.mp3")

if __name__ == "__main__":
    ai_assistant = ask_AIr()
    ai_assistant.run()
