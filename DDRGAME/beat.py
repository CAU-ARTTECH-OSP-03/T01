from pydub import AudioSegment
from pydub.utils import make_chunks
import pyaudio
import librosa
import pygame

filename = "just fine.mp3"
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
#beat_frames = beat_frames * 1000 #m to ms
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
