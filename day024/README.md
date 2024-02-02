# Notes
1. `open()` is the function used to open files and doesn't need to be imported to be used.
2. If you call `read()` on the stream returned by `open()` it will return all the contents of the file as a string.
3. If you call `close()` on the stream returned by `open()` it will close the file and free some resources for the program.
4. The `with` keyword can be used to open a file, give the stream a name and automatically close the file once the `with` block has finished (e.g.: `with open("my_file.txt") as file:`)
5. `open()` will create the file for you if it doesn't exist.
6. `open()` can open the file in different modes of use: `w`rite, `a`ppend and `r`ead (default).