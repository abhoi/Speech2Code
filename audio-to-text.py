'''
Written by Debojit Kaushik
'''
import os
import sys
import traceback
import pyaudio
import wave
import io
import json

import speech_recognition as sr

from luis_test import Speech2CodeRequest

#Global variables for settings.
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "voice.wav"


headers = {
    # Request headers
    "Ocp-Apim-Subscription-Key": "6a6728b9981d417280f4dad97f82df96",
    # "Ocp-Apim-Subscription-Key": "4cf3f63793cc4c518648eb2c5ba11ece",
    "content-type": "application/json",
}

params = {
    # Query parameter
    # 'q': 'Create a function named getUser with arguments alpha, beta, and gamma which returns a list',
    # Optional request parameters, set to default values
    'timezoneOffset': '0',
    'verbose': 'false',
    'spellCheck': 'false',
    'staging': 'false',
}

def record_speech_stream():
    try:
        from google.cloud import speech
        from google.cloud.speech import enums
        from google.cloud.speech import types

        py_audio = pyaudio.PyAudio()
        
        # stream = py_audio.open(format = FORMAT,channels = CHANNELS,rate = RATE, input = True, frames_per_buffer = CHUNK)

        r = sr.Recognizer()
        mic = sr.Microphone(device_index=0)
        print("Say something...")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        CREDENTIALS = None
        with open("Automaton-c06abc497891.json", "r") as f:
            CREDENTIALS = f.read()
        print("Got audio!")
        print("Sending recognition request...")
        response = r.recognize_google_cloud(audio, credentials_json = CREDENTIALS)
        print(response)
        if "go to" in response:
            response = response.replace("go to", "goto")
        s = Speech2CodeRequest(response, headers, params)
        json_response = s._create_request()
        if "create_variables" == json_response["topScoringIntent"]["intent"]:
            var_name = json_response["entities"][0]["entity"]
            print("%s" % var_name)
        # print("Recording now..")
        # frames = []
        # for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
        #     data = stream.read(CHUNK)
        #     frames.append(data)
        # print("Done Recording!")
        # stream.stop_stream()
        # stream.close()
        # py_audio.terminate()

        # wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        # wf.setnchannels(CHANNELS)
        # wf.setsampwidth(py_audio.get_sample_size(FORMAT))
        # wf.setframerate(RATE)
        # wf.writeframes(b''.join(frames))
        # wf.close()

        # client = speech.SpeechClient()
        # with io.open('voice.wav', 'rb') as audio_file:
        #     content = audio_file.read()
        
        # audio = types.RecognitionAudio(content=content)
        # config = types.RecognitionConfig(
        #     encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        #     sample_rate_hertz = 44100,
        #     language_code = 'en-US'
        # )

        # response = client.recognize(config, audio)
        # for result in response.results:
        #     # The first alternative is the most likely one for this portion.
        #     s = u'Transcript: {}'.format(result.alternatives[0].transcript)
        #     print(s)
        #     params["q"] = str(s)
        #     Speech2CodeRequest(s, headers, params)
    except Exception:
        print(traceback.format_exc())


if __name__ == '__main__':
    try:
        record_speech_stream()
    except Exception:
        print(traceback.format_exc())