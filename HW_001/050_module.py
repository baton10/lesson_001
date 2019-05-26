"""
from collections import Counter

phones = ["iPhone Xs", "Samsung Galaxy S10", "Xiaomi Mi8", "iPhone Xs", "iPhone Xs", "Xiaomi Mi8"]
count = Counter(phones)

print(count)

print(count['iPhone Xs'])



from collections import Counter

word = "Программирование"
count = Counter(word.lower())

print(count)

"""



import ephem

mars = ephem.Mars('2000/01/01')
const = ephem.constellation(mars)
print(const)