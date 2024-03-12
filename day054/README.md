# Notes
1. There are some Python Special Attributes such as `__name__` (the name of the class, function, method, descriptor or generator instance).
2. `__name__` will be `__main__` if the Python code is being run as a script and not because it's code was imported as a module.
3. Python functions are first-class objects and can be passed as arguments into a function or returned as results (use only function name in this case so it's not called).
4. Python functions can be defined within other function definitions. These are nested functions and are only callable from inside the function where they were defined.
5. Python decorators are functions that add functionality to another function they receive by parameter. This can be by running code before/after the parameter function is called or calling it multiple times.
6. After a python decorator is defined (basically a function that receives a function as parameter and returns a nested function that calls the parameterized one), we can use the `@decorator` syntax to apply it to other function definitions:
7. ```py
    def delay(function):
      def wrapper():
        time.sleep(2)
        function()
      return wrapper
   
    @delay
    def hello_world():
      print("Hello world!")
```