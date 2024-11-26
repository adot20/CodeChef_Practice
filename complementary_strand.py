# You are given the sequence of Nucleotides of one strand of DNA through a string S of length N. S contains the character A,T,C, and G only.
# Chef knows that:
# A is complementary to T
# T is complementary to A
# C is complementary to G
# G is complementary to C

# Using the string S, determine the sequence of the complementary strand of the DNA.
test_case = int(input())
for _ in range(test_case):
    n = int(input())
    string = str(input())
    result_string = ""
    for i in string:
        if i == 'A':
            result_string += 'T'
        elif i == 'T':
            result_string += 'A'
        elif i == 'C':
            result_string += 'G'
        elif i == 'G':
            result_string += 'C'

    print(result_string)