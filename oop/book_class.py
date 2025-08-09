from enum import auto


class Book:
    def __init__(self, title(str), author(str), year(int)):
        self.title = title
        self.author = author # type: ignore
        self.year = year # type: ignore
        print("(title) by (author), published in (year)")
    
    def __del__(self):
        self.file.close()
        
    def __str__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    

