money_capital = 10000
salary = 5000
spend = 6000
increase = 1.05
x = 0
month = 0  # количество месяцев, которое можно прожить


while money_capital + salary > x:
    x = spend * increase ** month
    money_capital -= x - salary
    salary = 5000
    month += 1


print(month)
