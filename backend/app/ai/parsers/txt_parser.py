from app.ai.parsers.base import BaseParser


class TextParser(BaseParser):

    def parse(
        self,
        file_path: str,
    ) -> str:

        with open(
            file_path,
            encoding="utf-8",
        ) as f:

            return f.read()
