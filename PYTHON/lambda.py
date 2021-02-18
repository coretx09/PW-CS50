people = [
    {'name': 'Sauvet', 'genre': 'masculin', 'age':60, 'language': 'french'},
    {'name': 'Galina', 'genre': 'feminin', 'age': 15, 'language': 'russian'}
]

people.sort(key=lambda i: i['name'])
print(people)