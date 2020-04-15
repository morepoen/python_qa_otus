from csv import DictReader
import json


with open("users.json", "r") as f:
    users = json.loads(f.read())

new_users = []

for user in users:
    new_user = {"name": user['name'],
                "gender": user['gender'],
                "address": user['address'],
                "books": []}
    new_users.append(new_user)

with open('books.csv', newline='') as f:
    reader = DictReader(f)
    for user, book in zip(new_users, reader):
        if book and user:
            new_book = {"title": book['Title'],
                        "author": book['Author'],
                        "height": book['Height']}
            user['books'].append(book)

with open('users_books.json', 'w') as f:
    json.dump(new_users, f, indent=4)