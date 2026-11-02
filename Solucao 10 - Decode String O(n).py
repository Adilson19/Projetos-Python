#str_to_decode = '2[abc]3[cd]ef'
#result = ''
# 2[a]3[bc]
# '123' -> int(123)

# '1' -> 10 * 0 + 1 -> 1
# '2' -> 10 * 1 + 1 -> 12
# '3' -> 10 * 12 + 3 -> 123


def solution(str_to_decode):
    stack = []

    number = 0
    temp_str = ''
    for s in str_to_decode:
        if s == '[':
            if temp_str:
                stack.append(temp_str)
                temp_str = ''
            stack.append(number)
            number = 0
        elif s == ']':
            if temp_str:
                stack.append(temp_str)
                temp_str = ''
        else:
            if s.isdigit():
                number = 10 * number + int(s)
            else:
                temp_str += s