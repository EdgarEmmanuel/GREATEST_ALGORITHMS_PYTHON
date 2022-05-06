from collections import namedtuple

Book = namedtuple("Book", "author title genre")

books = [
        Book("Pratchett", "Nightwatch", "fantasy"),
        Book("chett", "Thief Of Time", "fantasy"),
        Book("Le Guin", "The Dispossessed", "scifi"),
        Book("Alfred", "A Wizard Of Earthsea", "fantasy")
]
dict = {book.author:book.title for book in books}
print(dict)