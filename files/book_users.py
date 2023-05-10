import csv
import json
from files import CSV_FILE_PATH, JSON_FILE_PATH

lst_users = []
lst_books = []
with open(JSON_FILE_PATH) as f:
    users = json.load(f)
    for q in users:
        users_dict = {}
        users_dict["name"] = f"{q['name']}"
        users_dict["gender"] = f"{q['gender']}"
        users_dict["address"] = f"{q['address']}"
        users_dict["age"] = q['age']
        users_dict['books'] = []
        lst_users.append(users_dict)


with open(CSV_FILE_PATH) as t:
    rd = csv.DictReader(t)
    for row in rd:
        book_dict = {}
        book_dict["title"] = f"{row['Title']}"
        book_dict['author'] = f"{row['Author']}"
        book_dict['pages'] = int(f"{row['Pages']}")
        book_dict['genre'] = f"{row['Genre']}"
        lst_books.append(book_dict)

# calculate how many books to distribute to each user
num_users = len(lst_users)
num_books = len(lst_books)
books_per_user = num_books // num_users
extra_books = num_books % num_users

# distribute books to each user
book_idx = 0
for user in lst_users:
    # distribute the "equal" number of books
    for i in range(books_per_user):
        user['books'].append(lst_books[book_idx])
        book_idx += 1
    # distribute any remaining books
    if extra_books > 0:
        user['books'].append(lst_books[book_idx])
        book_idx += 1
        extra_books -= 1
        print(book_idx, books_per_user)


with open("result.json", "w")as f:  #сохранение результата в файл
    s = json.dumps(lst_users, indent=4)
    f.write(s)
