"""
General purpose forth implemented in python

Should eventually replace the messy one in p2psim.
"""
import fileinput
import sys

def print_stack(stack, words):
    print stack

def print_words(stack, words):
    print words

def print_pop(stack, words):
    print stack.pop()

def add(stack, words):
    stack.append(stack.pop() + stack.pop())

def dup(stack, words):
    stack.append(stack[-1])

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

stack = []
words = {
    ".s": print_stack,
    ".": print_pop,
    "+": add,
    "dup": dup,
    ".": define_end,
    ":": lambda x: x,
    "words": print_words,
}

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
                if ignore and token != ".":
                    stack.append(token)
                    continue
                func = words[token]
                if type(func) == list:
                    res = execute(func, stack, words)
                else:
                    res = func(stack, words)
                if res != None:
                    ignore = False

if __name__ == '__main__':    
    while True:
        line = sys.stdin.readline()[:-1].rstrip()
        tokens = line.split(" ")
        execute(tokens, stack, words)
