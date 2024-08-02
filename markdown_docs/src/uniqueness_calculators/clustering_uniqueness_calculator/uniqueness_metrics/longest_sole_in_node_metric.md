## ClassDef LongestSoleInNodeMetric
Doc is waiting to be generated...
### FunctionDef __init__(self, neighbours)
**__init__**: The function of __init__ is to initialize the LongestSoleInNodeMetric object with a specified number of neighbors.

**parameters**:
- neighbours: An integer representing the number of neighbors to consider. Default value is 1.

**Code Description**:
The __init__ function in the LongestSoleInNodeMetric class takes an optional parameter 'neighbours' which defaults to 1. It assigns the value of 'neighbours' to the object's 'neighbours' attribute, allowing the user to specify the number of neighbors to be considered when calculating the longest sole in a node metric.

**Note**:
- The 'neighbours' parameter allows customization of the calculation based on the specific requirements of the user.
- If no value is provided for 'neighbours', the default value of 1 will be used.
***
### FunctionDef apply(self, uniqueness_score)
**apply**: The function of apply is to calculate the uniqueness score based on the input array and return the indices that would sort the uniqueness scores in ascending order.

**parameters**:
- uniqueness_score: An input numpy array containing uniqueness scores.
  
**Code Description**:
The apply function takes the uniqueness_score array and calculates the sum of elements that are less than or equal to the number of neighbors specified by the 'neighbours' attribute of the object. It then returns the indices that would sort the uniqueness scores in ascending order.

**Note**:
- Make sure the uniqueness_score parameter is a numpy array.
- Ensure that the 'neighbours' attribute is properly set before calling the apply function.

**Output Example**:
[2, 0, 1, 3]
***
