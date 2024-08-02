## FunctionDef search_arxiv(query, id_list, max_results, sort_by, sort_order)
**search_arxiv**: The function of search_arxiv is to search for articles on arXiv based on the provided query, ID list, and search parameters.

**parameters**:
- query: A string representing the search query.
- id_list: A list of strings containing specific IDs to search for.
- max_results: An integer indicating the maximum number of results to retrieve.
- sort_by: An enum value from arxiv.SortCriterion to specify the sorting criterion for the search results.
- sort_order: An enum value from arxiv.SortOrder to determine the sorting order of the search results.

**Code Description**:
The search_arxiv function takes in the search parameters such as query, ID list, maximum results, sorting criterion, and sorting order. It initializes an arxiv Client, creates a search object with the provided parameters, and then returns the search results obtained from the client.

In the calling situation within the project, the _get_embeddings function in main.py utilizes search_arxiv to retrieve articles from arXiv based on the specified topic in the configuration. If the number of articles in the embedding holder is less than the configured number of checked articles, it populates the embedding holder with the search results obtained from search_arxiv.

**Note**:
Ensure that the arxiv library is installed in the project environment to use the search_arxiv function successfully.

**Output Example**:
A generator yielding arxiv.Result objects representing the search results from arXiv.
