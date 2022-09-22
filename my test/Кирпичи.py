if __name__ == '__main__':
    print('Введите цену 1шт кирпича в грн')
    cost = float(input())
    print('Введите длину кирпича в см')
    d = float(input())
    print('Введите высоту кирпича в см')
    v = float(input())
    print('Введите длину стены в см')
    ds = float(input())
    print('Введите высоту стены в см')
    vs = float(input())
    a = ds / d
    b = vs / v
    c = round(a * b)
    print("Вам нужно", c, "шт кирпичей или ", c / 10000, "палет кирпичей")
    print('Стоимость постройки', cost * c, 'грн')
