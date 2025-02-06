# YouTube Playlist Downloader Tool

A comprehensive toolkit for downloading YouTube playlists, consisting of two main applications:
1. Playlist URL Extractor
2. Batch Video Downloader

## Features

### Playlist URL Extractor (playlist_extractor.py)
- Clean and intuitive graphical user interface
- Automatic extraction of all video URLs from a playlist
- Saves results to a text file
- Built-in error handling and user feedback
- Cross-platform compatibility

### Batch Video Downloader (batch_downloader.py)
- User-friendly GUI
- Customizable download directory
- Powered by yt-dlp for reliable downloads
- Firefox cookies support (enables member-only content download)
- Real-time download progress tracking
- Batch processing capabilities

## System Requirements

- Python 3.6 or higher
- Firefox browser (for cookies)
- Compatible with Windows/macOS/Linux

## Installation

1. Clone the repository:
```bash
git clone https://github.com/LostSunset/youtube-playlist-downloader.git
cd youtube-playlist-downloader
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage Instructions

### Step 1: Extract Playlist URLs

1. Launch the Playlist URL Extractor:
```bash
python playlist_extractor.py
```

2. Enter your YouTube playlist URL in the popup window
3. Click "Extract URLs"
4. The program will generate a `playlist_urls.txt` file in the same directory

### Step 2: Download Videos

1. Launch the Batch Downloader:
```bash
python batch_downloader.py
```

2. Click "Select Download Location" to choose your target directory
3. Click "Select URL List File" to load the previously generated `playlist_urls.txt`
4. Click "Start Download" and wait for completion

## Creating Executables

Generate standalone executables using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile playlist_extractor.py
pyinstaller --onefile batch_downloader.py
```

Executable files will be created in the `dist` directory.

## FAQ

### Q: Why is Firefox required?
A: The program utilizes Firefox cookies to support downloading member-only content. For public videos only, you can modify the code to remove cookie dependencies.

### Q: How can I improve download speeds?
A: Try updating yt-dlp to the latest version:
```bash
pip install --upgrade yt-dlp
```

### Q: What should I do if I encounter errors?
A: Submit an issue on GitHub with the following information:
- Operating system
- Python version
- Error message
- Steps to reproduce

## Contributing

Pull requests are welcome! Please ensure:
1. Code follows PEP 8 style guide
2. New features include proper error handling
3. Documentation is updated accordingly

## Development Setup

1. Fork and clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -r requirements.txt
```

## Testing

Currently, manual testing is required for:
- GUI functionality
- Download capabilities
- Error handling
- Cross-platform compatibility

## Roadmap

Future improvements planned:
- [ ] Add support for other browsers
- [ ] Implement download queue management
- [ ] Add video quality selection
- [ ] Create progress bars for individual downloads
- [ ] Add support for other video platforms

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### v1.0.0 (2024-02-06)
- Initial release
- Basic functionality implementation
- Documentation added

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for the download functionality
- [pytube](https://github.com/pytube/pytube) for playlist parsing
- All contributors and users of this project

## Support

For support, please:
1. Check the FAQ section
2. Search existing issues
3. Create a new issue if needed

## Project Status

Active development - Bug reports and feature requests are welcome!