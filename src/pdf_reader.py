from __future__ import annotations

import arxiv
from phi.document.base import Document


def content_from_arxiv(arxiv_result: arxiv.Result) -> Document:
    return Document(
        name=arxiv_result.title,
        content=arxiv_result.summary,
        meta_data={"title": arxiv_result.title, "id": arxiv_result.pdf_url},
    )


def title_from_arxiv(arxiv_result: arxiv.Result) -> Document:
    return Document(
        name=arxiv_result.title,
        content=arxiv_result.title,
        meta_data={"title": arxiv_result.title, "id": arxiv_result.pdf_url},
    )
