from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH
import soundfile as sf
import pandas as pd

audio_path = "the_mountain-background-music-159125.mp3"

model_output, midi_data, note_events = predict(audio_path)

with open("output.mid", "wb") as f:
    midi_data.write(f)

df = pd.DataFrame(note_events)
df.to_csv("note_events.csv", index=False)