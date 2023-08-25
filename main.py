def palindrome_check(string):
    string = string.replace(' ', '').lower()
    s_reversed = string[::-1]
    if string == s_reversed:
        return True
    else:
        return False


data = input()
palindrome_check(data)
