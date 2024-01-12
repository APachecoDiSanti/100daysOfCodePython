# Notes

1. String indexing is done with brackets and an integer. e.g.: `"Hello"[1] => e`
2. Big numbers may use `_` to make them easier to read by humans. e.g.: `123_456_789` instead of 123.456.678 or 123,456,789 as people from different countries do.
3. Booleans in Python have a capital first character. i.e: `True` and `False`
4. The function `type(object)` can be used to get what's the type of the object.
5. Some casting functions: `int()`, `str()` and `float()`.
6. Division between integers produces a `float` as result.
7. `**` is an exponent operator. e.g.: `2 ** 3 => 8`
8. Some operators have the same priority and when multiple operators with the same priority are in the same expression the left operator precedes the right one.
9. Casting from float to int will truncate all the decimal values. Use `round(n)` to round a float to a whole int or `round(n, d)` to round `n` up to `d` decimal values.
10. `//` performs integer division.
11. `+=`, `-=`, `*=` and `/=` can be used in Python.
12. F-Strings are more convenient to print values other than strings as part of a meesage. e.g.: `print(f"your score is {score}")`