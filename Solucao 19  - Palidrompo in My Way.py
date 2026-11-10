def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    s == s[::-1]
    if s == s[::-1]:
        return True  # True
    else:
        return False  # False
print(is_palindrome("Arara"))  # True
print(is_palindrome("Ana"))  # False