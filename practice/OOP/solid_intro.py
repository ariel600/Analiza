class Book:
    book_list = []
    def __init__(self, title: str, author: str, content: str):
        self.title = title
        self.author = author
        self.content = content
    
    def __str__(self):
        return f""" title: {self.title} \n author: {self.author} \n content: {self.content}"""

class Save_to_list:
    def __init__(self):
        self.books_list = []

    def save_to_list(self, book: Book):
        self.books_list.append(book)
    
    def print_list(self):
        for book in self.books_list:
            print(book)
