## ClassDef DistanceMetric
**DistanceMetric**: The function of DistanceMetric is to calculate uniqueness scores based on distance metrics.

**attributes**:
- power: A float representing the power to which the cosine distance matrix is raised during the uniqueness score calculation.

**Code Description**:
The DistanceMetric class is a subclass of DistanceUniquenessMetric and is responsible for computing uniqueness scores using distance metrics. The class contains an attribute 'power' that determines the exponent to which the cosine distance matrix is raised. In the apply method, the uniqueness score is calculated by raising the cosine distance matrix to the power specified and then sorting the scores to return the indices.

The DistanceMetric class is utilized within the uniqueness calculation process to provide a specific implementation for distance-based uniqueness metrics. By inheriting from DistanceUniquenessMetric, it ensures adherence to the predefined structure for handling distance uniqueness metrics. Developers can instantiate DistanceMetric objects with a custom power value to tailor the uniqueness score calculation to their specific requirements.

**Note**:
Developers should ensure that the power attribute is set appropriately to achieve the desired impact on the uniqueness score calculation. The apply method should be implemented in a way that aligns with the intended distance metric calculation logic.

**Output Example**:
[2, 0, 1, 3]
### FunctionDef __init__(self, power)
**__init__**: The function of __init__ is to initialize the DistanceMetric object with a specified power value.

**parameters**:
- power: A float value representing the power to be assigned to the DistanceMetric object. The default value is 1.

**Code Description**:
The __init__ function is a constructor method for the DistanceMetric class. It takes an optional parameter 'power' which defaults to 1 if not provided. Inside the function, the 'power' parameter is assigned to the 'power' attribute of the DistanceMetric object.

**Note**:
- When creating an instance of the DistanceMetric class, you can pass a custom power value as an argument to set the power attribute accordingly. If no value is provided, the power will default to 1.
***
### FunctionDef apply(self, cosine_distance_matrix)
**apply**: The function of apply is to calculate the uniqueness score based on the cosine distance matrix provided as input.

**parameters**:
- cosine_distance_matrix: A numpy array representing the cosine distance matrix.
  
**Code Description**:
The apply function takes a cosine distance matrix as input and calculates the uniqueness score by raising each element of the matrix to the power specified by the 'power' attribute of the DistanceMetric object. It then sums up the values along the columns of the matrix to obtain the uniqueness score. Finally, the function returns the indices that would sort the uniqueness scores in ascending order.

**Note**:
- Make sure the cosine_distance_matrix is a valid numpy array.
- Ensure that the 'power' attribute of the DistanceMetric object is set appropriately before calling the apply function.

**Output Example**:
[2, 0, 1, 3]
***
