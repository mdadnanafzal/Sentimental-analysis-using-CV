import pandas as pd
from random import *
import os
import sys
import testemotiondetector_trial

Music_Player = pd.read_csv("data_moods.csv")
Music_Player = Music_Player[['name', 'artist', 'mood', 'popularity']]


def return_mainstream_song(play):
    random_row = choice(play.index)
    return play['name'].iloc[random_row]


def Recommend_Song(pred_class):
    random_song = ''
    if pred_class == 'Disgust':
        Play = Music_Player[Music_Player['mood'] == 'Sad']
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play.reset_index()
        random_song = return_mainstream_song(Play)

    if pred_class == 'Happy' or pred_class == 'Sad':
        Play = Music_Player[Music_Player['mood'] == 'Happy']
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play.reset_index()
        random_song = return_mainstream_song(Play)

    if pred_class == 'Fear' or pred_class == 'Angry':
        Play = Music_Player[Music_Player['mood'] == 'Calm']
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play.reset_index()
        random_song = return_mainstream_song(Play)

    if pred_class == 'Surprise' or pred_class == 'Neutral':
        Play = Music_Player[Music_Player['mood'] == 'Energetic']
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play.reset_index()
        random_song = return_mainstream_song(Play)

    return random_song

#print(Recommend_Song('Happy'))

