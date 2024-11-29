#       Самостоятельная работа по уроку "Рекурсия"
#       Задача "Рекурсивное умножение цифр"

def get_multiplied_digits(number):
    str_number = str(number)                                                    #   временная переменная
    if len(str_number)>1:                                                       #   условие рекурсии
        first = int(str_number[0]) * get_multiplied_digits(int(str_number[1:])) #   Рекурсия
    elif int(str_number[0]) == 0:                                               #   проверка нуля на конце
        first = 1                                                               #   игнорирование нуля
    else:
        first = int(str_number)                                                 #   последний множитель
    return first                                                                #   возврат

result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)


