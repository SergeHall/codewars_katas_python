# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.
#
# Example:
# Given an input string of:
# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:
# apples, pears
# grapes
# bananas
# The code would be called like so:
#
# var result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# // result should == "apples, pears\ngrapes\nbananas"

def solution(string, markers):
    new_str = ""
    flag = True

    for i in string:
        if i in markers:
            flag = False
            continue

        if i == " ":
            if flag:
                new_str += " "
                continue

            if not flag:
                new_str += ""
                continue

        if i == "\n":
            flag = True
        if flag:
            new_str += i

    while "  " in new_str or " \n" in new_str:
        new_str = new_str.replace("  ", " ")
        new_str = new_str.replace(" \n", "\n")

    if new_str and new_str[-1] == " ":
        new_str = new_str[:-1]

    return new_str