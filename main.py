# Задача 2: Найдите сумму цифр трехзначного числа.

# a = int(input("введите трехзначное число: "))
# k = a % 10
# a = a//10
# l = a % 10
# a = a//10
# print(a+l+k)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# a = int(input("Общее количество журавликов "))

# print('Петя сделал ', a//6)
# print('Сережа сделал ', a//6)
# print('Катя сделала ', a//6*4)

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# a = int(input("введите шестизначное число: "))
# sum1 = 0
# sum2 = 0
# while a > 1000:
#     sum1 = sum1+a % 10
#     a = a//10
# print(sum1)
# while a > 0:
#     sum2 = sum2+a % 10
#     a = a//10
# print(sum2)
# if sum1 == sum2:
#     print("Yes")
# else:
#     print("No")

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# n = int(input("введите первое число: "))
# m = int(input("введите второе число: "))
# k = int(input("введите третье число: "))

# if k<m and k<n:
#     print ('No')
# elif k%n==0 or k%m==0:
#     print ('Yes')
# else:
#     print ('No')
