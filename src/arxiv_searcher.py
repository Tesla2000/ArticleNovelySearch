from __future__ import annotations

from typing import Generator
from typing import List

import arxiv


def search_arxiv(
    query: str = "",
    id_list: List[str] = None,
    max_results: int | None = 10,
    sort_by: arxiv.SortCriterion = arxiv.SortCriterion.Relevance,
    sort_order: arxiv.SortOrder = arxiv.SortOrder.Descending,
) -> Generator[arxiv.Result, None, None]:
    id_list = id_list or []
    client = arxiv.Client()

    search = arxiv.Search(query, id_list, max_results, sort_by, sort_order)

    return client.results(search)
