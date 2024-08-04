## ClassDef UniquenessCalculator
**UniquenessCalculator**: The function of UniquenessCalculator is to provide a base class for calculating uniqueness scores based on different metrics.

**attributes**:
- type: An attribute that represents the type of the uniqueness calculator. It is of type UniquenessCalculatorName.
- pairwise_similarity: An attribute that stores the pairwise similarity matrix calculated during the uniqueness calculation.
- uniqueness_metric_name_scope: An attribute that represents the scope of the uniqueness metric names. It is of type Enum.
- uniqueness_metric_scope: An attribute that represents the scope of the uniqueness metrics. It is of type UniquenessMetric.

**Code Description**:
The UniquenessCalculator class is an abstract base class that provides the structure for uniqueness calculators. It contains several attributes and methods to support uniqueness calculations. The class includes the following methods:

- __init__(self, similarity_calculator: Optional[SimilarityCalculator] = None): A constructor method that initializes the UniquenessCalculator object. It takes an optional similarity_calculator parameter, which is used to calculate the similarity between embeddings. If no similarity_calculator is provided, it defaults to CosineSimilarityCalculator.

- create(cls, type: str, **kwargs) -> Self: A class method that creates an instance of a specific uniqueness calculator based on the given type. It iterates through the subclasses of UniquenessCalculator and returns the first calculator with a matching type. If no matching calculator is found, it raises a ValueError.

- _get_uniqueness_score(self, X: np.ndarray, config: "Config") -> np.ndarray: An abstract method that must be implemented by subclasses to calculate the uniqueness score for a given set of embeddings and configuration. It takes an X parameter, which is the input embeddings, and a config parameter, which represents the configuration for uniqueness calculation. It returns an array of uniqueness scores.

- rank_uniqueness(self, X: np.ndarray, metric: uniqueness_metric_scope | uniqueness_metric_name_scope, config: "Config", **kwargs) -> np.ndarray: A method that ranks the uniqueness of a set of embeddings based on a specified metric. It calculates the uniqueness score using the _get_uniqueness_score method and applies the metric to the uniqueness score. If the metric is of type uniqueness_metric_scope, it directly applies the metric. Otherwise, it uses the uniqueness_metric_scope's pick_and_apply method to find a valid metric type and apply it. It returns an array of ranked uniqueness scores.

**Note**:
Developers can create custom uniqueness calculators by subclassing UniquenessCalculator and implementing the _get_uniqueness_score method.

**Output Example**:
```python
array([0.8, 0.6, 0.9, 0.7])
```
### FunctionDef __init__(self, similarity_calculator)
**__init__**: The function of __init__ is to initialize an instance of the UniquenessCalculator class with an optional SimilarityCalculator object, defaulting to CosineSimilarityCalculator if none is provided.
**parameters**:
- self: The instance of the UniquenessCalculator class.
- similarity_calculator: An optional SimilarityCalculator object used for similarity calculations. Defaults to None.

**Code Description**: 
The __init__ method of the UniquenessCalculator class initializes an instance of the class. It takes an optional similarity_calculator parameter, which defaults to None. If no similarity_calculator is provided, it assigns a new instance of CosineSimilarityCalculator to the self.similarity_calculator attribute. This ensures that the UniquenessCalculator class can utilize a specific similarity calculator for its uniqueness calculations.

In the project structure, the UniquenessCalculator class in the uniqueness_calculators module is designed to calculate uniqueness based on the similarity of embeddings. By accepting a SimilarityCalculator object in its constructor, it allows flexibility in choosing the method for similarity calculations. The default behavior of using the CosineSimilarityCalculator ensures that cosine similarity is used for uniqueness calculations if no other similarity calculator is specified.

**Note**: When creating an instance of the UniquenessCalculator class, you can pass a custom SimilarityCalculator object to tailor the similarity calculation method to your specific requirements. If no similarity calculator is provided, the default CosineSimilarityCalculator will be used for the uniqueness calculations.
***
### FunctionDef create(cls, type)
**create**: The function of create is to instantiate a subclass of UniquenessCalculator based on the provided type and keyword arguments.

**parameters**:
- cls: The class object.
- type: A string representing the type of uniqueness calculator to create.
- **kwargs: Additional keyword arguments to pass to the instantiated uniqueness calculator.

**Code Description**:
The create function iterates over the subclasses of the UniquenessCalculator class to find a match for the provided type. If a matching subclass is found, it instantiates the subclass with the provided keyword arguments. If no match is found, it raises a ValueError indicating that the provided type is not valid. The error message includes the valid types that can be created using the subclasses of UniquenessCalculator.

In the project, the create function is called multiple times with different types of uniqueness calculators based on the configuration provided. It plays a crucial role in dynamically creating instances of uniqueness calculators based on the configuration settings, allowing for flexibility and customization in the uniqueness calculation process.

**Note**: Ensure that the type provided matches one of the valid types defined by the subclasses of UniquenessCalculator to avoid ValueError.

**Output Example**:
An instance of the specified uniqueness calculator class with the provided keyword arguments.
***
### FunctionDef _get_uniqueness_score(self, X, config)
**_get_uniqueness_score**: The function of _get_uniqueness_score is to calculate the uniqueness score based on the input data and configuration.

**parameters**:
- X: np.ndarray - Input data for which uniqueness score needs to be calculated.
- config: "Config" - Configuration settings required for the uniqueness score calculation.

**Code Description**:
The _get_uniqueness_score function is responsible for computing the uniqueness score for a given input data array and configuration. It raises a NotImplementedError, indicating that the method needs to be implemented in a subclass that inherits from the UniquenessCalculator class.

In the project structure, this function is called by the rank_uniqueness method within the UniquenessCalculator class. The rank_uniqueness method utilizes the uniqueness score calculated by _get_uniqueness_score to apply a specified uniqueness metric and return the result.

**Note**:
Developers need to implement the _get_uniqueness_score method in a subclass to provide the actual logic for calculating the uniqueness score based on the input data and configuration.
***
### FunctionDef rank_uniqueness(self, X, metric, config)
**rank_uniqueness**: The function of rank_uniqueness is to calculate the uniqueness score for a given input data array and configuration, apply a specified uniqueness metric, and return the result based on the provided metric type.

**parameters**:
- X: np.ndarray - Input data for which the uniqueness score needs to be calculated.
- metric: uniqueness_metric_scope | uniqueness_metric_name_scope - The type of uniqueness metric to be applied.
- config: "Config" - Configuration settings required for the uniqueness score calculation.
- **kwargs: Additional keyword arguments that may be passed to the metric.

**Code Description**:
The rank_uniqueness function first calculates the uniqueness score by calling the _get_uniqueness_score method with the input data and configuration. It then checks the type of metric provided: if it is an instance of uniqueness_metric_scope, the apply function of that metric is directly called with the uniqueness score. Otherwise, the pick_and_apply method of uniqueness_metric_scope is used to select and apply the appropriate metric on the uniqueness score, considering any additional keyword arguments provided.

In the project structure, rank_uniqueness is a crucial method within the UniquenessCalculator class, responsible for computing and applying uniqueness metrics to the input data. By utilizing the provided metric type, the function ensures the correct processing of the uniqueness score to generate meaningful results.

**Note**:
- Developers should ensure that the uniqueness_metric_scope class and its subclasses are properly implemented to support the desired uniqueness metrics.
- The rank_uniqueness function serves as a bridge between uniqueness score calculation and metric application, facilitating the evaluation of data uniqueness based on the specified metric type.

**Output Example**:
```python
array([0.8, 0.6, 0.9, 0.7])
```
***
