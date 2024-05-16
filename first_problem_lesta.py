# Медленее всего выполсяются операции деления и вычитания, как раз которые использеут операто "%",
# используя побитовое умножени(конъюнкцию) мы ускоряем выполнение функции.
#
# К плюсам "%" можно отнести работу с десятичной системой счисления, которая проще для восприятия, нежели двоичная.


def _is_even(value: int) -> bool:
    return not (value & 1)


def is_even(num: int) -> None:
    if type(num) is not int:
        print("Неверный тип, ожидается: int")
    elif _is_even(num):
        print("Четное")
    else:
        print("Нечетное")


def main():
    is_even(0)
    is_even(1)
    is_even(11)
    is_even(10)
    is_even('one')



if __name__ == '__main__':
    main()