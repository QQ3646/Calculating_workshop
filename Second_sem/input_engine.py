import math
import os
from abc import abstractmethod

# Интерфейс
from typing import Callable


class Expression:
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def eval(self, value_of_unknown: dict):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    def as_float(self) -> float:
        if issubclass(type(self), Const):
            return self.value
        raise TypeError

    def as_float_raw(self):
        try:
            return self.as_float()
        except TypeError:
            return self


# Абстратный класс арифметических операций
class Operation(Expression):
    __name: str
    arguments: list

    def __init__(self, name: str, arguments: list):
        super().__init__()
        self.__name = name
        self.arguments = arguments

    # def __collapce(self, op):
    def __str__(self):
        return f" {self.__name} ".join([str(self.arguments[i]) for i in range(len(self.arguments))])


# Класс неизвестных
class Unknown(Expression):
    __name: str
    __pm: int  # 1 | -1

    def __init__(self, name: str, pm: str):
        super().__init__()
        self.__name = name
        self.__pm = 1 if pm == '+' else -1

    def __str__(self):
        return ("-" if self.__pm == -1 else "") + self.__name

    def eval(self, value_of_unknown: dict):
        if self.__name in value_of_unknown:
            return self.__pm * value_of_unknown[self.__name]
        return self


# Класс тригонометрических функций
# Расчет идет через радианы, используя стандартную функцию из библиотеки math
class Trigonometric(Expression):
    __name: str
    __argument: Expression  # Один аргумент
    func: Callable
    __pm: int  # 1 | -1

    def __init__(self, name: str, argument: Expression, func: Callable, pm: int):
        super().__init__()
        self.__name = name
        self.__argument = argument
        self.func = func
        self.__pm = pm

    def eval(self, value_of_unknown: dict) -> float:
        v = self.__argument.eval(value_of_unknown)
        return self.__pm * self.func(v)

    def __str__(self) -> str:
        return f"{self.__name}({self.__argument})"


# Обертки, которые сложно назвать классами
# Созданы чисто для удобства создания, могут быть выпилены


# Синус
class Sin(Trigonometric):
    def __init__(self, argument, pm: int):
        super().__init__("sin", argument, math.sin, pm)


# Косинус
class Cos(Trigonometric):
    def __init__(self, argument, pm: int):
        super().__init__("cos", argument, math.cos, pm)


# Тангенс
class Tan(Trigonometric):
    def __init__(self, argument, pm: int):
        super().__init__("tg", argument, math.tan, pm)


# Класс констант
class Const(Expression):
    __value = 0

    def __init__(self, value: float):
        super().__init__()
        self.__value = value

    def eval(self, value_of_unknown: dict) -> float:
        return self.__value

    def __str__(self) -> str:
        return str(self.__value)


# Экспонента
class Exponent(Const):
    def __init__(self, sign: float):
        super().__init__(sign * math.e)

    def __str__(self) -> str:
        return "e"


# Пи
class Pi(Const):
    def __init__(self, sign: float):
        super().__init__(sign * math.pi)

    def __str__(self) -> str:
        return "pi"


class Sum(Operation):
    # __name = "+"
    def __init__(self, arguments):
        super().__init__('+', arguments)

    def eval(self, value_of_unknown: dict):
        # print(self.arguments)
        return sum(i.eval(value_of_unknown) for i in self.arguments)
    # Количество элементов неопределено, но >= 2
    # Порядок элементов не важен


class Diff(Operation):
    # __name = "-"
    def __init__(self, arguments):
        super().__init__('-', arguments)

    def eval(self, value_of_unknown: dict):
        return self.arguments[0].eval(value_of_unknown) - sum(i.eval(value_of_unknown) for i in self.arguments[1:])

    # Количество элементов неопределено, но >= 2
    # Порядок элементов важен


class Multi(Operation):
    # __name = "*"
    def __init__(self, arguments):
        super().__init__('*', arguments)

    def eval(self, value_of_unknown: dict):
        res = 1
        for i in self.arguments:
            res *= i.eval(value_of_unknown)
        return res
    # Количество элементов неопределено, но >= 2
    # Порядок элементов не важен


class Div(Operation):
    # __name = "/"
    def __init__(self, arguments):
        super().__init__('/', arguments)

    def eval(self, value_of_unknown: dict):
        res = self.arguments[0].eval(value_of_unknown)
        for i in self.arguments[1:]:
            res /= i.eval(value_of_unknown)
        return res
    # Количество элементов неопределено, но >= 2
    # Порядок элементов важен


class Exp(Operation):
    # __name = "^"
    def __init__(self, arguments):
        super().__init__('^', arguments)

    def eval(self, value_of_unknown: dict):
        return self.arguments[0] ** self.arguments[1]
    # Количество элементов определено, должно равняться двум
    # Порядок элементов важен


class Function:
    __exp: Expression = 0
    __res: int

    def __construct_operation(self, symbol: str, arguments: list):
        match symbol.lower():
            case '+':
                return Sum(arguments)
            case '-':
                return Diff(arguments)
            case '*':
                return Multi(arguments)
            case '/':
                return Div(arguments)
            case "sin" | "-sin":
                return Sin(arguments[0], -1 if symbol[0] == '-' else 1)
            case "cos" | "-cos":
                return Cos(arguments[0], -1 if symbol[0] == '-' else 1)
            case "tg" | "tan" | "-tg" | "-tan":
                return Tan(arguments[0], -1 if symbol[0] == '-' else 1)
        # TODO: add Exp

    def __priority(self, char) -> int:
        if char in "+-":
            return 1
        elif char in "*/":
            return 2
        else:
            return 0

    def __init__(self, raw_function: str):
        raw_function = raw_function.replace(" ", "")
        raw_function.replace('\n', '')
        end_s = []
        op_s = []

        current_ind = 0

        while current_ind < len(raw_function):
            current_ch = raw_function[current_ind]
            match current_ch:
                case '*' | '/':
                    if len(op_s) != 0 and self.__priority(op_s[-1]) >= self.__priority(current_ch):
                        end_s.append(op_s.pop())
                        op_s.append(current_ch)
                    else:
                        op_s.append(current_ch)
                case '(':
                    op_s.append(current_ch)
                case ')':
                    while op_s[-1] != '(':
                        end_s.append(op_s.pop())
                    op_s.pop()
                case '=':
                    if current_ind == 0 or self.__exp == 0:
                        print("Failed to recognize function.")
                        break
                    else:
                        pass
                case '^':
                    end_s.append(current_ch)
                case _:
                    # binary +-
                    if current_ch in "+-" and not (current_ind == 0 or raw_function[current_ind - 1] in "(-+*/"):
                        if len(op_s) != 0 and self.__priority(op_s[-1]) >= self.__priority(current_ch):
                            end_s.append(op_s.pop())
                            op_s.append(current_ch)
                        else:
                            op_s.append(current_ch)
                    # unary +- | digit | alpha
                    elif (current_ch in "+-" and (current_ind == 0 or raw_function[current_ind - 1] in "(-+*/")) or \
                            current_ch.isalnum():
                        if current_ch in "+-":
                            unknown_name = ""
                            sign = current_ch
                        else:
                            unknown_name = current_ch
                            sign = '+'
                        another_counter = 1
                        # TODO: remake with "for"
                        while current_ind + another_counter < len(raw_function) and \
                                (raw_function[current_ind + another_counter].isalnum() or \
                                 raw_function[current_ind + another_counter] == '_'):
                            unknown_name += raw_function[current_ind + another_counter]
                            another_counter += 1
                        if unknown_name[0].isalpha():
                            if unknown_name.lower() in ["sin", "cos", "tan", "tg"]:
                                op_s.append((sign if sign == '-' else '') + unknown_name)
                            elif unknown_name.lower() == "pi":
                                end_s.append(Pi(1 if sign == '+' else -1))
                            elif unknown_name.lower() == "e":
                                end_s.append(Exponent(1 if sign == '+' else -1))
                            end_s.append(Unknown(unknown_name, sign))
                        elif unknown_name[0].isdigit():
                            end_s.append(Const(float(sign + unknown_name)))
                        else:
                            print("Failed to recognize function.")
                            break
                        current_ind += another_counter - 1
            current_ind += 1
        end_s += reversed(op_s)

        finish_queue = []
        l = len(end_s)
        for i in range(l):
            if issubclass(type(end_s[0]), Expression):
                finish_queue.append(end_s.pop(0))
            else:
                t_arg = [finish_queue.pop(), finish_queue.pop()]
                t_arg[0], t_arg[1] = t_arg[1], t_arg[0]
                finish_queue.append(self.__construct_operation(end_s.pop(0), t_arg))
        self.__exp = finish_queue[0]
        # print(str(finish_queue[0]))

    def __parse(self, value_of_unknown: str) -> dict:
        value_of_unknown = value_of_unknown.replace(" ", "")
        raw_values = value_of_unknown.split(";")
        values = dict()
        for r_value in raw_values:
            values[r_value[:r_value.find('-')]] = int(r_value[r_value.find('>') + 1:])
        return values

    def __call__(self, value: float):
        value_of_unknown = {"x": value}
        return self.__exp.eval(value_of_unknown)

    def get_res(self):
        return self.__res

    def calculate(self, value_of_unknown: str):
        values = self.__parse(value_of_unknown)
        return self.__exp.eval(values)


def input_function() -> (Function, float):
    PATH = os.getcwd() + "\\input.txt"
    # function_line = ""
    # error_line = ""
    with open(PATH, "r") as file:
        function_line = file.readline()
        error_line = float(file.readline())
    return Function(function_line), error_line
    # print(PATH)


# c = Function("cos ")
#
# print(c.calculate("x->2"))
