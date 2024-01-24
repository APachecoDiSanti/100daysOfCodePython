# Notes
1. There is no block scope in Python. If a definition is indented (i.e.: inside an `if` statement) but not inside a function, then it has global scope.
2. Variables created inside a function are only available inside the function. Even if they have the same name as a variable in the global scope!
3. To modify a variable with global scope you first want to define it inside your function using `global`. e.g.: `global counter`
4. Global constants should be named using uppercase as a convention. e.g.: `PI = 3.14159`
