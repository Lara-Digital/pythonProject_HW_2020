print("Задание 1")
name = "Кеша"
age = 2
period = 2
print("Попугайчик " + name + ' в ' + str(age) + ' года научился говорить свое имя - ' + name)
print()
print("Через " + str(period) + " года он научился говорить сколько ему лет - " + str(age + period))
print()
print()
print("Работа с числами и строками")
a = int(input('Введите первое число:'))
print(a)
print()
b = int(input('Введите второе число:'))
print(b)
print('Сумма этих чисел составляет: ' + str(a + b))
print()
text1 = input('Какого цвета у вас глаза?  ')
print()
text2 = input('Какого цвета у вас волосы?  ')
print()
print('Вы красавчик! :-)')
#
print()
print()
print("Задание 2")
sec = int(input("Введите секунды: "))
hours = sec // 3600
minutes = (sec - hours * 3600) // 60
seconds = sec - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours:02} : {minutes:02} : {seconds:02}")
''''''
print()
print()
print("Задание 3")
n = input("Введите целое число n: ")
nn = int(n + n)
nnn = int(n+n+n)
summa = int(n) + nn + nnn
print("Сумма чисел " + n + " + " + str(nn) + " + " + str(nnn) + " = " + str(summa))
''''''
print()
print()
print("Задание 4")
num_init = int(input("Введите целое положительное число: "))
max_dig = num_init % 10
num = num_init

while num > 0:
    digit = num % 10
    if digit > max_dig:
        max_dig = digit
        if max_dig ==9:
            break
    num = num // 10
print(f"Наибольшая цифра в числе {num_init} равна {max_dig}")
''''''
print()
print()
print("Задание 5")
revenue = float(input("Введите значение выручки компании (руб.) - "))
cost = float(input("Введите зеначение издержек вашей компании (руб.) - "))
result = revenue - cost
if result > 0:
    print(f"Поздравляем! Ваша компания работает с прибылью {result} (руб.)")
    print(f"Рентабельность выручки составила {result / revenue:.3f} (%)")
    personal_n = int(input("Введите количество сотрудников вашей компании (чел.) - "))
    print(f"Прибыль компании в расчете на одного сотрудника {result / personal_n:.3f} (руб.)")
elif result < 0:
    print(f"Ваша компания работает с убытком {-result} (руб.) Проанализируйте ситуацию и сделайте необходимые выводы!")
else:
    print(f"Ваша компания ничего не заработала, но и не потеряла! Хвост пистолетом!")
''''''
print()
print()
print("Задание 6")
while True:
    days = 1
    start_km = float(input("Стартовый результат (км.): "))
    last_km = float(input("Финальный результат (км.): "))
    if start_km <= 0 or last_km < 0:
        print("Результаты должны быть больше нуля. Стартовое значение !=0.")
    else:
        while start_km < last_km:
            start_km += start_km * 0.1
            days += 1

        print(f"Спортсмен добьется результата за {days} дней")
        break
