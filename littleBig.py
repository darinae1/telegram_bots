number = 50
count_of_atemps = 1

flag = True

while flag:
    try:
        answer = int(input('введите число: '))


         if number == answer:
            print('\nВы угадали!')
            print(f'Количество попыток: {count_of_atemps}')
            flag = False
        elif answer > number:
            print('Ваше число больше загаданного\n')
            count_of_atemps += 1
        else:
            print('Ваше число меньше загаданного\n')
            count_of_atemps += 1

    except ValueError:
        print('\n["ERROR"] Пожалуйста, введите целое число\n')


'5417083958:AAH1WwqO1oG6x52fKN3W6R7_mOAmFp4Nb9A'