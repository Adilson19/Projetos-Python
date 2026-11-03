#   teste
#   len = 5
#   rev_index = 4
#   range(5) -> 0, 1, 2, 3, 4
def solution(string):
    rev_index = len(string) - 1
    try:
        for index in range(len(string)):
            if index == rev_index:
                return True
            
            if string[index] != string[rev_index]:
                return False
            rev_index -= 1
        return True
    except TypeError:
        return False
print(solution(None))