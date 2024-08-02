## ClassDef CustomArgumentParser
**CustomArgumentParser**: The function of CustomArgumentParser is to extend the functionality of the argparse.ArgumentParser class by customizing the behavior of adding arguments, specifically handling boolean types.

**attributes**:
- add_argument: A method that customizes the behavior of adding arguments by converting boolean types using the _str2bool method.
- _str2bool: A private method that converts string representations of boolean values to actual boolean values.

**Code Description**:
The CustomArgumentParser class extends the argparse.ArgumentParser class. The add_argument method overrides the parent class method to check if the argument type is boolean. If the type is boolean, it converts the string representation of boolean values to actual boolean values using the _str2bool method before adding the argument. The _str2bool method checks if the input string corresponds to a boolean value and returns the corresponding boolean value.

In the project, the CustomArgumentParser class is utilized in the parse_arguments function in the Config.py file. The parse_arguments function creates an instance of CustomArgumentParser and adds arguments based on the configuration class provided. It customizes the argument handling by using the CustomArgumentParser class to parse and handle arguments effectively.

**Note**: Developers using the CustomArgumentParser class should be aware of the custom behavior implemented for boolean arguments and utilize the _str2bool method for converting string representations of boolean values.

**Output Example**:
A possible output of using the CustomArgumentParser class with boolean arguments:
--enable_feature True
### FunctionDef add_argument(self)
**add_argument**: The function of add_argument is to handle the addition of arguments to the argument parser. It checks if the type of the argument is bool and converts it using the _str2bool function before adding the argument.

**parameters**:
- self: The instance of the CustomArgumentParser class.
- *args: Variable length argument list.
- **kwargs: Variable length keyword argument list.

**Code Description**: 
The add_argument function first checks if the type of the argument is bool. If it is, the function sets the type to _str2bool, a function that converts a string representation of a boolean value to a boolean type. After this check, the function calls the superclass's add_argument method to add the argument to the argument parser.

This function ensures that boolean arguments are correctly handled by converting string representations to boolean values using the _str2bool function. It enhances the functionality of the argument parser by providing a seamless way to work with boolean arguments.

**Note**: Developers using this function should be aware of the automatic conversion of boolean arguments and ensure that the input values are string representations of boolean values to avoid any unexpected behavior.
***
### FunctionDef _str2bool(self, v)
**_str2bool**: The function of _str2bool is to convert a string representation of a boolean value to a boolean type.

**parameters**:
- self: The instance of the class.
- v: The string value to be converted to a boolean.

**Code Description**: 
The _str2bool function first checks if the input value is already a boolean. If not, it converts the string representation of a boolean value to a boolean type. It accepts strings like "yes", "true", "t", "y", "1" as True and strings like "no", "false", "f", "n", "0" as False. If the input value does not match any of these, it raises an argparse.ArgumentTypeError.

This function is called by the add_argument method in the CustomArgumentParser class. In the add_argument method, if the type of the argument is bool, it sets the type to _str2bool before adding the argument using the superclass's add_argument method.

**Note**: 
Developers using this function should ensure that the input value is a string representing a boolean value to avoid raising an ArgumentTypeError.

**Output Example**: 
If the input value is "true", the function will return True.
***
