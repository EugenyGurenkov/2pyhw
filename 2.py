# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. Факториал
# 5! = 120

number = int(input('Введите число: '))
factorial = 1
for i in range(2, number+1):
    factorial*= i
print(factorial)