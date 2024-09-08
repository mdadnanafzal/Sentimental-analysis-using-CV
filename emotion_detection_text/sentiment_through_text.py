# import nltk
# nltk.download()
from nrclex import *


def emotion_through_text(text):
    emotion = NRCLex(text)
    return emotion.top_emotions

