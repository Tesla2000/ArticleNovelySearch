## ClassDef Config
**Config**: The Config class is responsible for defining the configuration settings for the application.

**attributes**:
- _root: Represents the root path of the project.
- _caches: Represents the path to the caches directory.
- hierarchical_caches: Represents the path to the hierarchical caches directory.
- cosine_caches: Represents the path to the cosine caches directory.
- embeddings_caches: Represents the path to the embeddings caches directory.
- db_url: Represents the URL of the database.
- n_checked_articles: Represents the number of checked articles.
- displayed_n_articles: Represents the number of articles to be displayed.
- batch_size: Represents the batch size for processing articles.
- compared_article_title: Represents the title of the article to be compared.
- n_most_similar: Represents the number of most similar articles to be retrieved.
- topic: Represents the topic of the articles.

- calc_uniqueness: Represents whether to calculate uniqueness.
- uniqueness_calculator_type: Represents the type of uniqueness calculator to be used.
- uniqueness_metric_name: Represents the name of the uniqueness metric.
- uniqueness_kwargs: Represents additional keyword arguments for uniqueness calculation.

- calc_commonness: Represents whether to calculate commonness.
- commonness_calculator_type: Represents the type of commonness calculator to be used.
- commonness_metric_name: Represents the name of the commonness metric.
- commonness_kwargs: Represents additional keyword arguments for commonness calculation.

**Code Description**:
The Config class is a subclass of the BaseModel class. It defines various attributes that represent the configuration settings for the application. These attributes include paths to different directories, database URL, article-related settings, uniqueness calculation settings, and commonness calculation settings.

The _root attribute represents the root path of the project, while the _caches attribute represents the path to the caches directory. The hierarchical_caches, cosine_caches, and embeddings_caches attributes represent specific paths within the caches directory.

The db_url attribute represents the URL of the database, which can be obtained from the DATABASE_URL environment variable or a default value based on other configuration settings.

The n_checked_articles attribute represents the number of articles to be checked. The displayed_n_articles attribute represents the number of articles to be displayed. The batch_size attribute represents the batch size for processing articles. The compared_article_title attribute represents the title of the article to be compared. The n_most_similar attribute represents the number of most similar articles to be retrieved. The topic attribute represents the topic of the articles.

The calc_uniqueness attribute represents whether to calculate uniqueness. The uniqueness_calculator_type attribute represents the type of uniqueness calculator to be used, which can be specified using the UniquenessCalculatorName enumeration. The uniqueness_metric_name attribute represents the name of the uniqueness metric, which can be specified using the ClusteringUniquenessMetricName enumeration. The uniqueness_kwargs attribute represents additional keyword arguments for uniqueness calculation.

The calc_commonness attribute represents whether to calculate commonness. The commonness_calculator_type attribute represents the type of commonness calculator to be used, which can also be specified using the UniquenessCalculatorName enumeration. The commonness_metric_name attribute represents the name of the commonness metric, which can be specified using the DistanceUniquenessMetricName enumeration. The commonness_kwargs attribute represents additional keyword arguments for commonness calculation.

The Config class is used in the main function of the main.py file to create a configuration object based on the command-line arguments. The configuration object is then used to set up various components and perform uniqueness and commonness calculations based on the specified settings.

**Note**:
Developers can use the Config class to define and manage the configuration settings for the application. The class provides a convenient way to organize and access different configuration parameters.
## FunctionDef parse_arguments(config_class)
**parse_arguments**: The function of parse_arguments is to create an argument parser using CustomArgumentParser and add arguments based on the provided configuration class. It then parses the arguments and returns the parsed values.

**parameters**:
- config_class: Represents the configuration class (Config) used to define the arguments.

**Code Description**:
The parse_arguments function initializes a CustomArgumentParser instance with a description for configuring application settings. It iterates over the model_fields of the provided config_class, excluding names starting with '_', and adds arguments to the parser based on the field names, types, defaults, and help messages. Finally, it parses the arguments and returns the parsed values.

This function is utilized in the main function of main.py to parse command-line arguments and create a configuration object. The configuration object is then used to set up components and perform calculations based on the specified settings.

**Note**:
Developers can use parse_arguments to dynamically generate argument parsers based on the configuration class, simplifying the process of handling command-line arguments and configuring the application.

**Output Example**:
A possible output of using the parse_arguments function:
Namespace(_root='path/to/root', _caches='path/to/caches', hierarchical_caches='path/to/hierarchical', ...)
## FunctionDef create_config_with_args(config_class, args)
**create_config_with_args**: The function of create_config_with_args is to create an instance of the Config class based on the provided arguments.

**parameters**:
- config_class: Represents the type of the Config class.
- args: Represents the arguments used to initialize the Config instance.

**Code Description**:
The create_config_with_args function takes a config_class parameter, which is the type of the Config class, and args parameter, which contains the arguments for initializing the Config instance. It then creates a new instance of the Config class by extracting values from the args parameter based on the model_fields attribute defined in the config_class. Additionally, it checks and creates directories if the specified paths in the Config instance are of type Path and do not exist. Finally, it returns the created Config instance.

This function is utilized in the main function of the main.py file to instantiate a Config object with the provided command-line arguments. The Config object is subsequently used to configure various components and perform uniqueness and commonness calculations based on the specified settings.

**Note**:
Developers can use create_config_with_args to dynamically create a Config object with specific attributes based on the arguments provided, offering flexibility in configuring the application settings.

**Output Example**:
```python
config_instance = create_config_with_args(Config, args)
```
