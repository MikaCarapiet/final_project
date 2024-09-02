"""Server file for app Emotion Detector"""
from flask import Flask, render_template, request
import json
from EmotionAnalysis.emotion_analysis import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyse = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyse)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = ['dominant_emotion']

    # Return a formatted string with the sentiment label and score
    return "For the given statement, the system response is {} , {} , {} , {} and {}. The dominant emotion is <b>{}</b>.".format({'anger': anger},{'disgust': disgust},{'fear': fear},{'joy': joy},{'sadness': sadness},response.get('dominant_emotion'))

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    