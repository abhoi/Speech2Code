#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
# import httplib
import http.client
import uuid
import json

import speech_recognition as sr

class Microsoft_ASR():
    def __init__(self):
        self.sub_key = '74c16290bd574b09bb279d6f2224fd1d'
        self.token = "4cf3f63793cc4c518648eb2c5ba11ece"
        pass

    def get_speech_token(self):
        FetchTokenURI = "/sts/v1.0/issueToken"
        header = {'Ocp-Apim-Subscription-Key': self.sub_key}
        conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
        body = ""
        conn.request("POST", FetchTokenURI, body, header)
        response = conn.getresponse()
        str_data = response.read()
        conn.close()
        self.token = str_data
        print("Got Token: ", self.token)
        return True

    def transcribe(self,speech_file):

        # Grab the token if we need it
        if self.token is None:
            print("No Token... Getting one")
            self.get_speech_token()

        # endpoint = 'https://speech.platform.bing.com/recognize'
        endpoint = "https://api.cognitive.microsoft.com/sts/v1.0"
        request_id = uuid.uuid4()
        # Params form Microsoft Example 
        params = {'scenarios': 'ulm',
                  'appid': 'cc219f0a-2124-47bd-beb8-cc185bbddf68',
                  'locale': 'en-US',
                  'version': '3.0',
                  'format': 'json',
                #   'instanceid': '565D69FF-E928-4B7E-87DA-9A750B96D9E3',
                  'requestid': uuid.uuid4(),
                  'device.os': 'linux'}
        content_type = "audio/wav; codec=""audio/pcm""; samplerate=16000"

        # def stream_audio_file(speech_file, chunk_size=1024):
        #     with open(speech_file, 'rb') as f:
        #         while 1:
        #             data = f.read(1024)
        #             if not data:
        #                 break
        #             yield data

        headers = {'Authorization': 'Bearer ' + self.token, 
                   'Content-Type': content_type}
        resp = requests.post(endpoint, 
                            params=params, 
                            data=speech_file, 
                            headers=headers)
        print(resp.status_code)
        val = json.loads(resp)
        print(val)
        return val["results"][0]["name"], val["results"][0]["confidence"]

if __name__ == "__main__":
    ms_asr = Microsoft_ASR()
    # ms_asr.get_speech_token()
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=0)
    print("Say something...")
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=1.0)
        audio = r.listen(source)
    print("Audio recorded!")
    # client = speech.SpeechClient()
    audio = audio.get_wav_data()

    text, confidence = ms_asr.transcribe(audio)
    print("Text: ", text)
    print("Confidence: ", confidence)