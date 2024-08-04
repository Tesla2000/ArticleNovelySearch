## FunctionDef main
**main**: The main function is the entry point of the application. It orchestrates the execution of various tasks based on the provided configuration settings.

**parameters**:
- No parameters.

**Code Description**:
The main function starts by parsing the command-line arguments using the parse_arguments function. It creates an argument parser using the CustomArgumentParser class and adds arguments based on the provided configuration class (Config). The parsed arguments are then returned.

Next, the function creates a configuration object by calling the create_config_with_args function with the Config class and the parsed arguments as parameters. The create_config_with_args function instantiates a Config object and initializes its attributes based on the provided arguments. It also checks and creates directories if the specified paths in the Config instance are of type Path and do not exist.

After creating the configuration object, the function checks if the "topic" attribute is provided in the configuration. If not, it raises a ValueError with the message "Topic must be provided".

The function then creates an instance of the EmbeddingHolder class, which is responsible for managing embeddings in a vector database. It initializes the EmbeddingHolder object with the collection name based on the lowercase and underscored version of the "topic" attribute from the configuration, and the database URL from the configuration.

Next, the function calls the _get_embeddings function to retrieve embeddings from the vector database. It passes the configuration object and the EmbeddingHolder object as parameters. The _get_embeddings function is responsible for retrieving embeddings from the vector database based on the provided configuration and embedding holder. It first calls the create method of the vector database to ensure that the necessary database table is created. Then, it checks if the number of articles in the vector database is less than the configured number of checked articles. If so, it populates the vector database by inserting documents obtained from the arXiv search based on the specified topic in the configuration. The search is performed using the search_arxiv function from the arxiv_searcher module. The title_from_arxiv function from the pdf_reader module is used to create Document objects from the search results. The insert method of the vector database is called to insert the documents in batches. Finally, the get_embeddings method of the vector database is called to retrieve the embeddings based on the specified limit from the configuration. The _get_embeddings function returns a tuple containing the retrieved embeddings as a NumPy array and the associated metadata as a list of dictionaries.

The function assigns the retrieved embeddings and metadata to the variables "embeddings" and "metadata" respectively. It then retrieves the title of the least relevant article from the metadata list and assigns it to the variable "least_relevant_title".

The function checks if the "calc_commonness" attribute in the configuration is set to True. If so, it creates an instance of the UniquenessCalculator class based on the "commonness_calculator_type" attribute from the configuration. It then calls the _get_most_common function to calculate the most common articles based on the uniqueness scores of their embeddings. It passes the configuration object, embeddings, metadata, and the created uniqueness calculator as parameters. The _get_most_common function calculates the uniqueness rank of the embeddings using the uniqueness_calculator's rank_uniqueness method. It retrieves the most common articles by selecting a subset of articles from the metadata list based on the number of displayed articles specified in the config object. The selection is performed by mapping the metadata.__getitem__ method to the reversed uniqueness rank, and then using the islice function to limit the number of articles to the config.displayed_n_articles value. The function returns a list of dictionaries representing the most common articles.

The function checks if the "calc_uniqueness" attribute in the configuration is set to True. If so, it creates another instance of the UniquenessCalculator class based on the "uniqueness_calculator_type" attribute from the configuration. It then calls the _get_most_unique function to calculate the uniqueness score for a given set of embeddings and metadata using the created uniqueness calculator. It passes the configuration object, embeddings, metadata, and the uniqueness calculator as parameters. The _get_most_unique function calculates the uniqueness score by calling the uniqueness_calculator's rank_uniqueness method. It retrieves the most unique articles by selecting a subset of articles from the metadata list based on the number of displayed articles specified in the config object. The selection is performed by mapping the metadata.__getitem__ method to the uniqueness rank, and then using the slicing operator to limit the number of articles to the config.displayed_n_articles value. The function returns a list of dictionaries representing the most unique articles.

The function checks if the "compared_article_title" attribute in the configuration is provided. If so, it creates another instance of the UniquenessCalculator class based on the "uniqueness_calculator_type" attribute from the configuration. It then calls the _print_uniqueness function to calculate the uniqueness rank of the compared article title and print the most similar articles based on the uniqueness metric. It passes the configuration object, embeddings, the Embedding
## FunctionDef _get_embeddings(config, vector_db)
**_get_embeddings**: The function of _get_embeddings is to retrieve embeddings from a vector database based on the provided configuration and embedding holder.

**parameters**:
- config: A Config object representing the configuration settings for the application.
- vector_db: An EmbeddingHolder object representing the vector database.

**Code Description**:
The _get_embeddings function is responsible for retrieving embeddings from a vector database. It first calls the create method of the vector database to ensure that the necessary database table is created. Then, it checks if the number of articles in the vector database is less than the configured number of checked articles. If so, it populates the vector database by inserting documents obtained from the arXiv search based on the specified topic in the configuration. The search is performed using the search_arxiv function from the arxiv_searcher module. The title_from_arxiv function from the pdf_reader module is used to create Document objects from the search results. The insert method of the vector database is called to insert the documents in batches. Finally, the get_embeddings method of the vector database is called to retrieve the embeddings based on the specified limit from the configuration.

The _get_embeddings function returns a tuple containing the retrieved embeddings as a NumPy array and the associated metadata as a list of dictionaries.

The _get_embeddings function is called within the main function of the main.py module. It is used to retrieve embeddings from the vector database based on the specified configuration. The retrieved embeddings are then used for further processing, such as calculating uniqueness and commonness metrics.

**Note**:
Developers should ensure that the vector database is properly configured and that the necessary dependencies, such as the arxiv library, are installed for successful execution of the _get_embeddings function.

**Output Example**:
```python
(np.ndarray(embeddings), list[dict[str, str]](metadata))
```
## FunctionDef _get_most_common(config, embeddings, metadata, uniqueness_calculator)
**_get_most_common**: The function of _get_most_common is to calculate the most common articles based on the uniqueness scores of their embeddings.

**parameters**:
- config: Config - An object of the Config class that represents the configuration settings for the application.
- embeddings: np.ndarray - An array of embeddings representing the articles.
- metadata: list[dict[str, str]] - A list of dictionaries containing metadata information for each article.
- uniqueness_calculator: UniquenessCalculator - An object of the UniquenessCalculator class used to calculate uniqueness scores.

**Code Description**:
The _get_most_common function takes the configuration object (config), embeddings array, metadata list, and uniqueness calculator object as input parameters. It calculates the uniqueness rank of the embeddings using the uniqueness_calculator's rank_uniqueness method. The rank_uniqueness method applies the specified uniqueness metric to the uniqueness scores calculated by the uniqueness_calculator's _get_uniqueness_score method.

The function then retrieves the most common articles by selecting a subset of articles from the metadata list based on the number of displayed articles specified in the config object. The selection is performed by mapping the metadata.__getitem__ method to the reversed uniqueness rank, and then using the islice function to limit the number of articles to the config.displayed_n_articles value.

Finally, the function returns a list of dictionaries representing the most common articles.

The _get_most_common function is called in the main function of the main.py file. It is called when the config.calc_commonness attribute is set to True, indicating that commonness calculation should be performed. The function is passed the config object, embeddings, metadata, and an instance of the UniquenessCalculator class created based on the config.commonness_calculator_type attribute.

**Note**:
Developers can use the _get_most_common function to calculate and retrieve the most common articles based on their uniqueness scores. The function provides a convenient way to analyze and display the articles that are most frequently occurring or have the highest commonness metric values.

**Output Example**:
```python
[
    {"title": "Article 1", "author": "Author 1"},
    {"title": "Article 2", "author": "Author 2"},
    {"title": "Article 3", "author": "Author 3"}
]
```
## FunctionDef _get_most_unique(config, embeddings, metadata, uniqueness_calculator)
**_get_most_unique**: The function of _get_most_unique is to calculate the uniqueness score for a given set of embeddings and metadata using a specified uniqueness calculator, and return a list of the most unique articles based on the uniqueness score.

**parameters**:
- config: Config - An object representing the configuration settings for the application.
- embeddings: np.ndarray - An array of embeddings representing the articles.
- metadata: list[dict[str, str]] - A list of dictionaries representing the metadata of the articles.
- uniqueness_calculator: UniquenessCalculator - An object representing the uniqueness calculator to be used for calculating the uniqueness score.

**Code Description**:
The _get_most_unique function takes the configuration object, embeddings, metadata, and uniqueness calculator as input parameters. It first calls the rank_uniqueness method of the uniqueness_calculator object to calculate the uniqueness score for the embeddings. The rank_uniqueness method applies a specified uniqueness metric to the uniqueness score. The uniqueness score is then used to rank the articles based on their uniqueness.

The function returns a list of dictionaries representing the metadata of the most unique articles. The number of articles to be displayed is determined by the displayed_n_articles attribute of the config object.

The _get_most_unique function is called in the main function of the main.py file. It is called when the calc_uniqueness attribute of the config object is set to True. The function is responsible for calculating and displaying the most unique articles based on the specified uniqueness calculator and configuration settings.

**Note**:
Developers can customize the uniqueness calculation by providing different uniqueness calculators and configuring the uniqueness metric and other parameters in the config object.

**Output Example**:
```python
[
    {"title": "Article 1", "author": "Author 1"},
    {"title": "Article 2", "author": "Author 2"},
    {"title": "Article 3", "author": "Author 3"}
]
```
## FunctionDef _print_uniqueness(config, embeddings, vector_db, uniqueness_calculator, metadata)
**_print_uniqueness**: The function of _print_uniqueness is to calculate the uniqueness rank of a given article title and print the most similar articles based on the uniqueness metric.

**parameters**:
- config: A Config object that represents the configuration settings for the application.
- embeddings: A numpy array that contains the embeddings of the articles.
- vector_db: An EmbeddingHolder object that manages embeddings in a database.
- uniqueness_calculator: A UniquenessCalculator object that calculates uniqueness scores based on different metrics.
- metadata: A list of dictionaries that contains metadata information for each article.

**Code Description**:
The _print_uniqueness function takes in the necessary parameters to calculate the uniqueness rank of a given article title and print the most similar articles based on the uniqueness metric. 

First, the function appends the embedding of the compared article title to the existing embeddings array. This is done by calling the `get_embedding` method of the `vector_db.embedder` object with the `config.compared_article_title` as the input. The resulting embedding is then appended to the `embeddings` array using the `np.append` function.

Next, the function calculates the uniqueness rank by calling the `rank_uniqueness` method of the `uniqueness_calculator` object. The method takes in the `embeddings`, `config.uniqueness_metric_name`, `config`, and `config.uniqueness_kwargs` as parameters. The uniqueness rank is stored in the `uniqueness_rank` variable.

The function then retrieves the indices of the highest similarities from the `uniqueness_calculator.pairwise_similarity` array. This is done by calling the `np.argsort` function on the last row of the `pairwise_similarity` array and selecting the last `config.n_most_similar` indices. The resulting indices are stored in the `highest_similarities` variable.

The function creates a list of similar articles by mapping the `metadata.__getitem__` function to the `highest_similarities` array. The `metadata` list contains dictionaries, and each dictionary represents the metadata information for an article. The `__getitem__` function is used to retrieve the article information based on the indices in the `highest_similarities` array. The resulting list is stored in the `similar` variable.

Finally, the function prints the uniqueness rank of the compared article title, along with the most similar articles. The output is formatted using f-strings and the `json.dumps` function to display the information in a readable format.

The _print_uniqueness function is called within the main function of the main.py file. It is called after retrieving the most common articles and most unique articles based on the specified configuration settings. The function utilizes the EmbeddingHolder object to manage embeddings and the UniquenessCalculator object to calculate uniqueness scores.

**Note**:
Developers can use the _print_uniqueness function as a reference for calculating and printing uniqueness rankings based on a specified article title. The function provides an example of how to use the EmbeddingHolder and UniquenessCalculator objects to perform uniqueness calculations and retrieve similar articles.
