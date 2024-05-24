# Для измерения скорости работы
import time


# Первая реализация заключается в заполнении списка данными, а затем выводом последних данных.
# Плюсы: 1) Есть возможность динамически расширить буфер с восстановлением старых данных
# Минусы: 1) Периодически потребуется чистить буфер, чтобы избежать переполнения.
#         2) Скорость выполнения несколько ниже, в сравнении со 2 классом.
class Circular_buffer_exp0:
    # Инициализируем класс
    def __init__(self, size):
        # Ограничение ввода
        if size >= 1:
            self.size = size
        else:
            raise ValueError('Размер буфера не может быть меньше 1')
        # Сам буфер в виде списка
        self.buffer_date = []
        print(f'Буфер из {size} элементов создан')
        # Вводимый элемент
        self.num_current_index = 0

    def add(self, meaning):
        self.buffer_date.append(meaning)
        self.print_buffer()

    def print_buffer(self, ind=-1):
        buf_out = self.buffer_date[-self.size:]
        if ind == -1:
            print(buf_out)
        else:
            if len(buf_out) > ind:
                print(buf_out[ind])
            else:
                print(buf_out)

    def status_buffer(self):
        print(
            f'Буфер заполнен на {len(self.buffer_date[-self.size:]) / self.size * 100}%: {len(self.buffer_date[-self.size:])} из {self.size}')
        # Размер

    def clear_buffer(self):
        self.buffer_date.clear()
        print('Буфер очищен')
        self.print_buffer()


# Вторая реализация отличается от первой тем, что мы переключаем индексы статического списка.
# Плюсы:
# Минусы:
class Circular_buffer_exp1:
    # Инициализируем класс
    def __init__(self, size):
        # Ограничение ввода
        if size >= 1:
            self.size = size
        else:
            raise ValueError('Размер буфера не может быть меньше 1')
        # Сам буфер в виде списка
        self.buffer_date = []
        print(f'Буфер из {size} элементов создан')
        # Вводимый элемент
        self.num_current_index = 0

    def num_element(self):
        if self.num_current_index + 1 == self.size:
            self.num_current_index = 0
        else:
            self.num_current_index += 1

    def print_buffer(self, ind=-1):
        if ind == -1:
            print(self.buffer_date)
        else:
            if len(self.buffer_date) > ind:
                print(self.buffer_date[ind])
            else:
                print(self.buffer_date)

    def add(self, meaning):
        # Добавляем в список с индексом num_last_index
        # Если размер буфера равен вводимому индексу, тогда увеличиваем буфер, если длина буфера не равна
        if len(self.buffer_date) == self.num_current_index and len(self.buffer_date) != self.size:
            self.buffer_date.append(meaning)
        else:
            self.buffer_date[self.num_current_index] = meaning
        self.num_element()
        self.print_buffer()

    def status_buffer(self):
        print(f'Буфер заполнен на {len(self.buffer_date) / self.size * 100}%: {len(self.buffer_date)} из {self.size}')
        # Размер

    def clear_buffer(self):
        self.buffer_date.clear()
        print('Буфер очищен')
        self.print_buffer()


if __name__ == '__main__':
    # Работа 1 класса:
    # начальное время
    start_time = time.time()

    # Создаем объект буфера из 10 элементов.
    cf = Circular_buffer_exp0(10)

    # Выводим состояние буфера
    cf.status_buffer()

    # Заполняем элементами
    cf.add(2)
    cf.add(5)
    cf.add(1)
    cf.add(2)
    cf.add(3)
    cf.add(4)
    # Выводим состояние буфера
    cf.status_buffer()
    cf.add(2)
    cf.add(5)
    cf.add(1)
    cf.add(2)
    cf.add(3)
    # Выводим состояние буфера
    cf.status_buffer()
    cf.add(4)

    # Чистим буфер
    cf.clear_buffer()

    # Выводим состояние буфера
    cf.status_buffer()

    # конечное время
    end_time = time.time()
    print(f'Время выполнения 1 класса:{end_time - start_time}', '\n')


    # Работа 2 класса:
    # начальное время
    start_time = time.time()

    cf1 = Circular_buffer_exp0(10)

    # Выводим состояние буфера
    cf1.status_buffer()

    # Заполняем элементами
    cf1.add(2)
    cf1.add(5)
    cf1.add(1)
    cf1.add(2)
    cf1.add(3)
    cf1.add(4)
    # Выводим состояние буфера
    cf1.status_buffer()
    cf1.add(2)
    cf1.add(5)
    cf1.add(1)
    cf1.add(2)
    cf1.add(3)
    # Выводим состояние буфера
    cf1.status_buffer()
    cf1.add(4)

    # Чистим буфер
    cf1.clear_buffer()
    # Выводим состояние буфера
    cf1.status_buffer()
    # конечное время
    end_time = time.time()
    print(f'Время выполнения 2 класса:{end_time - start_time}')
