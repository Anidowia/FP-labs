'''Шерубаева Дина, группа лабораторной работы пн 12:10
Ввиду нахождения в другой стране по академической мобильности,
не могу присутствовать на лабораторных работах, поэтому пока сдаю задания только в виде файла
Устная защита будет проходить по прибытию в Казахстан, в конце февраля'''
print('Привет, на каком ты курсе?')
course = int(input())
if course == 1: #проверка на равенство
    print('Рада тебя видеть на первом курсе, ты только начинаешь свой путь')
elif course == 2: #elif - сокращение от else if
    print('Рада тебя видеть на втором курсе')
elif course == 3:
    print('Круто, что ты на третьем курсе, ты уже близок к выпуску')    
elif course == 4: 
    print('Поздравляю, ты на четвертом курсе, скоро ты выпускник')
elif course > 4:
    print('Ты уже выпускник?')
else: #если ни одно из условий не выполняется
    print('Скорее всего, ты не студент') 

    
