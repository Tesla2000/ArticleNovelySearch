## ClassDef EmbeddingHolder
**EmbeddingHolder**: The function of EmbeddingHolder is to manage embeddings in a database, including retrieving, inserting, and filtering documents.

**attributes**:
- get_embeddings: Retrieves embeddings from the database based on specified criteria.
- insert: Inserts documents into the database in batches.
- _insert: Internal method to insert a single document into the database.
- filter_documents: Filters documents based on existing metadata in the database.
- get_table: Returns the database table structure for the embeddings.

**Code Description**:
The EmbeddingHolder class provides methods to interact with a database storing embeddings. The `get_embeddings` method retrieves embeddings from the database, with options to limit the number of results and use a custom embedder. The `insert` method inserts documents into the database in batches, utilizing threading for efficiency. The `_insert` method is an internal function to insert a single document. The `filter_documents` method filters input documents based on existing metadata in the database to avoid duplicates. Lastly, the `get_table` method returns the database table structure for the embeddings.

In the project, the main function utilizes EmbeddingHolder to manage embeddings. The `_get_embeddings` function calls the `create`, `insert`, and `get_embeddings` methods of EmbeddingHolder to handle embedding retrieval and insertion. The `_print_uniqueness` function also interacts with EmbeddingHolder to calculate uniqueness rankings based on embeddings.

**Note**: Ensure proper configuration of the database connection and embedder before using the EmbeddingHolder class methods.

**Output Example**:
```python
(np.ndarray(embeddings), list[dict[str, str]](metadata))
```
### FunctionDef get_embeddings(self, limit, embedder)
**get_embeddings**: The function of get_embeddings is to retrieve embeddings from a database, with an option to use a specified Embedder object for embedding text data.

**parameters**:
- self: The instance of the EmbeddingHolder class.
- limit: An integer specifying the maximum number of embeddings to retrieve.
- embedder: An optional Embedder object used for embedding text data.

**Code Description**:
The get_embeddings function interacts with a database session to fetch embeddings and associated metadata. If no embedder is provided, it retrieves embeddings directly from the database. If an embedder is specified, it uses the embedder to calculate embeddings based on the content fetched from the database. The function returns the embeddings as a NumPy array and the metadata as a list of dictionaries.

This function is called by the _get_embeddings function in the main.py module. The _get_embeddings function initializes the database, inserts data if needed, and then calls get_embeddings to retrieve the embeddings based on the specified configuration.

The get_embeddings function also has a relationship with the Embedder class defined in embedder.py. Embedder provides a base class for embedding text data, and subclasses such as TFEmbedder and TFIDFEmbedder implement the get_embeddings method to calculate embeddings using different vectorization techniques.

**Note**:
Developers can use this function to retrieve embeddings from a database and customize the embedding process by providing their own Embedder implementation.

**Output Example**:
(np.ndarray([embedding1, embedding2, ...]), [metadata1, metadata2, ...])
***
### FunctionDef insert(self, documents, batch_size)
**insert**: The function of insert is to process a collection of documents, filter them, and insert the valid ones into a PostgreSQL database table in batches for efficient handling.

**parameters**:
- documents: Iterable[Document] - A collection of documents to be processed and inserted.
- batch_size: int - The size of each batch for processing documents.

**Code Description**:
The insert function first filters the input documents using the filter_documents method to ensure that only new documents are considered for insertion. It then creates batches of documents and processes each batch concurrently by creating separate threads for each document. Within each thread, the _insert function is called to insert the document information into the database table after necessary processing. Once all documents in a batch have been processed, the changes are committed to the database.

**Note**:
It is essential to provide Document objects with complete information required for insertion into the database when using the _insert function. The use of threads in the insert function allows for parallel processing of document insertion, enhancing the efficiency of handling large batches of documents.
***
### FunctionDef _insert(self, document, sess)
**_insert**: The function of _insert is to insert document information into a PostgreSQL database table after processing and cleaning the content.

**parameters**:
- document: Represents the document object containing information to be inserted.
- sess: Represents the session object for interacting with the database.

**Code Description**:
The `_insert` function takes a `Document` object and a database session `sess` as parameters. It first embeds the document using an embedder, replaces any null bytes in the content with a replacement character, calculates the MD5 hash of the cleaned content, and then constructs an SQL statement to insert the document information into a PostgreSQL table. Finally, it executes the statement using the provided session.

In the calling object `insert`, batches of documents are processed, and for each batch, a separate thread is created to call the `_insert` function for each document in the batch. This allows for parallel processing of document insertion. Once all documents in a batch have been processed, the changes are committed to the database.

**Note**:
It's important to ensure that the `Document` object passed to `_insert` contains all the necessary information required for insertion into the database table. Additionally, the use of threads in the `insert` function enables concurrent processing of document insertion, improving efficiency for handling large batches of documents.
***
### FunctionDef filter_documents(self, documents)
**filter_documents**: The function of filter_documents is to filter a collection of documents based on whether their meta_data "id" field is not present in a set of database meta_data.

**parameters**:
- documents: Iterable[Document] - A collection of documents to filter.

**Code Description**:
The filter_documents function iterates over the input documents and filters out those documents whose meta_data "id" field is not found in the database_meta_data set. It retrieves the database meta_data from the database, compares the "id" field of each document with the database meta_data, and yields only the documents that do not exist in the database.

In the context of the project, this function is called by the insert method of the EmbeddingHolder class. Before inserting documents into the database, the insert method first filters the input documents using the filter_documents function to ensure that only new documents are processed and inserted into the database.

**Note**:
- Ensure that the Document class has a meta_data attribute with an "id" field for proper functioning of the filter_documents function.

**Output Example**:
```
<generator object filter_documents at 0x7f9d4d9c2a50>
```
***
### FunctionDef get_table(self)
**get_table**: The function of get_table is to create and return a Table object with specified columns and properties.

**parameters**: This function does not take any parameters.

**Code Description**: The get_table function creates a Table object with the following columns:
- "id" of type Integer, primary key, and auto-incremented
- "name" of type String
- "meta_data" of type JSONB with a default value of an empty JSON object
- "content" of type TEXT
- "embedding" of type Vector with dimensions specified elsewhere in the code
- "usage" of type JSONB
- "created_at" of type DateTime with timezone, defaulting to the current timestamp
- "updated_at" of type DateTime with timezone, updating to the current timestamp
- "content_hash" of type String

The Table object is extended with existing properties.

**Note**: Ensure that the necessary imports for Table, Column, Integer, String, postgresql, text, Vector, DateTime are included in the code before calling this function.

**Output Example**:
A Table object with the specified columns and properties is returned upon calling the get_table function.
***
