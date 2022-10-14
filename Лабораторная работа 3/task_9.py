salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
x = 0 # разница между зарплатой и тратами
need_money = 0  # количество денег, чтобы прожить 10 месяцев
i = 0 # счетчик

while i <= 9:
    x = salary - spend * (1 + increase) ** i
    need_money -= x
    i += 1

print(round(need_money))
