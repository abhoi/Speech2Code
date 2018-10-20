"""
    @author: Amlaan Bhoi, Debojit Kaushik
    @date: October 19 2018
    Module to encapsulate speech to text and text to speech requests from Google Speech Recognition API and Microsoft Luis API.
"""

import os
import json
import requests

import speech_recognition as sr
from google.cloud import speech
from google.cloud import texttospeech
from google.cloud.speech import enums
from google.cloud.speech import types

from pygame import mixer

CREDENTIAL_FILE_NAME = "/speech2code-0d3ecaa13ec2.json"
PATH = os.getcwd() + CREDENTIAL_FILE_NAME
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "%s" % PATH
LUIS_ENDPOINT = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/7cd5279c-2cdc-4234-b5dc-f2a4bfa809f2"

HEADERS = {
    # Request headers
    "Ocp-Apim-Subscription-Key": "6a6728b9981d417280f4dad97f82df96",
    "content-type": "application/json",
}

PARAMS = {
    # Don't forget to add query parameter "q": "query"
    'timezoneOffset': '0',
    'verbose': 'false',
    'spellCheck': 'false',
    'staging': 'false',
}

class Text2CodeRequest:
    def __init__(self, query, headers, params):
        self.query = query
        self.headers = headers
        self.params = params

    def _create_to_code_request(self):
        """
            Function to create a text to code request to Microsoft Luis
            Args:
                self: contains query, headers, and parameters
            Returns:
                json_response: [dict] a dictionary holding response from Luis including intent classifications
        """
        try:
            self.params["q"] = self.query
            print(params["q"])
            r = requests.get(LUIS_ENDPOINT, headers=self.headers, params=self.params)
            json_response = r.json()
            print(r.status_code)
            print(json_response)
            return json_response
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

class Speech2TextRequest:
    def __init__(self):
        pass

    def _create_to_text_request(self):
        r = sr.Recognizer()
        mic = sr.Microphone(device_index=0)
        print("Say something...")
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=1.0)
            audio = r.listen(source)
        print("Audio recorded!")
        self.audio = audio
        return self._transcribe_file()

    def _transcribe_file(self):
        """
            Function to call Google Speech-to-Text API to convert speech to text
            Args:
                self: contains audio file
            Returns:
                transcript: [string] result from speech to text
        """
        client = speech.SpeechClient()

        self.audio = self.audio.get_wav_data()

        audio = types.RecognitionAudio(content=self.audio)
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code='en-US')

        response = client.recognize(config, audio)
        for result in response.results:
            print(u'Transcript: {}'.format(result.alternatives[0].transcript))
            return result.alternatives[0].transcript

class Text2SpeechRequest:
    def __init__(self, query):
        self.query = query

    def _create_to_speech_request(self):
        """
            Function to create a text to speech request to Google Text-Speech-API
            Args:
                self: contains query in question
            Returns:
                None
        """
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.types.SynthesisInput(text=self.query)
        voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-US', 
            ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL
        )
        audio_config = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.MP3)
        response = client.synthesize_speech(synthesis_input, voice, audio_config)

        with open('output.mp3', 'wb') as out:
        # Write the response to the output file.
            out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

        mixer.init()
        mixer.music.load(os.getcwd() + "/output.mp3")
        mixer.music.play()

if __name__ == "__main__":
    # Uncomment to test out
    s = Speech2TextRequest()
    r = s._create_to_text_request()
    t = Text2CodeRequest(r, HEADERS, PARAMS)
    t._create_to_code_request()
    
    if r is None:
        r = "Something went wrong..."

    t = Text2SpeechRequest(r)
    t._create_to_speech_request() # Currently not working due to 403 error
