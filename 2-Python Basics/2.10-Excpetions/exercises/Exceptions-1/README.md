# Python basics - Exceptions-II

## IIa: Theoretical Warm Up

Write short answers (2-5 sentences) to the following questions:

1. Name three things that exception processing is good for.

    - Resource management(file operations, database connections)
    - Specific Error Handling
    - Handling unexpected events

2. What happens to an exception if you don’t do anything special to handle it?

    - The exception will be thrown/raised causing the program to stop execution and the exception will be present in the Traceback/Stack Trace.

3. How can your script recover (program continuation) from an exception?

    - We can use the try...except...finally block to catch and handle the exception. Further utitlizing the finally block to continue on with our program.

4. What is the `try` statement for?

    - Attempt to execute a specific block of code in case it throws an error/exception.

5. What are the two common variations of the `try` statement?

    - `try...except`
    - `try...except...finally`

6. What is the ```raise``` statement for?

    - Force the occurrence of an error/exception so it can be handled appropriately.

## IIb: Practical Warm Up (30 mins)

1. Place ```result="You can't divide by 0"``` in the correct place below such that the program avoids a ```ZeroDivisionError```.

    ```python
    #Type your answer below (pick the correct line).

    a=5
    b=0
    try:
        result=a/b
    except ZeroDivisionError:
        result="You can't divide by 0"


    print(result)
    ```

2. Place ```msg="You can't add int to string"``` in the correct place below such that the program avoids a ```BaseExceptionError```.

    - You can use ```except Exception```, although normally you should be careful using such powerful exception statements.

    ```python
    #Type your answer below.

    a="Hello World!"
    try:
        a + 10
    Exception:
        msg = "You can't add int to string"


    print(msg)
    ```

3. Place ```msg="You're out of list range"``` in the correct place below such that the program avoids an ```IndexError```.

    ```python
    #Type your answer below.

    lst=[5, 10, 20]

    try:
        print(lst[5])
    except IndexError:
        msg = "You're out of list range"


    print(msg)
    ```
