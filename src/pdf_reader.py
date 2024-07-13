from __future__ import annotations

from io import BytesIO
from typing import List

import httpx
from phi.document.base import Document
from phi.document.reader.pdf import PDFUrlReader
from phi.utils.log import logger
from pypdf import PdfReader as DocumentReader


class PDFAbsractReader(PDFUrlReader):
    """Reader for PDF files from URL"""

    chunk: bool = False

    def read(self, url: str) -> List[Document]:
        if not url:
            raise ValueError("No url provided")

        logger.info(f"Reading: {url}")
        response = httpx.get(url)

        doc_name = (
            url.split("/")[-1]
            .split(".")[0]
            .replace("/", "_")
            .replace(" ", "_")
        )
        doc_reader = DocumentReader(BytesIO(response.content))

        document = Document(
            name=doc_name,
            id=f"{doc_name}_1",
            meta_data={"page": 1},
            content=doc_reader.pages[0]
            .extract_text()
            .partition("Abstract")[-1]
            .partition("1. Introduction")[0],
        )
        return [document]
