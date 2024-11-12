#Работа со словарями
my_dict = {'Илья': 1993, 'Мария': 2020, 'Антон': 1966}
print('Словарь:', my_dict)
print('Год рождения Саманты:', my_dict.get('Саманты'))
my_dict.update({'Сара': 1991,
                'Витя': 1876})
print(my_dict)
removed_year = my_dict.pop('Сара')
print(f'Удаленное значение: {removed_year}')
print('Измененный словарь:', my_dict)
print() #отступ
#Работа с множествами
my_set = {1, 4, 2, 3, 1, True, False, True, 'list', 'hello','list' }
print('Множество:', my_set)
my_set.add('Мир')
my_set.add(66)
my_set.discard(2)
print(my_set)