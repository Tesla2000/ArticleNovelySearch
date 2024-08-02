## ClassDef DistanceMetric
Doc is waiting to be generated...
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
