# Audio extraction

import subprocess
import os

def extract_audio(input_path):
    output_path = "temp/audio.wav"

    cmd = [
        "ffmpeg",
        "-i", input_path,
        "-ac", "1",
        "-ar", "16000",
        output_path,
        "-y"
    ]

    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_path
