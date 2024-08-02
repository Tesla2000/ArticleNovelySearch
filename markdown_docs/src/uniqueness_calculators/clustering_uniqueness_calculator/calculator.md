## ClassDef ClusteringUniquenessCalculator
Doc is waiting to be generated...
### FunctionDef _cluster(self, X, config)
**_cluster**: The function of _cluster is to perform clustering on the input data based on pairwise similarities calculated using the provided similarity calculator and configuration.

**parameters**:
- X: An np.ndarray containing the input data for clustering.
- config: A "Config" object specifying the configuration parameters for clustering.

**Code Description**: 
The `_cluster` function initializes the `pairwise_similarity` attribute by calculating pairwise similarities using the `calculate_similarity` function from the `SimilarityCalculator` class. It then performs agglomerative clustering on the similarity matrix with varying numbers of clusters ranging from 2 to the number of samples in the input data. The clustering is done using the complete linkage method and the precomputed metric. The function returns an np.ndarray containing the cluster labels for each data point.

This function is a crucial part of the `ClusteringUniquenessCalculator` class in the `clustering_uniqueness_calculator/calculator.py` module. It leverages the `calculate_similarity` function to obtain pairwise similarities necessary for clustering uniqueness calculation.

**Note**: Ensure that the `SimilarityCalculator` class is properly implemented with the `calculate_similarity` method overridden to provide custom similarity calculation logic.

**Output Example**: 
```python
array([[0, 1, 0, ..., 2],
       [1, 0, 1, ..., 3],
       [2, 3, 2, ..., 0],
       ...,
       [0, 1, 0, ..., 2]])
```
***
### FunctionDef _get_uniqueness_score(self, X, config)
Doc is waiting to be generated...
***
