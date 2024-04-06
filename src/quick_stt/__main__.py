import logging
from quick_stt.transcription_loader import load_transcription
import sys
import typing
from quick_stt.config import parse_args


__author__ = "DavidTelenko"
__copyright__ = "DavidTelenko"
__license__ = "MIT"


def setup_logging(loglevel):
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def main(args: typing.List[str]):
    parsed_args = parse_args(args)

    setup_logging(parsed_args.log_level)

    # this is what this script is all about
    print(load_transcription(parsed_args.audio_file))


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
