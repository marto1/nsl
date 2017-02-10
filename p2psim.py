import re
import random
f = open("example_input1.txt", "r")


def tokenize(fileobj):
    """
    Probably the slowest forth tokenizer ever invented.
    """
    words = []
    for line in fileobj:
        if line.startswith("#"):
            continue
        else:
            line = re.sub('\s+',' ',line)
            if line == " ": continue
            w = line.split(" ")
            w = filter(lambda a: a != '', w)
            words.extend(w)
    return words

def parse(words):
    """
    Construct AST from tokens.
    Returns lists of (type, value) pairs.
    """
    ast = []
    for word in words:
        if word.isdigit():
            ast.append(('int', int(word)))
        else:
            ast.append(('word', word))
    return ast

def execute(ast, context):
    """
    Execute the AST using predefined context.

    Tolerates all unknown words.
    All known words must have a handler that takes all stacks as
    parameters.
    """
    stack = [] #main stack, contains mixed types
    variables = {} #dict of variables
    index = 0
    for node in ast:
        if node[0] == 'int':
            stack.append(node[1])
        elif node[0] == 'word':
            if node[1] not in context:
                stack.append(node[1])
            else:
                index = context[node[1]](stack, variables, index)
        index += 1
    print stack, variables

def assign(stack, variables, index):
    ntype = stack.pop()
    value = stack.pop()
    stack.append({"value": value, "type": ntype})
    return index-3

def create(stack, variables, index):
    """default "create from all of the above" word handler."""
    #block definition handling
    if ":" in stack:
        begin = stack.index(":")
        end = index
        name = stack[begin+1]
        variables[name]["definition"] = stack[begin+2:]
        del stack[begin:]
        return index-4
    #variable assingment
    name = stack.pop()
    val = stack.pop()
    variables[name] = val
    return index-3

def seconds(stack, variables, index):
    stack.append(stack.pop()*1000)
    return index-1

def KB(stack, variables, index):
    stack.append(stack.pop()*1000)
    return index-1

def B(stack, variables, index):
    return index-1

def calculate_all(variables):    
    nodes = 0
    for name, entry in variables.iteritems():
        if entry["type"] == "nodes":
            nodes += entry["value"]
    return nodes

def target_to_number(target, variables):
    if target == "all":
        nodes = calculate_all(variables)
        return nodes
    elif target == "random":
        nodes = calculate_all(variables)
        return random.randint(0, nodes)
    if target in variables:
        return variables[target]["value"]
    return 0
    
def sent(stack, variables, index):
    """reads "60, 'each', 2000, 'to', 'all'" and prepare equation"""
    subs = -3
    target = stack.pop()
    mod = 0
    while True:
        el = stack.pop()
        subs += 1
        if el == 'to':
            break
        elif el == 'other':
            mod -= 1

    nodes = target_to_number(target, variables)
    nodes += mod
    time = stack.pop()
    stack.pop() #each
    size = stack.pop()
    #compile equation
    stack.extend(["time", time, "/", size, nodes, "*", "*", ";"])
    return index - subs

def div(stack):
    first = stack.pop()
    second = stack.pop()
    stack.append(second/first)

def mult(stack):
    first = stack.pop()
    second = stack.pop()
    stack.append(second*first)

def sep(stack):
    res = stack.pop()
    print "result from calculation:", res

def run(stack, variables, index):
    time = stack.pop()
    print time
    context = {"/": div, "*": mult, ";": sep}
    for name, entry in variables.iteritems():
        if "definition" not in entry:
            continue
        definition = entry["definition"]
        definition = [time if a == 'time' else a for a in definition]
        #mini forth
        tmpstack = []
        for word in definition:
            if type(word) == int:
                tmpstack.append(word)
            else:
                context[word](tmpstack)
    return index-2

tokens = tokenize(f)
parsed = parse(tokens)
context = {
    "in": assign,
    ".": create,
    "seconds": seconds,
    "KB": KB,
    "B": B,
    "sent": sent,
    "run" : run
}

print "calculations are in bytes."
execute(parsed, context)
