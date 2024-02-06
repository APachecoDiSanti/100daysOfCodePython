# Notes
1. `tkinter.Tk()` creates a window.
2. `window.mainloop()` should be at the bottom of the code so the window listens for user interactions.
3. `component.pack()` will automatically center and position the component in the window. All components need to have their layout set, so they can appear on screen.
4. Functions can have default argument values that don't need to be provided when calling the function. (e.g.: `def fun(a=1, b=2, c=3)` can be called without arguments `fun()`).
5. Unlimited arguments can be passed to a function's parameter defined with an `*` preceding its name. This will be a tuple with all the multiple arguments provided by the caller.
6. `*args` as a function parameter is also called unlimited positional arguments.
7. `**kwargs` as a function parameter is used to provide multiple keyword arguments. 
8. `**kwargs` is a dictionary with the key as the parameter keyword and the value as the argument.
9. When a function is using unlimited keyword arguments, check the documentation to see what keywords are available and what do they do.
10. To get values from dictionaries we can also use `dict.get(key)` that will return `None` when `key` is not defined in `dict`.
11. In TKinter the `command` argument is to provide a function name to call when interacting with the UI component.