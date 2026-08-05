from pathlib import Path


class PromptManager:

    BASE_PATH = Path(__file__).parent / "templates"

    @classmethod
    def load(
        cls,
        prompt_name: str,
    ) -> str:

        file_path = cls.BASE_PATH / f"{prompt_name}.txt"

        if not file_path.exists():
            raise FileNotFoundError(f"Prompt '{prompt_name}' not found.")

        return file_path.read_text(encoding="utf-8")
