
"""
def cut_cake(parts):
    try:
        return 1/int(parts)
    except ZeroDivisionError:
        return "С ума посходили?"

cake = cut_cake(0)
print(cake)


def cut_cake(parts):
    try:
        return 1/int(parts)
    except (ZeroDivisionError, TypeError, ValueError):
        return "С ума посходили?"

cake = cut_cake([2, 5, 7])
print(cake)

"""

b = {"valid": 1}
print(b['valid'])
b["invalid"]

