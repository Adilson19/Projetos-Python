str_to_validate = '()[]{}'
def solution(str_to_validate):
    stack = []
    mapping = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    # O(n) - O(n) em questoes de tempo
    for s in str_to_validate:
        if s in mapping:
            if len(stack) and mapping[s] == stack.pop():
                continue
        stack.append(s)
    return len(stack) == 0
print(solution(str_to_validate))