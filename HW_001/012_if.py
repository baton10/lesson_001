# № 2
def two_lines():
    line_01 = input('Введите первую строку ')
    line_02 = input('Введите вторую строку ')
    lines = line_01 + line_02
    if isinstance(lines, (int, float)):
        return (0)
    elif line_01 == line_02:
        return (1)
    elif line_01 != line_02:
        if line_01 > line_02:
            return (2)
        elif line_01 or line_02 == 'learn':
            return (3)

b = two_lines()
print(two_lines())
print(b)