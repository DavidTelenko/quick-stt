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

[model]
name = "base" # particular model to use, customization point for each model
              # (you need to take a look at the model's documentation to see what models are
              # available)
device = "cpu" # device to use for inference, can be `cpu` or `gpu`

[log]
level = "INFO" # logging level, can be `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`
```

# Note

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.
