from __future__ import annotations

import arxiv
from phi.document.base import Document


def content_from_arxiv(arxiv_result: arxiv.Result) -> Document:
    """
    Extracts content from an arXiv result and formats it into a Document
    object.
    :param arxiv_result: An arXiv result object containing paper details.
    :return: A Document object containing title, summary, and metadata.
    """
    return Document(
        name=arxiv_result.title,
        content=arxiv_result.summary,
        meta_data={"title": arxiv_result.title, "id": arxiv_result.pdf_url},
    )


def title_from_arxiv(arxiv_result: arxiv.Result) -> Document:
    """
    Extracts the title from an arXiv result and creates a Document object with
    the title and its metadata.
    :param arxiv_result: An arxiv.Result object containing the title and PDF
    URL.
    :return: A Document object containing the title and metadata.
    """
    return Document(
        name=arxiv_result.title,
        content=arxiv_result.title,
        meta_data={"title": arxiv_result.title, "id": arxiv_result.pdf_url},
    )
