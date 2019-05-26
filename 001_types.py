"""
a = 2
b = 0.5
print(a + b)

name = input ("введите ваше имя")
print ("Привет, {}".format (name))

name = input ("Введите ваше имя")
print(f"Привет, {name}, как дела?")


v = input("Введите число от 1 до 10")
v = int(v)
print(10 + v)

a = 2
b = 3
c = b = a
print(c)


print(float("1"))
a = "2.5"
b = float(a)
print(int(b))
print(bool(1))
print(bool(""))
print(bool(0))


#СПИСКИ
a = [3, 5, 7, 9]
print(a)
a.append("Python")
print(len(a))
print(a[0])
print(a[-1])
print(a[2:5])
a.remove("Python")
print(a)
"""


#СЛОВАРИ ДОделать!!!!
dict = {
    "city" : "Москва",
    "temperature" : "20"
}
print(dict["city"])
dict["temperature"] = "5"
print(dict)
print (dict.get("country"))
dict ["country"] = "Россия"

