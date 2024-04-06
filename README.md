![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)

# quick-stt

Quickly written speech-to-text (STT) cli client for various STT backends.

The main idea behind this project is to create simple cli app that can be used
to quickly convert speech to text using various STT backends. The project is
still in early development stage and is not yet ready for production use.

## Configuration

App is configured using default locations for configuration files.

- Windows: `C:\Users\<username>\AppData\Roaming\quick-stt\config.toml`
- Linux: `~/.config/quick-stt/config.toml`
- MacOS: `~/Library/Application Support/quick-stt/config.toml`

Example configuration file:

```toml
[transcriber]
name = "whisper" # the name of the transcriber to use, for now can be `whisper` or `assemblyai`
token = "your-api-token" # the api token for the transcriber if needed
dir = "models dir" # defaults to <config-path>/models

[model]
name = "base" # particular model to use, customization point for each model
              # (you need to take a look at the model's documentation to see what models are
              # available)
device = "cpu" # device to use for inference, can be `cpu` or `gpu`

[log]
level = "INFO" # logging level, can be `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`
```

## CLI Parameters

This is as simple as writing `qstt --help`. Here is the message you will
receive.

```
usage: qstt [-h] [--version] [--transcriber-name TRANSCRIBER_NAME] [--transcriber-token TRANSCRIBER_TOKEN]
            [--preprocess-speed PREPROCESS_SPEED] [--preprocess-pitch PREPROCESS_PITCH] [--model-dir MODEL_DIR] [--model-name MODEL_NAME]
            [--model-device {cpu,gpu}] [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
            audio_file

Quick SST

positional arguments:
  audio_file            Path to the audio file to transcribe

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --transcriber-name TRANSCRIBER_NAME
                        Name of the transcriber to use, it can be default transcriber for `whisper` or `assemblyai` or a custom transcriber. A
                        custom transcriber is loaded from <config-directory>/plugins. For detailed description of how to write own transcriber
                        check docs.
  --transcriber-token TRANSCRIBER_TOKEN
                        API token for the transcriber. In case of defalut transcribers necessary only for `assemblyai`
  --preprocess-speed PREPROCESS_SPEED
                        Speed factor for preprocessing
  --preprocess-pitch PREPROCESS_PITCH
                        Pitch factor for preprocessing
  --model-dir MODEL_DIR
                        Directory to save model files
  --model-name MODEL_NAME
                        Name of the model to use
  --model-device {cpu,gpu}
                        Device to use for the model
  --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Log level
```

Several arguments are not used for now and only those which are mentioned in
configuration section above will take affect. Generally as in all sane CLI apps
the parameters you provide in cli itself will take precedence over
configuration values.

## Installation

For now this package is in too early stage to be published so you only can
install it from local sources. Thanks to PyScaffold it is as simple as this:

```
cd quick-stt
pip install .
```

After this script will be available by the name `qstt`.

## Examples

Simple transcribe job

```
qstt my:/audio/file.mp3
Transcription generation took: 2.66045069694519s
Hello there this is me talking.
```

Change transcriber and token from command prompt.

```
qstt my:/audio/file.mp3 \
    --transcriber-token asd8fdfa87asdf8 \
    --transcriber-name assemblyai
Transcription generation took: 1.71381411445512s
Hello there this is me talking.
```

## Future plans

- Fix GPU issues with whisper model
- Make it faster
- Make it work with audio streams and binary data
- Create plugin system, and give users ability to write their own transcribers
- Make CLI more beautiful

## Note

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.
