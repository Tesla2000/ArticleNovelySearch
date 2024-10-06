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
    """
    Searches the arXiv database for papers based on a query and specified
    parameters.
    :param max_results: The maximum number of results to return from the
    search.
    :param query: The search query string to find relevant papers.
    :param sort_order: The order in which to sort the results (ascending or
    descending).
    :param sort_by: The criterion by which to sort the results (e.g., relevance
    or date).
    :param id_list: A list of specific arXiv IDs to include in the search.
    :return: A generator of arXiv search results.
    """
    print("log if it got here")
    id_list = id_list or []
    client = arxiv.Client()

    search = arxiv.Search(query, id_list, max_results, sort_by, sort_order)

    return client.results(search)
