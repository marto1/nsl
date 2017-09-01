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
