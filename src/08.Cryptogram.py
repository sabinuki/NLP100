def cipher(input):
    result = ''
    if type(input) is str:
        for s in input:
            if s.isalpha() and s.islower():
                result += chr(219 - ord(s))
            else:
                result += s
        return result

    else:
        return input


lower_eng = 'apple'
upper_eng = 'APPLE'
str_jp = 'りんご'
str_num = '12345'
num = 12345
mix = 'AppLe'

print(cipher(lower_eng))
print(cipher(upper_eng))
print(cipher(str_jp))
print(cipher(str_num))
print(cipher(num))
print(cipher(mix))
