Description
===========

Simple forth-like language  that wraps around Python.

```
Forth                          Python
stack 1 print                  print(stack)
   '  '  '
   '  '  '
   '  '  ' check print type, function so consume arguments and execute
   '  '-- number of items to pull from the stack
   ' check stack type, is variable so put on stack
" Hello world! " 1 print       print("Hello World!")
x : " Hello " 1 print ; def    def x(): print("Hello")
' '   '               '  '
' '   '               '  '  define keyword
' '   '               ' end definiton block
' '   'definition block
' 'begin definition block
'definition name
```

DEMO
====

[![demo](https://asciinema.org/a/DmbDcipJAIOdR5hE8wYHychfN.png)](https://asciinema.org/a/DmbDcipJAIOdR5hE8wYHychfN?autoplay=1)


Dependencies
============

Python 2.7.x or 3.x

Quick Guide
===========

Start the interpreter:

` python picoforth.py basics.fth `

This will load the runtime and import basic functionality as well
as documentation for Forth definitions.

You can now do usual Forth stuff:

` 2 3 + . ` to print sum 2 + 3 and pop and print the result.

` 2 dup .s ` to duplicate 2 and print stack.

` 'dup .help ` will print help string for the dup definition.

` " Hello, this is a string " ` will put a string to the stack.

` bye ` to exit.

You can call help for all definitions by prefixing the definition
with ' and calling .help on it.

To call a Python function just call it as usual, but make sure the
first argument is the number of arguments the function takes.

For example: ` " Hello, world! " 1 len . ` will print the length.

See examples/ directory for more.
