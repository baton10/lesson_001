
# FOR

word = 'irresponsible'
for word_test in word:
    print(word_test)



# № 1

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    number +=1
    print(number)


# № 2

line = input('введите строку ')
for letter in line:
    print(letter)

"""

school = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '4b', 'scores': [4, 5, 3, 4, 5]},
    {'school_class': '5a', 'scores': [5, 2, 4, 5, 3]},
    {'school_class': '5b', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '6a', 'scores': [5, 5, 4, 5, 3]},
    {'school_class': '6b', 'scores': [3, 4, 3, 2, 5]}
    ]

a_4 = sum(school[0]['scores'])
b_4 = sum(school[1]['scores'])
a_5 = sum(school[2]['scores'])
b_5 = sum(school[3]['scores'])
a_6 = sum(school[4]['scores'])
b_6 = sum(school[5]['scores'])

print(a_4/len(school[0]['scores'])
#print(b_4/len(school[1]['scores'])
#print(a_5/len(school[2]['scores'])
#print(b_5/len(school[3]['scores'])
#print(a_6/len(school[4]['scores'])
#print(b_6/len(school[5]['scores'])
#print(len(school))
#print(school[0]['scores'])





school = []
a_4 = [4, 5, 2, 3, 5]
b_4 = [3, 5, 2, 3, 4]
a_5 = [5, 2, 3, 2, 4]
b_5 = [3, 5, 4, 4, 4]
a_6 = [3, 4, 2, 5, 5]
b_6 = [4, 5, 4, 3, 3]
school.append(a_4)
school.append(b_4)
school.append(a_5)
school.append(b_5)
school.append(a_6)
school.append(b_6)


school = []
a_4 = {'school_class': '4a', 'scores': [4, 5, 2, 3, 5]}
school.append(a_4)
print(school)
