## ClassDef DistanceUniquenessCalculator
Doc is waiting to be generated...
### FunctionDef _get_uniqueness_score(self, X, config)
**_get_uniqueness_score**: The function of _get_uniqueness_score is to calculate the pairwise similarity based on the embeddings and configuration provided as input parameters.

**parameters**:
- X: An np.ndarray containing the embeddings for which the similarity needs to be calculated.
- config: A "Config" object specifying the configuration parameters for the similarity calculation.

**Code Description**:
The `_get_uniqueness_score` function calculates the pairwise similarity by utilizing the `calculate_similarity` function from the `SimilarityCalculator` class. It first computes the similarity between the embeddings using the provided configuration and then returns the pairwise similarity scores.

This function is a crucial part of the `DistanceUniquenessCalculator` class in the project's uniqueness calculators module. By invoking the `calculate_similarity` method, it plays a key role in determining the uniqueness score based on the pairwise similarities of the embeddings.

**Note**:
Developers should ensure that the `calculate_similarity` method in the `SimilarityCalculator` class is properly implemented to provide accurate similarity calculations for the `_get_uniqueness_score` function to work effectively.

**Output Example**:
array([[0.8, 0.6, 0.9],
       [0.6, 1.0, 0.7],
       [0.9, 0.7, 1.0]])
***
