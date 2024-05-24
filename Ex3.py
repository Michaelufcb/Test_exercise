def forming(q):
    final = []
    final.extend(main(q))
    return final


def main(date_list):
    # Если элемент один, тогда возвращаем список
    if len(date_list) <= 1:
        return date_list

    # Получаем значение среднего элемента
    z = date_list[len(date_list) // 2]
    a = []
    b = []
    c = []
    for p in date_list:
        if p < z:
            a.append(p)
        elif p == z:
            b.append(p)
        else:
            c.append(p)

    return forming(main(a)) + b + forming(main(c))


if __name__ == "__main__":
    # Массив
    massiv_date = [53, 22, 88, 15, 9, 37, 7, 64, 64, 450]
    # Вывод результата функции
    print(main(massiv_date))
