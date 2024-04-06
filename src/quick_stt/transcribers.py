import pathlib
import quick_stt.config as config
import sys


class whisper:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        import whisper

        if config.model_dir is None:
            print("Models directory not set", file=sys.stderr)
            sys.exit(1)

        model_dir = config.model_dir / "whisper"

        if not model_dir.exists():
            model_dir.mkdir(parents=True)

        self.model = whisper.load_model(
            name=config.model_name,
            download_root=model_dir,
            device=config.model_device,
        )

    def __call__(self, file: pathlib.Path) -> str:
        file_path = str(file)
        result = self.model.transcribe(audio=file_path, fp16=False)["text"]
        if isinstance(result, list):
            return " ".join(result)
        return result


class assemblyai:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        import assemblyai as aai

        aai.settings.api_key = config.transcriber_token

        self.config = aai.TranscriptionConfig(
            punctuate=True,
            format_text=True,
        )
        self.transcriber = aai.Transcriber()

    def __call__(self, file: pathlib.Path) -> str:
        file_path = str(file)
        return self.transcriber.transcribe(file_path, self.config).text or ""
