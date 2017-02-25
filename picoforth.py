"""
General purpose forth implemented in python

Should eventually replace the messy one in p2psim.
"""
from __future__ import print_function as printf
import fileinput
import sys


#docs

"""put stack size on top ( -- n )"""
"""print all defined words ( -- )"""
"""print stack ( -- )"""
"""take 'word from stack and print help for word"""

#end docs

# builtins

def print_pop(stack, words):
    """pop top and print it ( a -- )"""
    print (stack.pop())

def add(stack, words):
    """add two numeric values ( n1 n2 -- n1+n2 )"""
    first = stack.pop()
    stack.append(stack.pop() + first)

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

def bigger(stack, words):
    """bigger than test ( a b -- -1/0 )"""
    second = stack.pop()
    stack.append(-1 if stack.pop() > second else 0)

def smaller(stack, words):
    """smaller than test ( a b -- -1/0 )"""
    second = stack.pop()
    stack.append(-1 if stack.pop() < second else 0)

def equal(stack, words):
    """equality test ( a b -- -1/0 )"""
    second = stack.pop()
    stack.append(-1 if second == stack.pop() else 0)

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

def define_end(stack, words):
    """end of definition."""
    definition = []
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

def strings(stack, words):
    """quote string ( a b.. -- a )"""
    newstr = []
    while len(stack) > 0:
        el = stack.pop()
        if type(el) == str and el == "\"":
            break
        else:
            newstr.insert(0, el)
    stack.append(" ".join(newstr))
    return 0

def exec_external(stack, words):
    """Execute a python statement and return to stack if not None"""
    cmd = 'res = {}'.format(stack.pop())
    code = compile(cmd, "script", "exec")
    ns = dict(globals())
    exec(code, ns)
    if ns["res"]: #only if its not None we want it on the stack
        stack.append(ns["res"])
    
words = {
    # ".s": print_stack,
    ".": print_pop,
    "+": add,
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
    ">": bigger,
    "<": smaller,
    "=": equal,
    "loop": loop,
    "exec": exec_external,
    "\"": strings,
}
# end builtins

# global stack
stack = []

# interpreter
def execute(tokens, stack, words):
    ignore = False
    for token in tokens:
        if token.lstrip("-").isdigit():
            stack.append(int(token))
        else:
            if token not in words:
                stack.append(token)
            else:
                if token == ":" or (token == "\"" and not ignore):
                    stack.append(token)
                    ignore = True
                    continue
                if ignore and token not in [";", "\""]:
                    stack.append(token)
                    continue
                func = words[token]
                if type(func) == list:
                    res = execute(func, stack, words)
                else:
                    res = func(stack, words)
                if res != None:
                    ignore = False

def read_line_and_execute(line):
    line = line[:-1].rstrip()
    tokens = line.split(" ")
    execute(tokens, stack, words)

def read_file_and_execute(filename):
    with open(filename, "r") as f:
            for line in f:
                read_line_and_execute(line)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        read_file_and_execute(sys.argv[1])
    while True:
        read_line_and_execute(sys.stdin.readline())
