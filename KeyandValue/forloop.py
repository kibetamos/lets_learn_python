# from multiprocessing.sharedctypes import Value
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

for value,key in person.items():
    print({value:key})
