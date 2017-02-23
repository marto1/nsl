"""
General purpose forth implemented in python

Should eventually replace the messy one in p2psim.
"""
import fileinput
import sys

# builtins

def print_stack(stack, words):
    """print stack ( -- )"""
    print stack

def stack_size(stack, words):
    """put stack size on top ( -- n )"""
    stack.append(len(stack))


def print_words(stack, words):
    """print all defined words ( -- )"""
    print words.keys()

def print_pop(stack, words):
    """pop top and print it ( a -- )"""
    print stack.pop()

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

def func_help(stack, words):
    """take 'word from stack and print help for word"""
    print words[stack.pop()[1:]].func_doc

def included(stack, words):
    """Include and execute a script file ( a n -- )"""
    read_file_and_execute(stack.pop())

words = {
    ".s": print_stack,
    ".": print_pop,
    "+": add,
    "dup": dup,
    "over": over,
    "rrot": rrotate,
    "rot": rotate,
    "swap": swap,
    ";": define_end,
    ":": lambda x: x,
    "words": print_words,
    "negate": negate,
    "and": logic_and,
    "or": logic_or,
    "invert": invert,
    ">": bigger,
    "<": smaller,
    "=": equal,
    "help": func_help,
    "ssize": stack_size,
    "loop": loop,
    "included": included,
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
                if token == ":":
                    stack.append(token)
                    ignore = True
                    continue
                if ignore and token != ";":
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
