from pydub import AudioSegment
from pydub.utils import make_chunks
import pyaudio
import librosa
import pygame
import numpy as np
import pandas as pd
filename = "just fine.mp3"
y, sr = librosa.load(filename)
tempo, beat_frames = librosa.beat.beat_track(y=y,sr=sr)
beat_times=librosa.frames_to_time(beat_frames, sr=sr)
print(type(beat_times))

pd.DataFrame(beat_times).to_csv('beatdata.csv')
