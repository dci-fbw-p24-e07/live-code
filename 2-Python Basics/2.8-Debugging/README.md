# Debugging

- What is debugging?
- Interpreting a Python StackTrace/Traceback
- Debugging with VS Code
- Debugging with `pdb`

## What is debugging?

- Is the process of identifying the source of errors in your code and fixing them.
- This could anything from a syntax error to a general issue with the flow of the program

### Where did the term debugging originate?

The term debugging can be traced back to Admiral Grace Hopper, who worked at Harvard University in the 1940s. When one of her colleagues found a moth impeding the operation of one of the university's computers, she told them they were debugging the system. Computer programmers were first recorded as using the terms bugs and debugging by the 1950s, and by the early 1960s, the term debugging was commonly accepted in the programming community.

### The debugging process


1. Error identification

    - Developers, testers and end-users report bugs discovered while testing or using the software. 
    - Developers locate the exacts lines of code responsible for the error/bug. 
    - This can a time-consuming process depending on the size of your code base

2. Error analysis

    - Developers analyze the error by recording all program state changes and data values/variables.
    - This is usually done using a debugging tool to make the process simpler.

3. Fix and validation

    - Developers fix the bug and run tests to ensure the software continues to work as expected.
    - They may write tests to check if the bug recurs in the future.

### Interpreting the StackTrace/Traceback

1. Understand the last in the trace as it gives you a summary of the error
2. The last File shown indicates the last place the code wan running before the error was raised.

### Debugging in VS Code

1. Ensure that you installed the `Python Debugger` extension developed by `Microsoft`
2. In order to use the debugger you need to set a breakpoint in your code 
    > The point at which you want to start analysing your code from
3. Run the debugger after the breakpoint has been set

### Debugging using `pdb` 

- This is built-in and comes with the standard Python installation
- Allows debugging through the console using a set of commands to step through the program
- In order to run `pdb` we can either:
    1. import it into the program and use the available functions to set a breakpoint

        ```python
        pdb.set_trace()
        # Line to be set as breakpoint
        ```

    2. Run python3 with the pdb command(s) in the terminal:

        ```shell
        python3 -m pdb <name-of-the-file>
        ```

**`pdb` Commands:**

| Command | Short form | Description |
|---------|------------|-------------|
| `args` | `a` | Print the argument list of the current function |
| `break` | `b` | Creates a breakpoint in the program execution |
| `continue` | `c` or `cont` | Continues the program |
| `help` | `h` | Provides a list of commands or help of a specified command |
| `jump` | `j` | Set the next to be executed |
| `list` | `l` | Print the source code around the current line |
| `next` | `n` | Continue execution until the next line in the current function is reached or returns |
| `step` | `s` | Execute the current line, stopping at the first possible occasion |
| `pp` | `pp` | Pretty-prints the value of the expression |
| `quit` or `exit` | `q` | Aborts the program |
| `return` | `r` | Continue execution until the current function returns |
