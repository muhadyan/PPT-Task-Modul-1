# Solve it! 1
for i in range(1, 11):
    print(f'Nomor urut {i}')

# Solve it! 2
for i in range(0,21,2):
    print(f'Nomor urut {i}')
# or
for i in range(11):
    print(f'Nomor urut {i * 2}')

# Solve it! 3
for i in range(1,20,2):
    print(f'Nomor urut {i}')

# Solve it! 4
x = ''
for i in range(5):
    for j in range(5):
        x += ' * '
    x += '\n'

print(x)

# Solve it! 5
x = ''
for i in range(5):
    x += ' * '
    print(x)


# Solve it! 1
x = ''
y = 5
for i in range(y):
    x = ' * ' * (y - i)
    print(x)

# Solve it! 2
x = ''
y = 5
for i in range(y):
    x = ' * ' * (y - i)
    print(x)
for i in range(1,5):
    x += ' * '
    print(x)

# Solve it! 3
x = ''
y = 20
for i in range(1,y):
    if i % 2 != 0:
        x = ('  ' * int((y-i)/2)) + ' *' * i + ('  ' * int((y-i)/2))
        print(x)

# Solve it! 4
x = ''
y = 20
for i in range(1,y):
    if i % 2 != 0:
        x = ('  ' * int((i+1)/2)) + '* ' * (y-i) + (' ' * int((i+1)/2))
        print(x)

# Solve it! 5
x = ''
y = 10
for i in range(1,y):
    if i % 2 != 0:
        x = ('  ' * int((y-i)/2)) + ' *' * i + ('  ' * int((y-i)/2))
        print(x)
x = ''
y = 10
for i in range(1,y):
    if i % 2 != 0:
        x = ('  ' * ((int((i+1)/2))-1)) + ' *' * (y-i) + ('  ' * int((i+1)/2))
        print(x)