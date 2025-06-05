# argument_parsing

Create three applications in three files. Each of these is to parse arguments given on the command line. Read more about ways of doing that here: https://www.geeksforgeeks.org/command-line-arguments-in-python/.

app1.py
=====

The application in this file will read the command line options using `sys.argv`.

If one of the options is `--help`, it should output a small help text.

If one of the options is `--fast` is should print the text "fast mode enabled" to the command line.

If `--fast` is not one of the options it should print the text "slow mode enabled" to the command line.

app2.py
=====

The application in this file will read the command line options using `getopt()`.

This application should accept the flags `-h` or `--help` to print a help text.

This application should let the user set a name with the option `-n [NAME]` or `--name=[NAME]`. 

If a name is given, the application should output `Good Morning [NAME]!`. If no name is specified, it should just output `Good Morning folks!`

app3.py
=====

The application in this file will read the command line options using argparse.

This application should support positional arguments and be called like this: `./app3.py [FIRST_NAME] [LAST_NAME] [AGE]`

If age is not specified, it should be assumed that it is 100. If the last name is not specified, it should be assumed that it is "Hanson". If the first name
is not specified, should be assumed that it is "Larry".

This application should also support the option `--fast`. It should print "fast mode enabled" if this is one of the options.

The app should then output the text "Hello [FIRST_NAME] [LAST_NAME]! I see that you have had [AGE + 1] birthdays.".
