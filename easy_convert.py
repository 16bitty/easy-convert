import subprocess
import sys

def main():
    if not check_ffmpeg():
        sys.exit(1)

def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"],
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       check=True)
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        print("Error: FFmpeg is not installed or not in the PATH.")
        print("Please install FFmpeg to use this program.")
        print("Installation instructions: https://ffmpeg.org/download.html")
        return False

if __name__ == "__main__":
    main()