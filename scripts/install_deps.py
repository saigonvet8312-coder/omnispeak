"""Cài hệ thống + Python package cho OmniSpeak."""

import sys

from colab_utils import run

APT_PACKAGES = ["ffmpeg", "libsndfile1"]
PIP_PACKAGES = ["omnivoice", "fastapi", "uvicorn[standard]", "python-multipart", "soundfile"]


def main():
    run(f"apt-get -qq update && apt-get -qq install -y {' '.join(APT_PACKAGES)}",
        "cài gói hệ thống")
    run([sys.executable, "-m", "pip", "install", "-q", *PIP_PACKAGES],
        "cài Python package")
    run([sys.executable, "-c",
         "from omnivoice import OmniVoice, VoiceClonePrompt; import fastapi, soundfile; print('OK')"],
        "kiểm tra import")


if __name__ == "__main__":
    main()
