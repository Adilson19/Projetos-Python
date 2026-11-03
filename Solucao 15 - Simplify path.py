def solution(path):
    left = 0
    stack = []

    for right in range(len(path)):
        if path[right] == '/':
            current = path[left:right]
            left = right

            if current:
                if current == '/..':
                    if stack:
                        stack.pop()
                elif current == '/.':
                    continue
                else:
                    stack.append(current)
    if not stack:
        stack.append('/')

    return ''.join(stack)