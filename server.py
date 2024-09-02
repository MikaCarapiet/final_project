"""Server file for app Emotion Detector"""
from flask import Flask, render_template, request
from EmotionAnalysis.emotion_analysis import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    """ Retrieve the text to analyze from the request arguments """
    text_to_analyse = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyse)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    return (
    f"For the given statement, the system response is anger: {anger}, "
    f"disgust: {disgust}, fear: {fear}, joy: {joy}, and sadness: {sadness}. "
    f"The dominant emotion is <b>{response.get(dominant_emotion)}</b>."
)
@app.route("/")
def render_index_page():
    """Function to render index page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    