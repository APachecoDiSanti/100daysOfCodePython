# Notes
1. A Python class inherits from another by providing the other class' name after parenthesis (e.g.: `class Fish(Animal)`)
2. In the `__init__(self)` method you may call the super-class' constructor by calling `super().__init__()`
3. You may also call function implementations from the super-class by calling it with `super().function_name()`
4. List slicing can be done with this syntax: `list[start:stop]` and will provide you items from index `start` (inclusive) up to `stop` (not inclusive).
5. `list[start:]` gives you all items from `start` (inclusive) up to the last element of the list.
6. `list[:stop]` gives you all items from index `0` up to `stop` (not inclusive).
7. `list[start:stop:step]` gives you all items from `start` (inclusive) up to `stop` (not inclusive) by going over increments of `step` (so the items at index `start+step`, `start+(step*2)` and so on).
8. `list[::step]` will give all items of the list from start to finish but only those at step increments indexes.
9. `list[::-1]` gives you a reverted list.
10. This slicing syntax can be used for both lists and tuples.
