import sys
from quick_stt import config
import pathlib
import quick_stt.transcribers as transcribers
from quick_stt.utility import time_this


def print_time(time):
    print(
        f"Transcription generation took: {time}s",
        file=sys.stderr,
    )


@time_this(print_time)
def load_transcription(file: pathlib.Path) -> str:
    return vars(transcribers)[config.transcriber_name]()(file)
