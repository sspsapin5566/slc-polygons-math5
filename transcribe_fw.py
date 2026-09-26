import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["PATH"] = "/Users/zhangwenbin/miniconda/envs/py311/bin:/Users/zhangwenbin/miniconda/bin:" + os.environ.get("PATH", "")

from pathlib import Path
from faster_whisper import WhisperModel

print("Loading faster-whisper small model with int8 compute on CPU...")
model = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=8)

initial_prompt = "這是一節新北市文林國小五年級數學公開課，主題是認識多邊形，授課教師黃曉雯。討論多邊形、封閉圖形、直線段、頂點、內角、正多邊形、均一教育平台。"

print("Transcribing output/audio.mp3 with faster-whisper...")
segments, info = model.transcribe(
    "output/audio.mp3",
    language="zh",
    initial_prompt=initial_prompt,
    beam_size=1
)

os.makedirs("output", exist_ok=True)

srt_lines = []
txt_lines = []

def format_time(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

for i, seg in enumerate(segments, 1):
    start_str = format_time(seg.start)
    end_str = format_time(seg.end)
    text = seg.text.strip()
    srt_lines.append(f"{i}\n{start_str} --> {end_str}\n{text}\n")
    txt_lines.append(f"[{start_str} -> {end_str}] {text}")

Path("output/subtitles.srt").write_text("\n".join(srt_lines), encoding="utf-8")
Path("output/transcript.txt").write_text("\n".join(txt_lines), encoding="utf-8")

print("faster-whisper transcription completed successfully!")
