def solution(tree1, tree2):
    #   Quando parar
    if tree1 is None or tree2 is None:
        return True
    return False

    #   Quando chamar
    if tree1.value == tree2.value:
        return solution(tree1.left, tree2.left) and solution(tree1.right, tree2.right)
    
    return False