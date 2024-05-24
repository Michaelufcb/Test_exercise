import time

# начальное время
start_time = time.time()

def isEven_lite(value):
    return not (value % 2 == 1)

# конечное время
end_time = time.time()

start_time_ = time.time()

def isEven(value):
    return (value ^ 1) > value

end_time_ = time.time()

if __name__ == '__main__':
    # Это было бы слишком просто :D
    print(isEven_lite(-2))
    print(f'Время выполнения:{end_time - start_time}')
    # Плюсы: интуитивно понятный код.
    # Минусы: -

    # Это уже поинтереснее. Использование исключающего или
    print(isEven(10))
    print(f'Время выполнения:{end_time - start_time}')
    # Плюсы: По времени абсолютно одинаковые, работают индентично
    # Минусы: без комментария не понятно, что за функция
