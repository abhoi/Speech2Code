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

from CONST import CREDENTIAL_FILE_NAME, LUIS_ENDPOINT, HEADERS, PARAMS

PATH = os.getcwd() + CREDENTIAL_FILE_NAME
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "%s" % PATH

class Speech2TextRequest:
    @staticmethod
    def _create_to_text_request():
        """
            Function to record audio from microphone
            Args:
                None
            Returns:
                text: [string] speech to text response string
        """
        r = sr.Recognizer()
        mic = sr.Microphone(device_index=0)
        print("Say something...")
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=1.0)
            audio = r.listen(source)
        print("Audio recorded!")
        return Speech2TextRequest._transcribe_file(audio)

    @staticmethod
    def _transcribe_file(audio):
        """
            Function to call Google Speech-to-Text API to convert speech to text
            Args:
                self: contains audio file
            Returns:
                transcript: [string] result from speech to text
        """
        client = speech.SpeechClient()

        audio = audio.get_wav_data()

        audio = types.RecognitionAudio(content=audio)
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code='en-US')

        response = client.recognize(config, audio)
        for result in response.results:
            print(u'Transcript: {}'.format(result.alternatives[0].transcript))
            return result.alternatives[0].transcript

class Text2CodeRequest:
    @staticmethod
    def _create_to_code_request(query, headers, params):
        """
            Function to create a text to code request to Microsoft Luis
            Args:
                self: contains query, headers, and parameters
            Returns:
                json_response: [dict] a dictionary holding response from Luis including intent classifications
        """
        try:
            params["q"] = query
            r = requests.get(LUIS_ENDPOINT, headers=headers, params=params)
            json_response = r.json()
            print(r.status_code)
            print(json_response)
            return json_response
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

class Text2SpeechRequest:
    @staticmethod
    def _create_to_speech_request(query):
        """
            Function to create a text to speech request to Google Text-Speech-API
            Args:
                self: contains query in question
            Returns:
                None
        """
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.types.SynthesisInput(text=query)
        voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-US', 
            ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL
        )
        audio_config = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.MP3)
        response = client.synthesize_speech(synthesis_input, voice, audio_config)

        with open('output.mp3', 'wb') as out:
            out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

if __name__ == "__main__":
    r = Speech2TextRequest._create_to_text_request()
    t = Text2CodeRequest._create_to_code_request(r, HEADERS, PARAMS)

    # if r is None:
    #     r = "Something went wrong..."

    # t = Text2SpeechRequest(r)
    # t._create_to_speech_request() # Currently not working due to 403 error
