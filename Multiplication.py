import bin2 as binary
import os

class Multiplication(object):
    def __init__(self, value1, value2):
        print("value1 = {}, value2 = {}".format(value1, value2))
        self._A = binary.Word(value1)
        self._B = binary.Word(value2)
        self._size = self._A.size
        self._result = binary.Word(0, self._size*2-1)
        self.calculate()


    def __str__(self):
        self.show_calculate(self)


     def result(self):
        return self._result


class Booth(Multiplication):
    def calculate(self):
        print("YOLO")
        pass


    def show_calculate(self):
        print("В умножении по алгоритму Бутта сомножители должны быть представлены в дополнительном коде.")
        pass


class Mult1(Multiplication):
    def calculate(self):
        pass


    def show_calculate(self):
        pass


class Mult2(Multiplication):
    def calculate(self):
        pass


    def show_calculate(self):
        pass


class Mult2(Multiplication):
    def calculate(self):
        pass


    def show_calculate(self):
        pass


class Mult2(Multiplication):
    def calculate(self):
        pass


    def show_calculate(self):
        pass

def Main():
    print("Умножение методом Бута\n")
    a = input("Введите первый операнд\n>>>")
    b = input("Введите второй операнд\n>>>")
    s1 = Booth(a, b)

    del(s1)
    os.system("pause")
    print("Умножение первым методом")

    s2 = Mult1(a, b)
    os.system("pause")

    print("Умножение вторым методом")


    pass


if __name__ == '__main__':
    os.system("title Multiplication")
    os.system("color 07")
    Main()
    os.system("pause")
    os.system("cls")