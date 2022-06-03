"""
Примитивный калькулятор с применением встроенного фреймворка для построения
пользовательского интерфейса Tkinter
"""

import tkinter as tk
import tkinter.ttk as ttk


class Example(ttk.Frame):
    def __init__(self, parent):
        """
        Конструктов приложения с инициализацией метода построения интерфейса.
        :param parent: ссылка на родительское окно приложения
        """
        ttk.Frame.__init__(self)  # вызов конструктора родительского класса
        self.parent = parent  # сохранение ссылки на основное окно
        self.entry = ttk.Entry(self, font=('serif', 12), justify=tk.RIGHT)  # создание текстового однострочного поля
        self.entry.insert(tk.END, '0')  # базовый ноль на экране
        self.memory = 0  # создание ячейки памяти, в качестве 2-ой ячейки будет entry
        self.clear_screen = True
        self.action = ''  # создание указателя на действие
        self.action_case = {'/': lambda x, y: x / y,  # набор действий
                            '*': lambda x, y: x * y,
                            '+': lambda x, y: x + y,
                            '-': lambda x, y: x - y}
        self.init_ui()  # инициализация метода построения интерфейса

    def init_ui(self):
        """
        Метод построения интерфейса калькулятора.
        """
        self.parent.title('Калькулятор на Tkinter')  # установка имени окна
        ttk.Style().configure('TButton', padding=(0, 5, 0, 5), font=('serif', 12))
        ttk.Style().configure('TEntry', padding=(0, 5, 0, 5))
        # устанавливаем стиль для кнопок включая отступы и шрифт
        self.columnconfigure(0, pad=3)  # конфигурирование столбцов сетки
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)
        self.rowconfigure(0, pad=3)  # конфигурирование строк сетки
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        self.rowconfigure(5, pad=3)
        self.entry.grid(row=0, columnspan=4, sticky=tk.W + tk.E)  # размещение текстового поля в нулевой строке
        # с заполнением на 4 клетки сетки и закреплением к левому и правому краю рамки
        cls = ttk.Button(self, text='Очистить', command=self.clear)  # создание и размещение кнопок калькулятор
        cls.grid(row=1, column=0)
        bck = ttk.Button(self, text='Удалить', command=self.delete)
        bck.grid(row=1, column=1)
        rev = ttk.Button(self, text='+/-', command=self.neg_pos)  # пустая кнопка
        rev.grid(row=1, column=2)
        clo = ttk.Button(self, text='Закрыть', command=quit)
        clo.grid(row=1, column=3)
        sev = ttk.Button(self, text='7', command=self.enter_7)
        sev.grid(row=2, column=0)
        eig = ttk.Button(self, text='8', command=self.enter_8)
        eig.grid(row=2, column=1)
        nin = ttk.Button(self, text='9', command=self.enter_9)
        nin.grid(row=2, column=2)
        div = ttk.Button(self, text='/', command=self.division)
        div.grid(row=2, column=3)
        fou = ttk.Button(self, text='4', command=self.enter_4)
        fou.grid(row=3, column=0)
        fiv = ttk.Button(self, text='5', command=self.enter_5)
        fiv.grid(row=3, column=1)
        six = ttk.Button(self, text='6', command=self.enter_6)
        six.grid(row=3, column=2)
        mul = ttk.Button(self, text='*', command=self.multiplication)
        mul.grid(row=3, column=3)
        one = ttk.Button(self, text='1', command=self.enter_1)
        one.grid(row=4, column=0)
        two = ttk.Button(self, text='2', command=self.enter_2)
        two.grid(row=4, column=1)
        thr = ttk.Button(self, text='3', command=self.enter_3)
        thr.grid(row=4, column=2)
        mns = ttk.Button(self, text='-', command=self.subtraction)
        mns.grid(row=4, column=3)
        zer = ttk.Button(self, text='0', command=self.enter_0)
        zer.grid(row=5, column=0)
        dot = ttk.Button(self, text='.', command=self.enter_dot)
        dot.grid(row=5, column=1)
        equ = ttk.Button(self, text='=', command=self.equally)
        equ.grid(row=5, column=2)
        pls = ttk.Button(self, text='+', command=self.addition)
        pls.grid(row=5, column=3)
        self.pack()

    def enter_1(self):
        """
        Переадресация вызова на метод ввода цифры с передачей ее в виде аргумента.
        """
        self.enter_digit('1')

    def enter_2(self):
        """
        Переадресация вызова на метод ввода цифры с передачей ее в виде аргумента.
        """
        self.enter_digit('2')

    def enter_3(self):
        """
        Переадресация вызова на метод ввода цифры с передачей ее в виде аргумента.
        """
        self.enter_digit('3')

    def enter_4(self):
        """
        Переадресация вызова на метод ввода цифры с передачей ее в виде аргумента.
        """
        self.enter_digit('4')

    def enter_5(self):
        """
        Переадресация вызова на метод ввода цифры с передачей ее в виде аргумента.
        """
        self.enter_digit('5')

    def enter_6(self):
        """
        Переадресация вызова на метод ввода цифры с передачей ее в виде аргумента.
        """
        self.enter_digit('6')

    def enter_7(self):
        """
        Переадресация вызова на метод ввода цифры с передачей ее в виде аргумента.
        """
        self.enter_digit('7')

    def enter_8(self):
        """
        Переадресация вызова на метод ввода цифры с передачей ее в виде аргумента.
        """
        self.enter_digit('8')

    def enter_9(self):
        """
        Переадресация вызова на метод ввода цифры с передачей ее в виде аргумента.
        """
        self.enter_digit('9')

    def enter_0(self):
        """
        Переадресация вызова на метод ввода цифры с передачей ее в виде аргумента.
        """
        self.enter_digit('0')

    def neg_pos(self):
        """
        Метод установки знака числа.
        """
        if self.entry.get() == 'Error' or self.entry.get() == '0' or not self.entry.get():  # блокирование ввода если имеется ошибка
            return
        elif self.entry.get()[0] == '-':
            self.entry.delete(0)
        else:
            self.entry.insert(0, '-')

    def cls(self):
        """
        Метод очистки экрана
        """
        self.entry.delete(0, tk.END)
        self.clear_screen = False

    def enter_dot(self):
        """
        Метод ввода десятичной точки
        """
        if self.clear_screen:
            self.cls()
        if '.' in self.entry.get():
            return
        elif self.entry.get():
            self.entry.insert(tk.END, '.')
        else:
            self.entry.insert(tk.END, '0.')

    def clear(self):
        """
        Метод очистки калькулятора
        """
        self.entry.delete(0, tk.END)  # очистка экрана
        self.entry.insert(tk.END, '0')  # базовый ноль на экране
        self.memory = 0  # очистка памяти
        self.action = ''  # очистка указателя операций

    def delete(self):
        """
        Метод удаления последнего символа на экране
        """
        if self.clear_screen:
            self.cls()
        self.entry.delete(len(self.entry.get()) - 1)  # удаление последнего символа
        if not self.entry.get():
            self.entry.insert(tk.END, '0')

    def division(self):
        """
        Переадресация вызова на метод ввода действия с передачей его в виде аргумента.
        """
        self.actions('/')

    def multiplication(self):
        """
        Переадресация вызова на метод ввода действия с передачей его в виде аргумента.
        """
        self.actions('*')

    def subtraction(self):
        """
        Переадресация вызова на метод ввода действия с передачей его в виде аргумента.
        """
        self.actions('-')

    def addition(self):
        """
        Переадресация вызова на метод ввода действия с передачей его в виде аргумента.
        """
        self.actions('+')

    def equally(self):
        """
        Переадресация вызова на метод ввода действия равно.
        """
        self.actions()

    def enter_digit(self, digit: str):
        """
        Метод ввода цифры
        :param digit: текст
        """
        if self.entry.get() == '0' or self.clear_screen:
            self.cls()
        self.entry.insert(tk.END, digit)

    def actions(self, op: str = ''):
        """
        Метод выполнения действий.
        :param op: текст - знак действия -,+,/,*
        """
        try:
            if self.entry.get() == 'Error' or self.entry.get()[-1] == '.':
                return
            elif self.action:
                self.memory = self.action_case[self.action](self.memory, float(self.entry.get()))
                if self.memory % 1 == 0:
                    self.memory = int(self.memory)
                self.cls()
                self.entry.insert(0, self.memory)
                self.action = op
                self.clear_screen = True
                return
            self.action = op
            self.memory = float(self.entry.get())
            self.clear_screen = True
        except (ZeroDivisionError, ValueError):
            self.cls()
            self.entry.insert(tk.END, 'Error')
            self.action = ''
            self.clear_screen = True


def main():
    """
    Функция запуска основного цикла приложения
    """
    root = tk.Tk()  # создание главного окна приложения
    Example(root)  # создание экземпляра класса приложения
    root.mainloop()  # запуск основного цикла приложения


if __name__ == '__main__':
    main()
