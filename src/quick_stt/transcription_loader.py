from quick_stt import config
from quick_stt.utility import print_time
import pathlib
import quick_stt.transcribers as transcribers
from quick_stt.utility import time_this


@time_this(print_time)
def load_transcription(file: pathlib.Path) -> str:
    return vars(transcribers)[config.transcriber_name.lower()]()(file)
