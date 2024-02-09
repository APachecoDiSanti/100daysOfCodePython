# Notes
1. `try`, `except`, `else` and `finally` are used to handle exceptions.
2. `try` used to enclose code that might cause an exception.
3. `except` execute this block of code when a specific exception does occur.
4. `else` execute this block of code if there were no exceptions.
5. `finally` always execute this block of code if there were exceptions or not.
6. Instead of `except:` we should use one or multiple `except exception_class:` to provide specific actions for each exception that we want to handle.
7. To get data from the exception object that was caught, we can use `except exception_class as variable_name` and use `variable_name` to get the data.
8. `raise exception_class` is used to throw an exception and cause an error.
9. The `json` package has functions to `dump` (write), `update` and `load` (read) JSON data.
10. `json.load()` loads the JSON file as a Python dictionary.
11. `json.dump()` saves a Python dictionary in JSON format.
12. Use `json.load()` with a file in read mode to load it. Update the dictionary with the new data using `json.update()`. Finally, open the file in write mode and use `json.dump()` to save it.
13. Exception handling should be used when there's no easy alternative such as an if-then-else.
