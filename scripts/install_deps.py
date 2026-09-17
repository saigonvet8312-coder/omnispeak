"""Cài hệ thống + Python package cho OmniSpeak."""

import sys

from colab_utils import run

APT_PACKAGES = ["ffmpeg", "libsndfile1"]


def _already_installed():
    try:
        import fastapi  # noqa: F401
        import soundfile  # noqa: F401
        import omnivoice  # noqa: F401
        return True
    except ImportError:
        return False


def main(requirements_path=None, force=False):
    if not force and _already_installed():
        print("Đã cài đủ package — bỏ qua bước cài đặt.")
        print("(Muốn cài lại từ đầu: gọi main(force=True))")
        return

    run(f"apt-get -qq update && apt-get -qq install -y {' '.join(APT_PACKAGES)}",
        "cài gói hệ thống")

    if not requirements_path:
        raise SystemExit(
            "Thiếu requirements_path — truyền đường dẫn tới backend/requirements.txt."
        )
    run([sys.executable, "-m", "pip", "install", "-q", "-r", requirements_path],
        "cài Python package từ requirements.txt")

    run([sys.executable, "-c",
         "from omnivoice import OmniVoice, VoiceClonePrompt; import fastapi, soundfile; print('OK')"],
        "kiểm tra import")


if __name__ == "__main__":
    main()
