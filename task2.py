"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?
"""
a = int(input("Всего журавликов: ")) 
p = a // 6 
k = p * 4 
print("Петя сделал -",p,"журавлик(а/ов)") 
print("Катя сделала -",k,"журавлик(а/ов)") 
print("Серёжа сделал -",p,"журавлик(а/ов)")
