class Book:
    def __init__(self, title, author, is_borrowed = False):
        self.title = title
        self.author = author
        self._is_borrowed = is_borrowed
        self.log = []

    @property
    def is_borrowed(self):
        return self._is_borrowed

    def describe(self):
        return f"{self.title} - {self.author}"

    def borrow(self):
        if self._is_borrowed:
            return False
        self._is_borrowed = True
        self.log.append("borrow")
        return True

    def return_book(self):
        if self._is_borrowed:
            self._is_borrowed = False
            self.log.append("return")
            return True
        return False


a = Book("Python cơ bản", "Linh")
b = Book("Git thực hành", "Hà")

#test describe

print(f"{a.describe()} \n{b.describe()}")

#test trang thai
print(a.borrow())
print(a.borrow())
print(b.is_borrowed)
print(a.return_book())
print(a.is_borrowed)
print(a.return_book())
print(a.log)