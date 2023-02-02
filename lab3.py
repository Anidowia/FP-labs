# Написать программу используя цикл for и while.
i = 1
print('while loop')
n = int(input('Until which number do you want me to print? '))
for i in range(1, n + 1):
    print(i, end=' ')
    i = i + 1
print('\nfor loop')
total = 0
number = int(input('Enter a number: '))
while number != 0:
    total += number  
    number = int(input('Enter a number: '))
print('total =', total)

# в функцию range() введите данные с разными типами и выведите на экран в разных примерах.
list = []
n = int(input())
for i in range(0,n):
    a = input()
    list.append(a)
print(list)


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
        
#3 Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно, в порядке убывания. В этой задаче можно обойтись без инструкции if.
A = int(input("A = "))
B = int(input("B = "))
for i in range(A - (A + 1) % 2, B - B % 2, -2):
    print(i, end=' ')

'''4. Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. 
Найдите ее, зная номера оставшихся карточек. Дано число N, далее N − 1 номер оставшихся карточек 
(различные числа от 1 до N). Программа должна вывести номер потерянной карточки.
Для самых умных: массивами и аналогичными структурами данных пользоваться нельзя.
'''
n = int(input("Enter the number of cards: "))
sum_of_cards = 0
for i in range(1, n + 1, +1):
    sum_of_cards += i

for i in range(n - 1):
    lost_card = int(input("Enter the number of the remaining card: "))
    sum_of_cards -= lost_card

print("The lost card is:", sum_of_cards)
