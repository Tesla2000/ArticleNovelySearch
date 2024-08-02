## FunctionDef import_python(root)
**import_python**: The function of import_python is to recursively import Python modules from a specified root directory.

**parameters**:
- root: The root directory path from which to start importing Python modules.

**Code Description**:
The `import_python` function takes a `root` directory path as input and iterates through the contents of the directory. It skips certain files and directories such as "__init__.py", "pycache", and "__pycache__". If a file is encountered, it calculates the relative path to the file, imports the module using `import_module`, and yields the name of the module. If a directory is encountered, it recursively calls itself on that directory.

**Note**:
- This function is designed to import Python modules from a specified directory and its subdirectories.
- Make sure to provide a valid root directory path to ensure the function works correctly.
- The function uses `import_module` to dynamically import modules, so ensure that the necessary modules are accessible in the Python environment.
