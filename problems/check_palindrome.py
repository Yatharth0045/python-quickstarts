str = "aabbccbbaa"

def is_palindrome(str):
    str = str.lower()
    if str == str[::-1]:
        return True 
    else:
        return False

print(is_palindrome(str))
