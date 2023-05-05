"""
    Автор: Покровский Антон
    Контрольная работа по 1 модулю
    Чтобы запустить задание, запустите программу и напишите номер задания!
"""
# import using modules
import random
#Tasks
def task1():
    """Задание 1"""
    A: int = int(input("Введите A: "))
    B: float = float(input("Введите B: "))
    print(f"A = {A}, B = {B}")
    C = A*B
    print(f"C = {C}")
def task2():
    """Задание 2"""
    def inputNumbers()-> list[int]:
        numbers: list[int] = []
        number = None
        while number != 999:
            number: int = int(input("Введите число: "))
            if number > 1000:
                raise ValueError("Число должно быть меньше 1000")
            if number == 999:
                break
            numbers.append(number)
        return numbers
    def main():
        numbers = inputNumbers()
        minNumber = min(numbers)
        print(f"Наименьшее из введеных чисел: {minNumber}")
        pass
    main()
def task3():
    """Задание 3"""
    string = input("Введите строку: ")
    print(string[1],string[-2],string[:3],string[:-2]
        , string[::-2],len(string),sep= "\n")
def task4():
    """Задание 4"""
    stroka = input("Введите строку: ")
    simvol = input("Введите символ: ")
    print(stroka.count(simvol))
def task5():
    """Задание 5"""
    korteg=(13, 2, 23, 14, 5)
    for number in korteg:
        if number > 10:
            print(number)
def task6():
    """Задание 6"""
    a = [5, -2, 5, 3, 4, 12, 17]
    positive_a = []
    for number in a:
        if number >= 0:
            positive_a.append(number)
    sr = sum(positive_a)/len(positive_a)
    print(sr)
def task7():
    """Задание 7"""
    my_func = lambda numList: sum(numList)
def task8():
    """Задание 8"""
    MONTHS: list[str] = ["января", "февраля", "марта"
                        ,"апреля", "мая", "июня"
                        ,"июля", "августа", "сентября"
                        ,"октября", "ноября", "декабря"]
    dictMonths: dict = {}
    for i in range(len(MONTHS)):
        dictMonths[MONTHS[i]] = i + 1
def task9():
    """Задание 9"""
    A = set()
    B = set()
    for i in range(10):
        A.add(random.randrange(1,20))
    for i in range(5):
        B.add(random.randrange(1,20))
    print(A,B,sep="\n")
def task10():
    """Дополнтельное задание 10"""
    def find_quarter(x,y):
        quarter = None
        if (x > 0) and (y > 0):
            quarter = 1
        elif (x > 0) and (y < 0):
            quarter = 2
        elif (x < 0) and (y < 0):
            quarter = 3
        elif (x < 0) and (y > 0):
            quarter = 4
        else: raise ValueError("Координата не находиться в четвертях")
        return quarter
    x = float(input("x = "))
    y = float(input("y = "))
    try:
        print(f"x = {x}\ny = {y}")
        print(f"Ваша координата лежит на {find_quarter(x,y)} четверти")
    except ValueError:
        print("Ваша координата не находиться ни в одной из четвертях, тк ",end = "")
        if (x == 0) and (y == 0):
            print("Ваша точка в центре")
        elif (x != 0) or (y != 0):
            if x == 0: print("Ваша координата лежит на оси x")
            else:      print("Ваша координата лежит на оси y")
def task11():
    """Дополнительное задание 11"""
    def findVovelWords(string: str) -> list[str]:
        VOVELLETTER = "АУОЫИЭЯЮЁЕYOUAIE"
        vovelWords = []
        wordslist = string.split()
        for word in wordslist:
            if word[0].upper() in VOVELLETTER:
                vovelWords.append(word)
        return vovelWords
    string = input("Введите строку: ")
    vovelsWord = findVovelWords(string)
    print(vovelsWord)
def task12():
    """Дополнительное задание 12"""
    ArithmeticOperations = {(lambda a,b: a+b) : "+",
                            (lambda a,b: a-b) : "-",
                            (lambda a,b: a*b) : "*",
                            (lambda a,b: a/b) : "/"}
    a = int(input("1-ое число: "))
    b = int(input("2-ое число: "))
    operation = input("(*,/,+,-): ")
    for arithOperation in ArithmeticOperations.items():
        if operation == arithOperation[1]:
            result = arithOperation[0](a,b)
            break
    else: print("Нет такой операции")
    print(result)
def task13():
    """Дополнительное задание 13"""
    S =lambda A,B,C: abs(((B[0]-A[0])*(C[1]-A[1]) - (C[0]-A[0])*(B[1]-A[1]))/2)
    a = tuple(map(int,input("X,Y точки А(через пробел): ").split()))
    b = tuple(map(int,input("X,Y точки B(через пробел): ").split()))
    c = tuple(map(int,input("X,Y точки C(через пробел): ").split()))
    print(S(a,b,c))
def task14():
    """Дополнительное задание 14"""
    def to_int(number: str):
        NUMBERS = {"один": 1,"два" : 2,"три": 3
                ,"четыре": 4,"пять":5,"шесть":6
                ,"семь":7,"восемь":8,"девять":9}
        RANGE10_20 = {"одиннадцать":11,"двенадцать":12,"тринадцать":13
                    ,"четырнадцать":14,"пятнадцать":15,"шестнадцать":16
                    ,"семнадцать":17,"восемнадцать":18,"девятнадцать":19}
        DOZENS = {"десять": 10,"двадцать":20, "тридцать":30,"сорок":40,"пятьдесят":50}
        NUMBERLETTERS = (RANGE10_20,NUMBERS,DOZENS)
        result = 0
        isend = False
        for num in number.split():
            for i in range(len(NUMBERLETTERS)):
                if num in NUMBERLETTERS[i].keys():
                    result += NUMBERLETTERS[i][num]
                    if i == 0 or i == 1:
                        isend = True
                        break
            if isend:
                break
        return result
    number = input("Введите число от 0 - 59 словесно: ")
    print(f"Ваше число записанное в цифрах: {to_int(number)}")
#Main
if __name__ == "__main__":
    TASKS = (task1,task2,task3
            ,task4,task5,task6
            ,task7,task8,task9
            ,task10,task11,task12
            ,task13,task14)
    print("Укажите задание, которое хотите запустить.")
    taskNum = int(input(f"Номер задания(1 - {len(TASKS) }): "))
    TASKS[taskNum - 1]()
    input("Нажмите 'Enter', чтобы выйти")
