## FunctionDef content_from_arxiv(arxiv_result)
The function of content_from_arxiv is to create a Document object based on the provided arXiv result.

**parameters**:
- arxiv_result: An arxiv.Result object containing information about the arXiv result.

**Code Description**:
The content_from_arxiv function takes an arxiv.Result object as input and constructs a Document object with the following attributes:
- name: The title of the arXiv result.
- content: The summary of the arXiv result.
- meta_data: A dictionary containing metadata information such as the title of the result and its PDF URL.

**Note**:
- Make sure to pass an arxiv.Result object as the input parameter to this function.
- The returned Document object will contain the title, summary, and metadata of the arXiv result.

**Output Example**:
{
    "name": "Title of the arXiv result",
    "content": "Summary of the arXiv result",
    "meta_data": {
        "title": "Title of the arXiv result",
        "id": "PDF URL of the arXiv result"
    }
}
## FunctionDef title_from_arxiv(arxiv_result)
**title_from_arxiv**: The function of title_from_arxiv is to create a Document object based on the provided arXiv result.

**parameters**:
- arxiv_result: An arxiv.Result object containing information about the arXiv result.

**Code Description**:
The title_from_arxiv function takes an arXiv result as input and constructs a Document object with the name, content, and meta_data fields populated based on the information from the arXiv result. The name and content of the Document are set to the title of the arXiv result, while the meta_data field is a dictionary containing the title of the result and its PDF URL.

In the project, this function is called within the _get_embeddings function in main.py. When _get_embeddings is executed, it creates a vector database and inserts Document objects created by title_from_arxiv based on the search results from arXiv. The function then returns the embeddings of the inserted documents.

**Note**:
Ensure that the arxiv_result parameter is an instance of arxiv.Result to avoid any potential errors.

**Output Example**:
```python
Document(
    name="Sample Title",
    content="Sample Title",
    meta_data={"title": "Sample Title", "id": "https://sample-url.com"}
)
```
