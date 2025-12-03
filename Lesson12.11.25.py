'''avengers = 'WE ARE IN THE ENDGAME NOW'
print(avengers.isupper())

eddie = 'we are venom'
print(eddie.islower())

tony = 'I am ironman'
print(tony.upper())

avengers = 'WE ARE IN THE ENDGAME NOW'
print(avengers.lower())'''

'''list_of_meal = ['vegetables', 'chicken', 'cola']
print(list_of_meal)
list_of_meal.pop()
print(list_of_meal)
list_of_meal.append('water')
print(list_of_meal)
print('#' * 30)
for i in range(len(list_of_meal)):
    print(list_of_meal[i])
print('#' * 30)
for item in list_of_meal:
    print(item)
print('#' * 30)

list_of_meal[0] = 'Овощи'
print(list_of_meal)

list_of_meal2 = ('Vegetables', 'chicken', 'water')
list_of_meal2[0] = 'Овощи'
print(list_of_meal2)
print(min(list_of_meal))'''

marks = input('Введите оценки: ')
marks = marks.split()
print(marks)
for i in range(len(marks)):
    marks[i] = int(marks[i])

print(sum(marks) / len(marks))
