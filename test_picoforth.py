"""
Black box tests for picoforth.
"""
import pytest
from picoforth import execute, global_words, read_file_and_execute

#each input tuple represents:
# tokens -> result in stack
operations = [
    (["-10", "-9", "+"], -19),
    (["-10", "20", "+"], 10),
    (["0", "1", "+"], 1),
    (["10", "20", "+"], 30),
    (["-10", "-9", "-"], -1),
    (["-10", "20", "-"], -30),
    (["0", "1", "-"], -1),
    (["10", "20", "-"], -10),
    (["0", "1", "*"], 0),
    (["0", "0", "*"], 0),
    (["4", "5", "*"], 20),
    (["0", "5", "*"], 0),
    (["0", "5", "*"], 0),
    (["10", "2", "*"], 20),
    (["-2", "-3", "*"], 6),
    (["2", "-3", "*"], -6),
    (["1", "1", "xor"], 0),
    (["1", "0", "xor"], -1),
    (["0", "0", "xor"], 0),
    (["0", "1", "xor"], -1),
    (["1", "1", "="], -1),
    (["0", "1", "="], 0),
    (["20", "30", "="], 0),
    (["HLFD", "HLFD", "="], -1),
    (["SSd", "SSD", "="], 0),
    (["4", "5", ">"], 0),
    (["5", "5", ">"], 0),
    (["6", "5", ">"], -1),
    (["4", "5", "<"], -1),
    (["5", "5", "<"], 0),
    (["6", "5", "<"], 0),
    (["4", "5", "<="], -1),
    (["5", "5", "<="], -1),
    (["6", "5", "<="], 0),
    (["4", "5", ">="], 0),
    (["5", "5", ">="], -1),
    (["6", "5", ">="], -1),
    (["true"], -1),
    (["false"], 0),
    (["2", "0>"], -1),
    (["0", "0>"], 0),
    (["-1", "0>"], 0),
]

stack_op = [
    # (["6", "5", "nip"], [5]),
    (["6", "5", "dup"], [6, 5, 5]),
    (["6", "5", "over"], [6, 5, 6]),
    (["6", "5", "swap"], [5, 6]),
    (["1", "negate"], [-1]),
    (["None"], [None]),
    (["-1", "invert"], [0]),
    (["0", "invert"], [-1]),
    (["20", "invert"], [-21]),
]

read_file_and_execute("basics.fth")

@pytest.mark.parametrize("tokens, result", operations)
def test_tos(tokens, result):
    stack = []
    execute(tokens, stack, global_words)
    assert stack[-1] == result

@pytest.mark.parametrize("tokens, result", stack_op)
def test_stack_op(tokens, result):
    stack = []
    execute(tokens, stack, global_words)
    assert stack == result
