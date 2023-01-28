#1. Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.
A = int(input('A = '))
B = int(input('B = '))
if A <= B:
    for i in range(A - 1, B):
        i = i + 1
        print(i, end=' ')
else:
    print('A > B')

#2. Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в порядке убывания в противном случае.
A = int(input('A = '))
B = int(input('B = '))
if A < B:
    i = A
    while i <= B:
        print(i, end=' ')
        i += 1
else:
    i = A
    while i >= B:
        print(i, end=' ')
        i -= 1
