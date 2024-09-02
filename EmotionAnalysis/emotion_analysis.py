"""Module providing a function detecting emotion of a string of text."""
# pylint: disable=line-too-long
import json
import requests

def emotion_detector(text_to_analyse):
    """Function that detects the emotion of a string of text."""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id":
              "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header, timeout=10)
    formatted_response = json.loads(response.text)
    anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    dominant_emotion = max(formatted_response['emotionPredictions'][0]['emotion'],key=formatted_response['emotionPredictions'][0]['emotion'].get)

    return {'anger': anger, 'disgust': disgust,'fear': fear,'joy': joy,'sadness': sadness,'dominant_emotion': dominant_emotion}
