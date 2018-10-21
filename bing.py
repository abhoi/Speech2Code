import json
import requests

import speech_recognition as sr

YOUR_API_KEY = '74c16290bd574b09bb279d6f2224fd1d'
YOUR_AUDIO_FILE = 'output.mp3'
REGION = 'northeurope' # westus, eastasia, northeurope 
MODE = 'interactive'
LANG = 'en-US'
FORMAT = 'simple'


def handler():
    # 1. Get an Authorization Token
    token = get_token()
    # 2. Perform Speech Recognition
    results = get_text(token, YOUR_AUDIO_FILE)
    # 3. Print Results
    print(results)

def get_token():
    # Return an Authorization Token by making a HTTP POST request to Cognitive Services with a valid API key.
    url = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'
    headers = {
        'Ocp-Apim-Subscription-Key': YOUR_API_KEY
    }
    r = requests.post(url, headers=headers)
    token = r.content
    return(token)

def get_text(token, audio):
    # Request that the Bing Speech API convert the audio to text
    # url = 'https://{0}.stt.speech.microsoft.com/speech/recognition/{1}/cognitiveservices/v1?language={2}&format={3}'.format(REGION, MODE, LANG, FORMAT)
    url = "https://api.cognitive.microsoft.com/sts/v1.0"
    headers = {
        'Accept': 'application/json',
        'Ocp-Apim-Subscription-Key': YOUR_API_KEY,
        'Transfer-Encoding': 'chunked',
        'Content-type': 'audio/wav; codec=audio/pcm; samplerate=16000',
        'Authorization': 'Bearer {0}'.format(token)
    }
    r = requests.post(url, headers=headers, data=stream_audio_file(audio))
    print(r.status_code)
    results = json.loads(r.content)
    return results

def get_audio():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=0)
    print("Say something...")
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=1.0)
        audio = r.listen(source)
    print("Audio recorded!")
    with open('output.mp3', 'wb') as out:
        out.write(audio.get_wav_data())

def stream_audio_file(speech_file, chunk_size=1024):
    # Chunk audio file
    get_audio()
    with open(speech_file, 'rb') as f:
        while 1:
            data = f.read(1024)
            if not data:
                break
            yield data

if __name__ == '__main__':
    handler()