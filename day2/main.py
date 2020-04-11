#!/usr/bin/env python3
import functools


def processIntCode(intcode):
    # print(f"processing type {type(intcode[0])}")
    currentIndex = 0
    while True:
        opcode = int(intcode[currentIndex])
        # print(f"current index {currentIndex} val {intcode[currentIndex]}")
        if opcode == 99:
            # print("opcode 99")
            break
        elif opcode == 1:
            # print("addition")
            first_operand = int(intcode[int(intcode[currentIndex + 1])])
            second_operand = int(intcode[int(intcode[currentIndex + 2])])
            position = int(intcode[currentIndex + 3])
            intcode[position] = str(first_operand + second_operand)
            # print(
            #     f"{first_operand} plus {second_operand} equal {intcode[position]}")

            currentIndex = currentIndex + 4
        elif opcode == 2:
            # print("multiplication")
            first_operand = int(intcode[int(intcode[currentIndex + 1])])
            second_operand = int(intcode[int(intcode[currentIndex + 2])])
            position = int(intcode[currentIndex + 3])
            intcode[position] = str(first_operand * second_operand)
            # print(
            #     f"{first_operand} times {second_operand} equal mult {first_operand * second_operand} stored val {intcode[position]}")
            currentIndex = currentIndex + 4
        else:
            # print("something went wrong")
            break
    # print(intcode)
    return intcode


def nested(outer, inner):
    for i in range(outer):
        for j in range(inner):
            yield i, j


testintcode = ["1", "9", "10", "3", "2",
               "3", "11", "0", "99", "30", "40", "50"]
processIntCode(testintcode)
test_two = ["1", "0", "0", "0", "99"]
processIntCode(test_two)
test_three = ["2", "3", "0", "3", "99"]
processIntCode(test_three)
test_four = ["2", "4", "4", "5", "99", "0"]
processIntCode(test_four)
test_five = ["1", "1", "1", "4", "99", "5", "6", "0", "99"]
processIntCode(test_five)


opcodes = {}
opcodes[1] = ("addition", 3)
opcodes[2] = ("multiplication", 3)
opcodes[99] = ("terminate", 0)
filename = "input.txt"
with open(filename, 'r') as f:
    line = f.readline()
    orig_intcode = [token.strip() for token in line.split(',')]
    orig_zero = orig_intcode[0]
    intcode = list(orig_intcode)
    intcode[1] = "12"
    intcode[2] = "2"
    processIntCode(intcode)
    print(f"part one {intcode[0]}")
    # find noun and verb to get 19690720

    needle = 19690720
    res = 0
    needle_noun = 0
    needle_verb = 0
    generator = nested(100, 100)
    for current_noun, current_verb in generator:
        copy = list(orig_intcode)
        copy[1] = str(current_noun)
        copy[2] = str(current_verb)
        processIntCode(copy)
        res = int(copy[0])
        # print(f" noun {noun} verb {verb} result {copy[0]}")
        if int(copy[0]) == 19690720:
            print("YAYYYY")
            needle_noun = current_noun
            needle_verb = current_verb
            break
    print(
        f"res for needle {needle} verify res {res} = {needle_noun}, {needle_verb} ")
