# Notes
1. List comprehension: unique to Python and used to create a new list from an existing list.
2. `new_list = [new_item for item in list]` where `new_item` is an expression on how each `item` from `list` will be computed to generate `new_list`.
3. Conditional List Comprehension adds a test to each item from the original list: `new_list = [new_item for item in list if test]` apply `new_item` to each `item` in `list` if `item` passes `test` to build `new_list`.
4. Dictionary comprehension: generate a dictionary from another dictionary or a list.
5. `new_dict = {new_key: new_value for item in list}` create a dictionary from items in a list.
6. `new_dict = {new_key: new_value for (key, value) in dict.items()}` create a dictionary from key,values from another dictionary.
7. 6. `new_dict = {new_key: new_value for (key, value) in dict.items() if test}` also add a condition to the items.