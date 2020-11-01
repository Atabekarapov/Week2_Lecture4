# Dictionary (Dic)     (izmenyayemiy tip dannyh, hranit sebe spisok i slojnye struktury dannyh) (Hash --> sortirovka)
# did = {key(adress): value...}          (ispolzuem otobrajeniye dly peredachi dannyh)
# 1)
# student = {'name': 'Atabek', 'surname': 'Arapov', 'age': 17}
# studenty = {}
# print(type(studenty))
# student = dict((('winter', 1), ('spring', 2), ('fall', 3)))
# print(type(student))
# print(len(student))


# 2)
# student = {'name': 'Atabek', 'surname': 'Arapov', 'age': 17}
# student
# print(student['name'])
# del student['name']
# print(student)




# 3)
# student = {
#     'name': 'Atabek', 
#     'surname': 'Arapov', 
#     'age': 17,
#     'languages':['english', 'russian', 'kyrgyz'],
#     'smokes': False,
#     'other_dict': {1:'one', 2:'two'},
#     True: 'True giiii',
#     None: 'None giiii',
#     (1, 2, 3): 'Eto tuple',
#     'name': 'Moi name',
#     }
# print(student['other_dict'][2])
# print(student[None])
# print(['name'])

# 4)
# my_tuple =[('one', 1), ('two', 2), ('three', 3)]
# dict_ = dict(one = 1, two = 2, three = 3)
# dict_ = dict(my_tuple)
# print(dict_)
                                            #   ZIP -----> dva spisko vzyal i soedinyayet po indexu
# 5)
# days = [1, 2, 3]
# days_name = ['mon', 'thues', 'wed']
# dist_days = dict(zip(days, days_name))
# one_more = [5, 6, 7]
# print(days, dist_days, one_more)

# 6)
# dict_ = dict(one=1, two=2, three=3)
# num = int(1,2,3)                           ()
# spisok = tuple()

# 7)
student = {
    'name': 'Atabek', 
    'surname': 'Arapov', 
    'age': 17,
    'languages':['english', 'russian', 'kyrgyz'],
    'smokes': False,
    'other_dict': {1:'one', 2:'two'},
    True: 'True giiii',
    None: 'None giiii',
    (1, 2, 3): 'Eto tuple',
    }
# 8) 
#  student.clear() 
#         
# 9)
#  new_student = student.copy()

# 10) 
# (student.items())                # (sdelal iz elementov spisok )
# for item in student.keys():        # (zdelaet ekrankirovanie)
#     print(item)

# 11)
# new_item = student.pop('name')             item ---->klyuch znacheniye
# print(new_item)
# print(student)

# 12)
# new_item = student.popitem()              LIFO ---> first in last out (Udalyayet poslednim)
# print(new_item)

# 13)     setdefault ---------> po umalchaniyu NONE dobavlyayet v konse 
# student.setdefault(10, 'DEFAULT')
# print(student)

# 14)     UPDATE ----> obnavlyayet slovar s pomoshyu slovaram i dobavlyayet
# student.update([('key1',5), ('2', 8)])
# print(student)

# 15)     VALUES ------> 


# 16)       FROMKEYS ----->  Po umalchaniyu NONE, 
student = dict.fromkeys([1, 2, 3], 'Makers')
print(student)



































