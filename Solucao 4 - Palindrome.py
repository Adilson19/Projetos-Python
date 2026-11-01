def solution(string):
    #reversed_string = ''.join(reversed(string))
    #for index in reversed(range(len(string))):
    #    reversed_string += string[index]
    return string == string[::-1]
    