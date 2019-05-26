"""
# IF

# № 1.1

age = input('age')
age = int (age)
if age >= 18:
    print('welcome to the event')

else:
    print('other events will suit you')


age = input ('Сколько вам лет?')
if 3 > age > 6:
    print('тебе в садик пора')
elif 6 > age < 17:
    print('школота')
elif 17 < age < 23:
    print('к парам готов?')
elif age > 23:
    print('заводы стоят - дуй на рабтоту')


# № 1.2

def vozrast():
    age = input("Сколько вам лет? ")
 # ввод исключения для текста
    age = int(age)
    if 1 <= age <= 6 :
      return("В сад!")
    elif 7 <= age <= 16 :
      return("Школота")
    elif 17 <= age <= 25 :
      print("Встану рано утром, выпью кружку ртути и пойду повешусь в этом институте")
    elif age >= 26 :
      return("Заводы стоят - дуй на работу")
    elif age < 1 :
      return("попробуй еще раз")


print(vozrast())



# № 1.3

def vozrast():
    age = input("Сколько вам лет? ")
 # ввод исключения для текста
    age = int(age)
    if 1 <= age <= 6 :
      return ("отправиться в детский сад")
    elif 7 <= age <= 16 :
      return ("пойти в школу")
    elif 17 <= age <= 25 :
      return ("идти на пары")
    elif age >= 26 :
      return ("идти на работу")
    elif age < 1 :
      return ("попробывать еще раз ввести свой возраст")
a = vozrast()
print(f'Привет! Тебе самое время {a}')



















