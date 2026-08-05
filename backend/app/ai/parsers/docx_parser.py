from docx import Document

from app.ai.parsers.base import BaseParser


class DocxParser(BaseParser):

    def parse(
        self,
        file_path: str,
    ) -> str:

        doc = Document(file_path)

        return "\n".join(paragraph.text for paragraph in doc.paragraphs)
