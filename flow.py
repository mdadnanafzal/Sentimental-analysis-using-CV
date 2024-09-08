from emotion_detection_text import sentiment_through_text as senttex
import testemotiondetector_trial as sentcv
from voica import *
from Music_recom import *
import pyjokes


def generate_sentiment_code(pred_emotion):
    if pred_emotion == 'Happy' or pred_emotion == 'Surprised' or pred_emotion == 'joy' or pred_emotion == 'trust' or pred_emotion == 'positive' or pred_emotion == 'Neutral':
        return 1
    else:
        return 0


def display_manuscript():
    print("send email\nplay song on spotify\nopen youtube\nopen google")


wishMe()
name()
query = takeCommand()
emotion_text = senttex.emotion_through_text(query)
emotion_text_code = generate_sentiment_code(emotion_text[0][0])
print(f"Sentiment from text\nEmotion : {emotion_text}\nSentiment value : {emotion_text_code}")
emotion_cv = ''
emotion_cv_code = 0
right_choice = False
while not right_choice:
    speak("May i look at you")
    choice = takeCommand().lower()
    if 'yes' in choice or 'sure' in choice or 'alright' in choice:
        emotion_cv = sentcv.emotion_from_face_detection()
        emotion_cv_code = generate_sentiment_code(emotion_cv)
        right_choice = True
    elif 'no' in choice:
        emotion_cv = 0
        right_choice = True
    elif 'maybe' in choice:
        speak("i am accessing cam to look at you!")
        emotion_cv = sentcv.emotion_from_face_detection()
        emotion_cv_code = generate_sentiment_code(emotion_cv)
        right_choice = True
    else:
        speak("I didn't understand that")
print(f"Sentiment from cv\nEmotion : {emotion_cv}\nSentiment value : {emotion_cv_code}")
speak("You look amazing")
if emotion_text_code != emotion_cv_code:
    speak("Oh! i seem to have detected some sarcasm")
    joke = pyjokes.get_joke()
    speak(joke)

if emotion_cv_code == 1:
    speak("You are in a jolly good mood today, "
          'Shall i suggest some songs to further energize your mood ')
    right_choice = False
    while not right_choice:
        choice = takeCommand()
        if 'yes' in choice or 'sure' in choice or 'alright' in choice or 'ok' in choice:
            song = Recommend_Song(emotion_cv)
            print(song)
            speak(f"You can listen to {song}")
            right_choice = True
        elif choice == 'no':
            right_choice = True
        else:
            speak("I didn't understand that")
elif emotion_cv_code == 0:
    speak("You are distressed about something,"
          'Shall i suggest some songs to help you calm down a bit ?')
    right_choice = False
    while not right_choice:
        choice = takeCommand()
        if 'yes' in choice or 'sure' in choice or 'alright' in choice or 'ok' in choice:
            song = Recommend_Song(emotion_cv)
            print(song)
            speak(f"You can listen to {song}")
            right_choice = True
        elif choice == 'no':
            right_choice = True
        else:
            speak("I didn't understand that")

speak("Is there anything else i can help you with")

