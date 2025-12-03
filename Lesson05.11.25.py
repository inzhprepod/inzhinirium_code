name = 'Inginirium'

'''print(name[0:4:1])
print(name[4:0:-1])
print(name[:])
print(name[::-1])

print(chr(125))
print(ord('П'))
print(chr(ord('а') + 3))

for i in range(32):
    print(chr(ord('а') + i), chr(ord('А') + i), sep=' ~ ')
'''

stroka = input('Введите строку: ')
for i in range(len(stroka)):
    print(ord(stroka[i]), end=', ')


