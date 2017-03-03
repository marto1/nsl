"""
General purpose forth implemented in python

Should eventually replace the messy one in p2psim.

Forth                          Python
stack 1 print                  print(stack)
   '  '  '
   '  '  '
   '  '  ' check print type, function so consume arguments and execute
   '  '-- number of items to pull from the stack
   ' check stack type, is variable so put on stack
" Hello world! " 1 print       print("Hello World!")

"""
from __future__ import print_function
from time import time, sleep
import fileinput
import sys
import inspect
import operator as op

# builtins

def print_pop(stack, words):
    """pop top and print it ( a -- )"""
    print (stack.pop())

def dup(stack, words):
    """duplicate top ( a -- a a )"""
    stack.append(stack[-1])

def negate(stack, words):
    """negate numeric value ( n -- -n )"""
    stack.append(-stack.pop())

def logic_and(stack, words):
    """logical and ( a b -- -1/0 )"""
    second = stack.pop() #prevent short circuit
    stack.append(stack.pop() and second)

def logic_or(stack, words):
    """logical or ( a b -- -1/0 )"""
    second = stack.pop() #prevent short circuit
    stack.append(stack.pop() or second)

def over(stack, words):
    """copy 2nd element to top ( a b -- a b a )"""
    stack.append(stack[-2])

def rrotate(stack, words):
    """place first element to 3rd place ( a b c -- c b a )"""
    el = stack.pop()
    stack.insert(-2, el)

def rotate(stack, words):
    """place 3rd element on top ( a b c -- c b a )"""
    el = stack.pop(-3)
    stack.append(el)

def swap(stack, words):
    """swap 2 topmost elements ( a b -- b a )"""
    second = stack.pop()
    first = stack.pop()
    stack.append(second)
    stack.append(first)

def invert(stack, words):
    """invert numerical value ( 0 -- -1 ; -1 -- 0 )"""
    stack.append(-1 if stack.pop() == 0 else 0)

def loop(stack, words):
    """take 'word and number, execute word n times  ( a n -- )"""
    number = stack.pop()
    word = stack.pop()[1:]
    w_list = [word]*number
    execute(w_list, stack, words)

class WordList(list): #cannot add func_doc to list
    pass

def define_end(stack, words):
    """end of definition."""
    definition = WordList()
    while len(stack) > 0:
        el = stack.pop()
        if type(el) == str and el == ":":
            name = definition.pop()
            definition.reverse()
            words[name] = definition
            break
        else:
            definition.append(str(el))
    return 0    


def exec_external(stack, words):
    """Execute a python statement and return to stack if not None"""
    cmd = 'res = {}'.format(stack.pop())
    code = compile(cmd, "script", "exec")
    ns = dict(glob)
    exec(code, ns)
    if ns["res"]: #only if its not None we want it on the stack
        stack.append(ns["res"])

def call(stack, words):
    """call function recorded on the stack with arguments ( a n -- )"""
    argcount = stack.pop()
    func = stack.pop()
    if argcount == -1: #FIXME
        stack.append(func)
        return
    args = [stack.pop() for i in range(argcount)]
    args.reverse()
    res = func(*args)
    if res != None:
        stack.append(res)

def none(stack, words):
    """None constant"""
    stack.append(None)

def call_python(token, argcount, isbuilt):
    if argcount == -1:
        if isbuilt:
            stack.append(builtins[token])
        else:
            stack.append(glob[token])
        return
    args = stack[-argcount:]
    del stack[-argcount:]
    if isbuilt:
        res = builtins[token](*args)
    else:
        res = glob[token](*args)
    if res != None:
        stack.append(res)

    
global_words = {
    ".": print_pop,
    "dup": dup,
    "over": over,
    "rrot": rrotate,
    "rot": rotate,
    "swap": swap,
    ";": define_end,
    ":": lambda x: x,
    "negate": negate,
    "and": logic_and,
    "or": logic_or,
    "invert": invert,
    "loop": loop,
    "exec": exec_external,
    "call": call,
    "None": none,
}
# end builtins

# global stack
stack = []
glob = globals()
b = glob['__builtins__']
if type(b) == dict: #profilers change module to dict
    builtins = dict(b)
else:
    builtins = dict(b.__dict__)
quoted_stack = []
quote_flag = False
ignore = False

# interpreter
def execute(tokens, stack, words):
    global quoted_stack, quote_flag, ignore
    for token in tokens:
        if token == "\"":
            if quote_flag:
                stack.append(" ".join(quoted_stack))
                quote_flag = False
            else:
                quoted_stack = []
                quote_flag = True
            continue
        if quote_flag:
            quoted_stack.append(token)
            continue
        if token.lstrip("-").isdigit():
            stack.append(int(token))
        else:
            if token not in words:
                isbuilt = token in builtins
                if not ignore and (isbuilt or token in glob):
                    if isbuilt or callable(glob[token]):
                        argcount = stack.pop()
                        call_python(token, argcount, isbuilt)
                    else:
                        stack.append(glob[token])
                    continue
                stack.append(token)
            else:
                if token == ":":
                    stack.append(token)
                    ignore = True
                    continue
                if ignore and token != ";":
                    stack.append(token)
                    continue
                func = words[token]
                if type(func) == WordList:
                    res = execute(func, stack, words)
                else:
                    res = func(stack, words)
                if res != None:
                    ignore = False

def read_line_and_execute(line):
    line = line[:-1].rstrip()
    tokens = line.split(" ")
    execute(tokens, stack, global_words)

def read_file_and_execute(filename):
    with open(filename, "r") as f:
        tokens = []
        for line in f:
            tokens.extend(line[:-1].rstrip().split(" "))
        execute(tokens, stack, global_words)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        read_file_and_execute(sys.argv[1])
    while True:
        read_line_and_execute(sys.stdin.readline())
