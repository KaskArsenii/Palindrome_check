def palindrome_check(s):
    s = s.replace(' ', '').lower()
    s_reversed = s[::-1]
    if s == s_reversed:
        print(True)
    else:
        print('False')


data = input()
palindrome_check(data)
