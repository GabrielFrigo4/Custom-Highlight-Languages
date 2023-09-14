str = input('DATA: ')
list = str.split()


result1 = ''
result2 = ''
for item in list:
    if item.endswith('ss') or item.endswith('sd') or item.endswith('ps') or item.endswith('pd'):
        result1 = f'{result1} {item}'
    else:
        result2 = f'{result2} {item}'


print(f'RESULT1:{result1}')
print(f'RESULT2:{result2}')
input('press \'enter\' to exit')