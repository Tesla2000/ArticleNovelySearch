## ClassDef DistanceUniquenessMetricName
**DistanceUniquenessMetricName**: The function of DistanceUniquenessMetricName is to define an enumeration class with a single member "DISTANCE".

**attributes**:
- DISTANCE: Represents the only member of the DistanceUniquenessMetricName enumeration class with a string value of "distance".

**Code Description**:
The DistanceUniquenessMetricName class is a subclass of the Python Enum class. It defines a single enumeration member "DISTANCE" with the value "distance". This class is used to provide a specific name for a distance uniqueness metric within the uniqueness calculation process.

In the project, the DistanceUniquenessMetricName class is utilized in the Config class to set the commonness metric name for the uniqueness calculation. Specifically, in the Config class, the commonness_metric_name attribute is set to DistanceUniquenessMetricName.DISTANCE.value, which corresponds to the "DISTANCE" member of the DistanceUniquenessMetricName enumeration.

**Note**:
Developers can use the DistanceUniquenessMetricName enumeration class to ensure consistency and avoid hardcoding distance uniqueness metric names in the codebase.
