# Notes
1. `tkinter.Tk()` creates a window.
2. `window.mainloop()` should be at the bottom of the code so the window listens for user interactions.
3. `component.pack()` will automatically center and position the component in the window.
4. Functions can have default argument values that don't need to be provided when calling the function. (e.g.: `def fun(a=1, b=2, c=3)` can be called without arguments `fun()`).
5. Unlimited arguments can be passed to a function's parameter defined with an `*` preceding its name. This will be a tuple with all the multiple arguments provided by the caller.
6. `*args` as a function parameter is also called unlimited positional arguments.