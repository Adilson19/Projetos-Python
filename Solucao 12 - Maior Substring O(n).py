S = 'abcabcss'

# O(n)
def solution(s):
    #   Valor da variavel result que vai retornar o numero maximo de valores que ha na hash_table
    result = 0

    # Primeiro ponteiro andando ate o final da String
    for first_pointer in range(len(s)):
        hash_table = {s[first_pointer]: True}
        second_pointer = first_pointer

        while True:
            second_pointer += 1
            if second_pointer >= len(s) or s[second_pointer] in hash_table:
                result = max(len(hash_table.keys()), result)
                break

            hash_table[s[second_pointer]] = True

    return result