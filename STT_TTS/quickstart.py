#!/usr/bin/env python

# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Text-To-Speech API sample application .

Example usage:
    python quickstart.py
"""
import os
import playsound
from google.cloud import texttospeech

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='./speech-to-text-292808-d4d23dae896a.json'

COUNT = 0

def play_and_remove(response):
    global COUNT
    OUTPUT = str(COUNT) + 'output.mp3'
    COUNT+=1
    # The response's audio_content is binary.
    with open(OUTPUT, "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
    # [END tts_quickstart]

    playsound.playsound(OUTPUT, True)
    os.remove(OUTPUT)

def call_tts(sentence):

    sentence = input('말하고 싶은 텍스트를 입력하세요. : ')

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=sentence)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="ko-KR", ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    play_and_remove(response)

if __name__ == "__main__":
    run_quickstart()
