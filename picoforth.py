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
# "duplicate top ( a -- a a )"

def negate_func(stack, words):
    """negate numeric value ( n -- -n )"""
    stack.append(-stack.pop())

def over_func(stack, words):
    """copy 2nd element to top ( a b -- a b a )"""
    stack.append(stack[-2])

def swap_func(stack, words):
    """swap 2 topmost elements ( a b -- b a )"""
    second = stack.pop()
    first = stack.pop()
    stack.append(second)
    stack.append(first)

def loop_func(stack, words):
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

def call_func(stack, words):
    """call function recorded on the stack with arguments ( a n -- )"""
    argcount = stack.pop()
    func = stack.pop()
    if argcount == -1: #FIXME
        stack.append(func)
        return
    args = stack[-argcount:]
    del stack[-argcount:]
    res = func(*args)
    if res != None:
        stack.append(res)

def none_func(stack, words):
    """None constant"""
    stack.append(None)

def call_python(token, stack, argcount, isbuilt):
    if argcount == -1:
        if isbuilt:
            stack.append(builtins[token])
        else:
            stack.append(glob[token])
        return
    args = stack[-argcount:]
    del stack[-argcount:]
    if isbuilt:
        # print("{}! {} {} {}".format(token , args, argcount, len(stack)))
        res = builtins[token](*args)
    else:        
        res = glob[token](*args)
    if res != None:
        stack.append(res)

global_words = {
    "over": over_func,
    "swap": swap_func,
    ";": define_end,
    ":": lambda x: x,
    "negate": negate_func,
    "loop": loop_func,
    "exec": exec_external,
    "call": call_func,
    "none": none_func,
}
# end builtins

# global stack
global_stack = []
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
def execute(tokens, lstack, words):
    global quoted_stack, quote_flag, ignore
    glob["stack"] = lstack
    glob["global_words"] = words
    for token in tokens:
        if token == "\"":
            if quote_flag:
                lstack.append(" ".join(quoted_lstack))
                quote_flag = False
            else:
                quoted_lstack = []
                quote_flag = True
            continue
        if quote_flag:
            quoted_lstack.append(token)
            continue
        if token.lstrip("-").isdigit():
            lstack.append(int(token))
        else:
            if token not in words:
                isbuilt = token in builtins
                if not ignore and (isbuilt or token in glob):
                    if isbuilt or callable(glob[token]):
                        argcount = lstack.pop()
                        call_python(token, lstack, argcount, isbuilt)
                    else:
                        lstack.append(glob[token])
                    continue
                lstack.append(token)
            else:
                if token == ":":
                    lstack.append(token)
                    ignore = True
                    continue
                if ignore and token != ";":
                    lstack.append(token)
                    continue
                func = words[token]
                if type(func) == WordList:
                    res = execute(func, lstack, words)
                else:
                    res = func(lstack, words)
                if res != None:
                    ignore = False

def read_line_and_execute(line, stack, words):
    line = line[:-1].rstrip()
    tokens = line.split(" ")
    execute(tokens, stack, words)

def read_file_and_execute(filename, stack, words):
    with open(filename, "r") as f:
        tokens = []
        for line in f:
            tokens.extend(line[:-1].rstrip().split(" "))
        execute(tokens, stack, words)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        read_file_and_execute(sys.argv[1], global_stack, global_words)
    while True:
        read_line_and_execute(
            sys.stdin.readline(),
            global_stack,
            global_words)
