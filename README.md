This package includes a Python3 port of purdy/aws-transcribe-transcript intended to parse Amazon Transcribe JSONs and make them more human readable, and a script to make an Amazon Transcribe SRT more human readable.

# aws-transcribe-transcript

Amazon has a neat Transcription service and you can have the service identify speakers. And in their web interface, they show you a neat play-by-play transcript, but it's limited to the first 5,000 characters. If you want the full transcript, you have to download their JSON file. However, the JSON file only has the transcript as a big block and then some structured data below for the various speakers, start times, and text fragments.

This script creates a transcript that's human-readable.

## Regular JSON Directions

1. Download your Transcription from the Job Details page. The filename format is currently asrOutput.json.
2. Run the `transcript.py` program on the downloaded file, i.e. `python3 ./transcript.py asrOutput.json`
3. Results will be written in your current working directory as `[FILENAME]-transcript.txt`

## S3/Lambda JSON Directions

0. Probably worth checking your lambda Memory/Execution time settings, depending on the size of the files you'll work with. I like ~256MB and ~15 seconds for general use.
1. Create an S3 bucket with two folders; input/ and output/
2. Create a Lambda function that triggers on CreateObject in input/ (Triggers section of the UI)
3. Give the function access to write to S3/output (Resources section of the UI)
4. Place json file in S3/input and wait a few seconds for your transcript to show up in output/

## SRT directions

1. Download your SRT from the Job Details page. The filename format is srtSubtitles.srt.
2. Run the 'srt*to*...py" script appropriate for your desired output
3. For MMM:SS an example would be `python3 srt_to_mmmss.py srtSubtitles.srt`
4. For HH:MM:SS an example would be `python3 srt_to_hhmmss.py srtSubtitles.srt`
5. For H:M:SS `python3 srt_to_hmss.py srtSubtitles.srt`
