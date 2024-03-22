import argparse
import os
from dotenv import load_dotenv, find_dotenv
from deepgram import DeepgramClient, PrerecordedOptions, FileSource
from deepgram_captions import DeepgramConverter, webvtt, srt
import mimetypes

load_dotenv(find_dotenv())
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")


def transcribe_audio(audio_file_path, model="nova-2", response_format="vtt"):
    audio_file_dir = os.path.dirname(audio_file_path)
    transcript_file_name = (
        f"{os.path.splitext(os.path.basename(audio_file_path))[0]}.{response_format}"
    )
    transcript_file_path = os.path.join(audio_file_dir, transcript_file_name)

    mimetype = mimetypes.guess_type(audio_file_path)[0]

    with open(audio_file_path, "rb") as audio_file:
        deepgram = DeepgramClient(DEEPGRAM_API_KEY)
        source: FileSource = {"buffer": audio_file, "mimetype": mimetype}
        options = PrerecordedOptions(
            smart_format=True,
            utterances=True,
            model=model,
            punctuate=True,
            diarize=True,
        )

        response = deepgram.listen.prerecorded.v("1").transcribe_file(source, options)

        converter = DeepgramConverter(response)

        transcript = ""
        if response_format == "vtt":
            transcript = webvtt(converter)
        elif response_format == "srt":
            transcript = srt(converter)
        else:
            transcript = response.to_json()

        with open(transcript_file_path, "w") as transcript_file:
            transcript_file.write(transcript)

    return transcript_file_path


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe an audio file using Deepgram's API."
    )
    parser.add_argument(
        "audio_file_path", help="The path to the audio file to transcribe."
    )
    parser.add_argument(
        "-m",
        "--model",
        default="nova-2",
        help="The model of Deepgram. Can be 'nova', 'enhanced', 'base', 'whisper', etc.",
    )
    parser.add_argument(
        "-f",
        "--format",
        default="vtt",
        help="The format of the transcription. Can be 'vtt', 'srt', 'text', etc.",
    )
    args = parser.parse_args()

    transcript_file_path = transcribe_audio(
        args.audio_file_path, model=args.model, response_format=args.format
    )

    print(f"Transcription saved to: {transcript_file_path}")


if __name__ == "__main__":
    main()
