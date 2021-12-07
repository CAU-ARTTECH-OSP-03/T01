from pydub import AudioSegment
from pydub.utils import make_chunks
import pyaudio
import librosa
import numpy as np

song_path = 'powerup.mp3'
chunk_size = 20  # ms

y, sr = librosa.load(song_path, duration=None)
tempo, beats = librosa.beat.beat_track(y=y, sr=sr, trim=False, units='time')
beats = beats * 1000

# print(beats)
song = AudioSegment.from_file(song_path)
p = pyaudio.PyAudio()
stream = p.open(
    format=p.get_format_from_width(song.sample_width),
    channels=song.channels,
    rate=song.frame_rate,
    output=True
)

time_counter = 0  # ms
for chunk in make_chunks(song, chunk_size):
    time_counter += chunk_size
    stream.write(chunk._data)

    if len(beats) > 0:
        if time_counter <= beats[0] < time_counter + chunk_size:
            # print("\n\n\n\n\nenter!")
            beats = beats[1:]
            print(beats)
            input()

stream.stop_stream()
stream.close()
p.terminate()