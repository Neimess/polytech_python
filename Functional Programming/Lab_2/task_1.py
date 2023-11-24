money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
mounth = 0
while True:
        money_capital += salary - spend
        spend *= (1+increase)
        if money_capital < 0:
            break
        mounth += 1
print("Количество месяцев, которое можно протянуть без долгов:", mounth)
