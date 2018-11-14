import os
import random
import time
print(
    'Здраствуйте!\nЭта игра на запоминания слов\nВам требуется запомнить слова на экране и после этого ввести их.Если вы запомните от 3 до 5 слов,то вам добавится 1 очко.Если от 5 до 7 ,то 2 очка Игра завершиться в том случае,если вы введете все слова не правильно или не введете слов вообще.\nЧтобы завершить игру досрочно введите: quit')
sch = 0  # schetchik пользователя
scp = 0  # Счет пользователя
n = 0  # количество слов
d = {}  # Словарь для рекордов
zap = ''  # Переменная для записи рекордов в файл
list_scor = []  # Список для рекордов
Prov = False  # проверка для выхода из цикла
Prov_2 = False  # проверка на ожинаковый результат в таблице рекордов
Name_p = ''
while True:
    Name = input('Введите ваше имя: ')
    soglas = input('Вы хотите начать игру Y/N: ')
    if soglas == 'Y':
        os.system('cls')
        sloz = input('Выберите уровень сложности:Easy,Middle,Difficult: ')
        if sloz == 'Easy':
            n = 3
        elif sloz == 'Middle':
            n = 5
        elif sloz == 'Difficult':
            n = 7
        else:
            print('Вы ввели что-то не то вы точно хотите начать игру?')
            continue
        while True:
            os.system('cls')
            with open('word_rus.txt', encoding='utf-8') as fs:
                a = fs.readlines()
            b = random.sample(a, n)
            b = [line.rstrip() for line in b]
            print(b)
            time.sleep(5)
            os.system('cls')
            slov_p = input('Введите слова через пробел: ').split()
            if slov_p == [] or slov_p[0] == 'quit':  # Проверка на выход
                break
            for i in range(int(len(slov_p))):  # Проверка правильности введеных слов
                if slov_p[i] in b:
                    sch += 1  # счетчик
                    scp += 1  # счет пользователя
                else:
                    Prov = True
                    break
            if Prov:
                break
            if 3 <= sch < 5:
                scp += 1
            elif 5 <= sch < 7:
                scp += 2
            sch = 0
            os.system('cls')
        print('Ваш счет: %d\n' % scp)
        if scp == 0:
            break
        """Запись рекордов"""
        if sloz == 'Easy':
            Tabl = 'Score_p_E.txt'
        elif sloz == 'Middle':
            Tabl = 'Score_p_M.txt'
        else:
            Tabl = 'Score_p_D.txt'
        with open(Tabl, 'r+') as fl:
            score = fl.read()
        list_scor = score.split(': ')
        for i in range(1, len(list_scor), 2):
            if scp == int(list_scor[i]):
                Prov_2 = True
                Name_p = list_scor[i - 1]
            d[int(list_scor[i])] = list_scor[i - 1]
        d[scp] = Name
        p = sorted(d, reverse=True)
        with open(Tabl, 'w') as fl:
            for i in range(len(p[:10])):
                p[i] = str(p[i])
                if str(scp) == p[i] and Prov_2:
                    zap = zap + Name_p + ': ' + p[i] + ': '
                zap = zap + str(d.get(int(p[i]))) + ': ' + p[i] + ': '
            zap = zap[:len(zap) - 2]
            fl.write(zap)
            '''Вывод таблицы рекордов'''
        with open(Tabl, 'r+') as fl:
            score = fl.read()
        list_scor = score.split(': ')
        print('Рекорд лист:\n')
        for i in range(0, len(list_scor) - 1, 2):
            print(list_scor[i] + ': ' + list_scor[i + 1])
        break

    elif soglas == 'N':
        exit()
    else:
        print('Вы ввели что-то не то,попробуйте снова')
        time.sleep(1)
        os.system('cls')
        continue
