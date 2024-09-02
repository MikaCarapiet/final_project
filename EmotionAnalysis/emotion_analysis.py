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
    
    if response.status_code == 200:
        emotions_list=formatted_response['emotionPredictions'][0]['emotion']
        anger = emotions_list['anger']
        disgust = emotions_list['disgust']
        fear = emotions_list['fear']
        joy = emotions_list['joy']
        sadness = emotions_list['sadness']
        dominant_emotion = max(emotions_list,key=emotions_list.get)
    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None

    return {'anger': anger, 'disgust': disgust,'fear': fear,'joy': joy,'sadness': sadness,'dominant_emotion': dominant_emotion}
