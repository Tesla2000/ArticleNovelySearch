## ClassDef UniquenessMetric
**UniquenessMetric**: The function of UniquenessMetric is to define an abstract base class for uniqueness metrics.

**attributes**:
- type: Enum

**Code Description**:
The UniquenessMetric class is an abstract base class that defines the structure for uniqueness metrics. It contains a type attribute as an Enum. The class includes the following methods:
- apply(cls, uniqueness_score: np.ndarray) -> np.array: An abstract method that must be implemented by subclasses to apply the uniqueness metric.
- pick_and_apply(cls, type: str, clusters: np.ndarray, **kwargs) -> np.ndarray: A method that iterates through subclasses to find a valid type and apply the metric.
- is_valid(cls, type: str) -> bool: A method to check if a given type is valid for the uniqueness metric.

In the project hierarchy, the UniquenessMetric class serves as the base class for specific uniqueness metrics such as ClusteringUniquenessMetric and DistanceUniquenessMetric. These subclasses implement the apply method to calculate uniqueness scores based on different metrics.

**Note**:
Developers can create custom uniqueness metrics by subclassing UniquenessMetric and implementing the apply method.

**Output Example**:
```python
array([0.8, 0.6, 0.9, 0.7])
```
### FunctionDef apply(cls, uniqueness_score)
**apply**: The function of apply is to apply a uniqueness score, represented as a NumPy array, but it raises a NotImplementedError.

**parameters**:
- uniqueness_score: a NumPy array representing the uniqueness score.

**Code Description**: The apply function is designed to apply a uniqueness score, which is expected to be a NumPy array. However, in its current state, the function raises a NotImplementedError, indicating that the implementation of this function is incomplete or intended to be overridden by subclasses.

In the project, the apply function is called within the rank_uniqueness method of the UniquenessCalculator class. When a metric is provided, the apply function is invoked on that metric to process the uniqueness score obtained from the dataset. If the metric is an instance of the uniqueness_metric_scope class, the apply function is directly called on the metric. Otherwise, the pick_and_apply method of the uniqueness_metric_scope class is used to select and apply the appropriate metric on the uniqueness score.

**Note**: As the apply function raises a NotImplementedError, it needs to be implemented or overridden in a subclass to provide the desired functionality for processing uniqueness scores.
***
### FunctionDef pick_and_apply(cls, type, clusters)
**pick_and_apply**: The function of pick_and_apply is to select a valid metric type and apply it to the given clusters.

**parameters**:
- cls: The class object.
- type: A string representing the type of metric to be applied.
- clusters: A numpy array containing the clusters data.
- **kwargs: Additional keyword arguments.

**Code Description**:
The pick_and_apply function iterates through the subclasses of the provided class object (cls) to find a valid metric type. It then instantiates the class with the valid type and applies it to the clusters data. If no valid type is found among the subclasses, a ValueError is raised indicating the invalid type and listing the valid types available.

In the context of the project, the pick_and_apply function is called from the rank_uniqueness method in the UniquenessCalculator class. In this context, the function is used to select and apply a metric to the uniqueness scores based on the provided metric type.

**Note**:
- Ensure that the provided class object has valid subclasses with the necessary methods.
- The metric type must be a valid type supported by the subclasses of the provided class.

**Output Example**:
```python
array([0.8, 0.6, 0.9, 0.7])
```
***
### FunctionDef is_valid(cls, type)
**is_valid**: The function of is_valid is to check if the input type matches the type stored in the class.

**parameters**:
- type: A string representing the type to be checked against the type stored in the class.

**Code Description**:
The is_valid function compares the input type parameter with the type attribute of the class. If they match, the function returns True, indicating that the input type is valid. Otherwise, it returns False.

**Note**:
Make sure to provide a valid string type as the input parameter when calling this function.

**Output Example**:
- True
- False
***
