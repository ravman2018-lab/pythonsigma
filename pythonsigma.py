# Версия 2.0 - изменения в ветке feature
# Задача: найти все числа от 100 до 500, сумма цифр которых равна 15
count = 0
print("Числа от 100 до 500, сумма цифр которых равна 15:")
for i in range(100, 501):
    sum_digits = sum(int(digit) for digit in str(i))
    if sum_digits == 15:
        print(i, end=" ")
        count += 1

print(f"\nОбщее количество таких чисел: {count}")
