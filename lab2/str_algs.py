def reverse(string):
    reversed_string = ''
    for i in reversed(range(len(string))):
        reversed_string += string[i]
    return reversed_string


def reverse_v2(string):
    return string[::-1]


print(reverse_v2('Hello, World!'))
