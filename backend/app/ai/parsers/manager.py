from pathlib import Path

from app.ai.parsers.csv_parser import CSVParser
from app.ai.parsers.docx_parser import DocxParser
from app.ai.parsers.excel_parser import ExcelParser
from app.ai.parsers.markdown_parser import MarkdownParser
from app.ai.parsers.pdf_parser import PDFParser
from app.ai.parsers.txt_parser import TextParser


class ParserManager:

    PARSERS = {
        ".pdf": PDFParser(),
        ".docx": DocxParser(),
        ".xlsx": ExcelParser(),
        ".csv": CSVParser(),
        ".txt": TextParser(),
        ".md": MarkdownParser(),
    }

    @classmethod
    def parse(
        cls,
        file_path: str,
    ) -> str:

        extension = Path(file_path).suffix.lower()

        parser = cls.PARSERS.get(extension)

        if not parser:
            raise ValueError(f"No parser registered for {extension}")

        return parser.parse(file_path)
