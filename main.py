# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

resultListAlg = []
intermediate_list = []

def start():
    print('Вас приветствует программа для вычисления hash')

    while 1:
        print('В каком виде у вас сообщение?')
        print('0 - в двоичном')
        checkTypeMessage = input('1 - в текстовом\n')

        if checkTypeMessage == '0':
            bit_sms = input('Пожалуйста введите сообщение...\n')
            break
        if checkTypeMessage == '1':
            sms = input('Пожалуйста введите сообщение...\n')
            bit_sms = ''.join(format(ord(x), '08b') for x in sms)
            print('Ваше сообщение в двоичном виде', bit_sms)
            break
        print('По-моему вы ошиблись(')
        print('Ну ничего, всегда есть возможность выбрать заново')

    while 1:
        print('В каком виде у вас H0?')
        print('0 - в двоичном')
        checkTypeH0 = input('1 - в текстовом\n')

        if checkTypeH0 == '0':
            H0 = input('Пожалуйста введите H0...\n')
            break
        if checkTypeH0 == '1':
            H0 = input('Пожалуйста введите H0...\n')
            H0 = ''.join(format(ord(x), '08b') for x in H0)
            break
        print('По-моему вы ошиблись(')
        print('Ну ничего, всегда есть возможность выбрать заново')

    resultListAlg.append(H0)
    len_bit_sms = len(bit_sms)
    len_H0 = len(H0)
    remainder = len_bit_sms % len_H0

    if remainder > 0:
        factor = len_bit_sms // len_H0
        difference = len_bit_sms - len_H0 * factor
        for i in range(difference):
            if i == 0:
                bit_sms += '1'
            if i > 0:
                bit_sms += '0'
        print('Мы тут пошуршали и докинули пару битиков, чтобы алгоритм работал корректно...')
        print('Отредактированная битовая последовательность: ', bit_sms)
        list_bit_sms = [bit_sms[i:i + len_H0] for i in range(0, len(bit_sms), len_H0)]
    else:
        list_bit_sms = [bit_sms[i:i + len_H0] for i in range(0, len(bit_sms), len_H0)]

    i = 0

    print('*чик-чик*')
    print('А ой, мы тут порезали твою битовую последовательность на равные части, для дальшейших манипуляций.')
    print('Взгляни, что получилось:')
    for elem in list_bit_sms:
        i += 1
        print(i, '-ый элемент списка: ', elem)

    print('Эх...ну разве не красота? \n')

    while 1:
        print('Какой алгоритм необходимо использовать?')
        print('Если вам нужен алгоритм Метиса Мейера введите - 0')
        checkAlgoritm = input('Если вам нужен алгоритм Девиса Мейера введите - 1\n')
        if (checkAlgoritm == '0'):
            algorithmMathias_Meyer(list_bit_sms)
            print_decision_algorithm(sms, bit_sms, H0, list_bit_sms, checkAlgoritm)
            break
        if (checkAlgoritm == '1'):
            algorithmDavis_Meyer(list_bit_sms)
            print_decision_algorithm(sms, bit_sms, H0, list_bit_sms, checkAlgoritm)
            break
        print('По-моему вы ошиблись(')
        print('Ну ничего, всегда есть возможность выбрать заново')


def algorithmMathias_Meyer(list_bit_sms):
    i = 0
    for elem in list_bit_sms:
        firstItem = resultListAlg[i]
        secondItem  = elem
        intermediate_list.append(bit_addition(firstItem,secondItem))
        resultListAlg.append(bit_addition(intermediate_list[i],secondItem))
        i+=1

def algorithmDavis_Meyer(list_bit_sms):
    i = 0
    for elem in list_bit_sms:
        firstItem = resultListAlg[i]
        secondItem = elem
        intermediate_list.append(bit_addition(firstItem, secondItem))
        resultListAlg.append(bit_addition(intermediate_list[i], firstItem))
        i += 1



def print_decision_algorithm(message, bit_message, HASH0, list_bit_sms,checkAlgoritm):
    print('Опачки...Тута решение подкатило 0_0...')

    print('Введенное сообщение: ', message)
    print('Сообщение в двоичном виде: ', bit_message)
    print('H0 = ', HASH0)
    print()

    i = 0
    for elem in list_bit_sms:
        print(i,'-ая операция')
        print(resultListAlg[i])
        print('+')
        print(elem)
        print(separation('-',len(elem)))
        print(intermediate_list[i])
        print('+')
        if(checkAlgoritm == '0'):
            print(elem)
        if(checkAlgoritm == '1'):
            print(resultListAlg[i])
        print(separation('-',len(elem)))
        print(resultListAlg[i+1])
        if i == len(list_bit_sms)-1:
            print()
            print('Где деньги ЛЕБОВСКИ ???!!!')
        else:
            print(separation('=', len(elem)))
        print()
        i += 1


def separation(ch, length):
    stroka = ''
    for i in range(length):
        stroka += ch
    return stroka


def bit_addition(firstItem, secondItem):
    result_bit_addition = ''
    for i in range(len(firstItem)):
        if (firstItem[i] == secondItem[i]):
            result_bit_addition += '0'
        else:
            result_bit_addition += '1'
    return result_bit_addition




#шлепаем точку старта в самом конце
start()