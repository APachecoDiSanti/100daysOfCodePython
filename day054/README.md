# Notes
1. There are some Python Special Attributes such as `__name__` (the name of the class, function, method, descriptor or generator instance).
2. `__name__` will be `__main__` if the Python code is being run as a script and not because it's code was imported as a module.
3. Python functions are first-class objects and can be passed as arguments into a function or returned as results (use only function name in this case so it's not called).
4. Python functions can be defined within other function definitions. These are nested functions and are only callable from inside the function where they were defined.
5. Python decorators