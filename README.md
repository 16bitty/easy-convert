# easy-convert
An audio converter that allows for fast and easy conversion between any two formats, while allowing precise control for audiophiles.

## Dependencies

### Python Dependencies
All Python dependencies are managed through the virtual environment and will be installed automatically when you run `./setup.sh`.

### External Dependencies
This tool requires FFmpeg to be installed on your system:

- **Linux**: 
  - Debian/Ubuntu: `sudo apt install ffmpeg`
  - Arch/EndeavourOS: `sudo pacman -S ffmpeg`
- **macOS**: 
  - Using Homebrew: `brew install ffmpeg`
- **Windows**:
  - Using Chocolatey: `choco install ffmpeg`
  - Or download from [FFmpeg's official site](https://ffmpeg.org/download.html)