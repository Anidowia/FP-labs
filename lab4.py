# Напишите программу, используя 10 функции и методы, связанные со строками
s1 = str(input())
s2 = str(input())
print('1, сложение строк: ', s1 + s2)
print('2, дублирование строк: ', s1 * 2)
print('3, длина строки: ', len(s1))
print('4, доступ по индексу: ', s1[0])
print('5, сравнение строк: ', s1 > s2)
print('6, проверка на число: ', s1.isnumeric())
print('7, начинаются ли слова в строке с прописной буквы: ', s2.islower())
print('8, написание с заглавной буквы: ', s2.capitalize())
print('9, проверка на пробелы: ', s1.isspace())
print('10, замена символов: ', s1.replace('a', 'b'))

# Напишите программу, в которой предлагается вводить учащихся различных груп, посещающих секции по программированию. Требуется упорядочить список по возрастанию классов. Распечатать список фамилий и классов. 
students = []
while True:
    student = input("Enter the name and class of a student (or type 'q' to quit): ")
    if student == 'q':
        break
    name, grade = student.split() 
    students.append((name, int(grade))) 
students.sort(key=lambda x: x[1]) #лямбда x: x[1] — короткая анонимная функция, возвращает 2 элемент каждого кортежа в списке, и sort использует его в качестве ключа сортировки.

for student in students:
    print(f"{student[0]}: Class {student[1]}")
    
'''1)Вводится строка, включающая строчные и прописные буквы. 
Требуется вывести ту же строку в одном регистре, который зависит от того, каких букв больше. 
При равном количестве преобразовать в нижний регистр. Например, вводится строка "HeLLo World", 
она должна быть преобразована в "hello world", потому что в исходной строке малых букв больше. 
Необходимо свой пример привести. В коде используйте цикл for, строковые методы upper() 
(преобразование к верхнему регистру) и lower() (преобразование к нижнему регистру), 
а также методы isupper() и islower(), проверяющие регистр строки или символа.'''

s = str(input("Введите строку: "))
lower_count = 0
upper_count = 0
for char in s:
    if char.islower():
        lower_count += 1
    elif char.isupper():
        upper_count += 1
if lower_count >= upper_count:
    print(s.lower())
else:
    print(s.upper())
    
#Input             Output
#GOOD Code       GOOD CODE



