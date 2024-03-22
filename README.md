# Deepgram Caption Generator

This Python script utilizes Deepgram's advanced speech recognition API to transcribe audio files and generate captions in WebVTT (`.vtt`) or SubRip (`.srt`) formats. It supports multiple Deepgram transcription models, providing flexibility to achieve the best accuracy for various audio types and use cases. This tool is perfect for content creators, podcasters, and anyone looking to enhance their audio content with accurate and easily integrated captions.

## Features

- Transcribe audio files using Deepgram's state-of-the-art speech-to-text API.
- Generate captions in either WebVTT or SubRip format.
- Choose from a variety of Deepgram transcription models.
- Output transcription in `.vtt`, `.srt`, or plain text format.

## Prerequisites

- Python 3.10 or later
- A Deepgram account and API key. Sign up [here](https://console.deepgram.com/signup) to obtain your API key.

## Installation

1. Clone this repository or download the files to your local machine.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Deepgram API key like so:

```
DEEPGRAM_API_KEY='your_deepgram_api_key_here'
```

## Usage

Navigate to the `src/` directory and run the script from the command line, specifying the audio file path and optional parameters for the transcription model and output format.

```bash
python transcribe_and_caption.py path_to_your_audio_file -m model_name -f output_format
```

- `path_to_your_audio_file`: The path to the audio file you want to transcribe.
- `model_name` (optional): The Deepgram model to use for transcription. Defaults to `nova-2`.
- `output_format` (optional): The format of the transcription output. Can be `vtt`, `srt`, or `text`. Defaults to `vtt`.

Example:

```bash
python src/transcribe_and_caption.py ./audio/sample.mp3
```

This command will transcribe the `sample.mp3` file using the `nova-2` model and save the captions in WebVTT format.

## Supported Audio Formats

Deepgram supports a wide range of audio formats. For optimal results, use audio files in MP3, WAV, or FLAC format.

## Note

Ensure your audio file is accessible and the path is correct. Network issues or incorrect API keys may lead to transcription failures.
