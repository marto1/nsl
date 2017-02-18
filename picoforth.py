"""
General purpose forth implemented in python

Should eventually replace the messy one in p2psim.
"""
import fileinput
import sys


# builtins

def print_stack(stack, words):
    print stack

def print_words(stack, words):
    print words.keys()

def print_pop(stack, words):
    print stack.pop()

def add(stack, words):
    first = stack.pop()
    stack.append(stack.pop() + first)

def dup(stack, words):
    stack.append(stack[-1])

def negate(stack, words):
    stack.append(-stack.pop())

def logic_and(stack, words):
    stack.append(stack.pop() and stack.pop())

def logic_or(stack, words):
    second = stack.pop() #prevent short circuit
    stack.append(stack.pop() or second)

def bigger(stack, words):
    second = stack.pop()
    stack.append(-1 if second > stack.pop() else 0)

def define_end(stack, words):
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


words = {
    ".s": print_stack,
    ".": print_pop,
    "+": add,
    "dup": dup,
    ";": define_end,
    ":": lambda x: x,
    "words": print_words,
    "negate": negate,
    "and": logic_and,
    "or": logic_or,
    ">": bigger,
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

if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            for line in f:
                read_line_and_execute(line)
    while True:
        read_line_and_execute(sys.stdin.readline())
