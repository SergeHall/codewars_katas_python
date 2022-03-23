#  Write a function that takes an integer as input, and returns the number
#  of bits that are equal to one in the binary representation of that number.
#  You can guarantee that input is non-negative.
# Example: The binary representation of 1234 is 10011010010, so the function
# should return 5 in this case


def count_bits(my_str):
    count_1 = 0
    for i in bin(my_str)[2:]:
        if int(i) == 1:
            count_1 += 1
    return count_1


count_bits(10)
