
#Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов, после чего дробная часть
#копеек отбрасывается.Требуется определить: через сколько лет вклад составит не менее Y рублей.
#Пример:
#100
#10
#200
#Вывод:
#8


print('Сумма вклада: ')
deposit = int(input())
print('Процент по вкладу: ')
percent = int(input())
print('Ожидаемая сумма: ')
deposit2= int(input())
years=0
while deposit<deposit2:
    deposit = deposit+(deposit*percent/100)
    years+=1
print(years)