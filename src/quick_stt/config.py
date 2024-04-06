import toml
import pathlib
import argparse
import typing
import logging
import sys
from quick_stt.utility import flatten_dict

from quick_stt import __version__

_logger = logging.getLogger(__name__)

transcriber_name = "whisper"
transcriber_token = None
preprocess_speed = 1.0
preprocess_pitch = 1.0
model_dir = None
model_name = "base"
model_device = "cpu"
log_level = "INFO"


def load_config(config_path: pathlib.Path) -> dict:
    with open(config_path) as f:
        return toml.load(f)


def default_config_dir() -> pathlib.Path:
    import platform
    import os

    return pathlib.Path(
        {
            "Linux": "~/.config/quick-stt/",
            "Darwin": "~/Library/Application Support/quick-stt/",
            "Windows": f"{os.getenv('APPDATA')}\\quick-stt\\",
        }[platform.system()]
    )


def default_config() -> dict:
    return {
        "transcriber": {
            "name": "whisper",
        },
        "preprocess": {
            "speed": 1.0,
            "pitch": 1.0,
        },
        "model": {
            "name": "openai/whisper-base",
            "device": "cpu",
        },
        "log": {
            "level": "INFO",
        },
    }


def create_default_config() -> None:
    config = default_config()
    config_dir = default_config_dir()

    try:
        config_dir.mkdir(parents=True, exist_ok=True)
    except FileExistsError:
        _logger.error(f"Config directory `{config_dir}` already exists as file")
        sys.exit(1)

    config_file = config_dir / "config.toml"

    if config_file.exists():
        return

    with open(config_file, "w") as f:
        toml.dump(config, f)

    (config_dir / "models").mkdir(parents=True, exist_ok=True)


def parse_args(argv: typing.List[str]) -> argparse.Namespace:
    create_default_config()

    defaults = default_config()
    config_dir = default_config_dir()

    with open(config_dir / "config.toml") as f:
        config = toml.load(f)
        defaults.update(config)

    defaults = flatten_dict(defaults)
    defaults["log_level"] = defaults["log_level"].upper()

    defaults["model_dir"] = pathlib.Path(
        defaults.get("model_dir") or config_dir / "models"
    )

    parser = argparse.ArgumentParser(description="Quick SST")

    # TODO: Add streaming capability
    parser.add_argument(
        "audio_file",
        help="Path to the audio file to transcribe",
        type=pathlib.Path,
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"quick-stt {__version__}",
    )
    parser.add_argument(
        "--transcriber-name",
        dest="transcriber_name",
        help="Name of the transcriber to use, it can be default transcriber"
        " for `whisper` or `assemblyai` or a custom transcriber. A custom"
        " transcriber is loaded from <config-directory>/plugins. For detailed"
        " description of how to write own transcriber check docs.",
        type=str,
    )
    parser.add_argument(
        "--transcriber-token",
        dest="transcriber_token",
        help="API token for the transcriber. In case of defalut transcribers"
        " necessary only for `assemblyai`",
        type=str,
    )
    parser.add_argument(
        "--preprocess-speed",
        dest="preprocess_speed",
        help="Speed factor for preprocessing",
        type=float,
    )
    parser.add_argument(
        "--preprocess-pitch",
        dest="preprocess_pitch",
        help="Pitch factor for preprocessing",
        type=float,
    )
    parser.add_argument(
        "--model-dir",
        dest="model_dir",
        help="Directory to save model files",
        type=pathlib.Path,
    )
    parser.add_argument(
        "--model-name",
        dest="model_name",
        help="Name of the model to use",
        type=str,
    )
    parser.add_argument(
        "--model-device",
        dest="model_device",
        help="Device to use for the model",
        choices=["cpu", "gpu"],
    )
    parser.add_argument(
        "--log-level",
        dest="log_level",
        help="Log level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    )

    parser.set_defaults(**defaults)
    config = parser.parse_args(argv)

    if not config.model_dir.exists():
        print(
            f"Model directory `{config.model_dir}` does not exist, expected model `{config.model_name}` to be present",
            file=sys.stderr,
        )
        sys.exit(1)

    if not config.audio_file.exists():
        print(f"Audio file `{config.audio_file}` does not exist", file=sys.stderr)
        sys.exit(1)

    globals().update(config.__dict__)

    return config
