import os
import sys

os.environ["PATH"] = "/Users/zhangwenbin/miniconda/envs/py311/bin:/Users/zhangwenbin/miniconda/bin:" + os.environ.get("PATH", "")

import torch
import whisper

print("Loading Whisper small model on CPU with beam_size=1...")
model = whisper.load_model("small", device="cpu")

initial_prompt = "這是一節新北市文林國小五年級數學公開課，主題是認識多邊形，授課教師黃曉雯。討論多邊形、封閉圖形、直線段、頂點、內角、正多邊形、均一教育平台。"

print("Transcribing audio fast...")
result = model.transcribe(
    "output/audio.mp3",
    language="zh",
    initial_prompt=initial_prompt,
    fp16=False,
    beam_size=1,
    verbose=False
)

os.makedirs("output", exist_ok=True)

with open("output/transcript.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

with open("output/subtitles.srt", "w", encoding="utf-8") as f:
    for i, segment in enumerate(result.get("segments", []), 1):
        start = format_timestamp(segment["start"])
        end = format_timestamp(segment["end"])
        text = segment["text"].strip()
        f.write(f"{i}\n{start} --> {end}\n{text}\n\n")

print("Transcription complete successfully!")
