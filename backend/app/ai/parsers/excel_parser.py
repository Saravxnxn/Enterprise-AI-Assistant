import pandas as pd

from app.ai.parsers.base import BaseParser


class ExcelParser(BaseParser):

    def parse(
        self,
        file_path: str,
    ) -> str:

        excel = pd.ExcelFile(file_path)

        text = ""

        for sheet in excel.sheet_names:

            df = pd.read_excel(
                file_path,
                sheet_name=sheet,
            )

            text += f"Sheet: {sheet}\n"

            text += df.to_string(index=False)

            text += "\n\n"

        return text
