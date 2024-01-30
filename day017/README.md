# Notes
1. To create an empty class or function, after the colon `:` use the keyword `pass`
2. After creating an empty object, we can add as many attributes as we like using dot notation assignation (e.g.: `user1.id = "001"`)
3. The `def __init__(self):` is used to define class constructors. 
4. `self` is the actual object being created and doesn't need to be specified in the constructor call (e.g.: `User()`)
5. After `self` in the `__init__` function we can add parameters to use in the function (to set the attributes).
6. The convention is for the constructor parameters to be called the same as the class attributes they will be assigned to.
7. To assign a value to an attribute in a constructor use `self.attribute_name = value` (e.g.: `self.id = id`)
8. Methods are function definitions inside a class. To call a method use the object dot notation (e.g.: `car.accelerate()`)
9. All methods need to have as their first parameter `self` that is the object that called the method.
10. Python dictionaries have a very similar structure to JSON objects.
