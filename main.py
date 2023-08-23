def palindrome_check(string):
    string = string.replace(' ', '').lower()
    s_reversed = string[::-1]
    if string == s_reversed:
        return print('True')
    else:
        return print('False')


data = input()
palindrome_check(data)
