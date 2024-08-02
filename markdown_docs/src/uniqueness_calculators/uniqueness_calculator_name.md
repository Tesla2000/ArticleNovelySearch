## ClassDef UniquenessCalculatorName
The function of UniquenessCalculatorName is to define two enumeration constants: CLUSTERING and DISTANCE.

**attributes**:
- CLUSTERING: Represents the value "clustering".
- DISTANCE: Represents the value "distance".

**Code Description**:
The UniquenessCalculatorName class is a subclass of the Enum class, defining two enumeration constants: CLUSTERING with the value "clustering" and DISTANCE with the value "distance". This class provides a way to represent these specific values within the UniquenessCalculatorName enumeration.

In the project, the Config class utilizes the UniquenessCalculatorName class to set the uniqueness_calculator_type for uniqueness calculation. The Config class assigns the value of UniquenessCalculatorName.CLUSTERING.value to uniqueness_calculator_type for clustering uniqueness calculation and UniquenessCalculatorName.DISTANCE.value for distance uniqueness calculation.

**Note**:
Developers can use the UniquenessCalculatorName enumeration to specify the type of uniqueness calculator to be used in the project, either for clustering or distance uniqueness calculation.
