def reverse(string):
    reversed_string = ''
    for i in reversed(range(len(string))):
        reversed_string += string[i]
    return reversed_string


print(reverse('Hello, World!'))
