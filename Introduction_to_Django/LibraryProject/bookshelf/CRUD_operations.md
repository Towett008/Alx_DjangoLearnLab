\# CRUD Operations for Book Model



---



\## 🟢 Create Operation

```python

from bookshelf.models import Book



\# Create a Book instance

book = Book.objects.create(title="1984", author="George Orwell", publication\_year=1949)



\# Display the created book

book



\# Expected Output:

\# <Book: 1984 by George Orwell (1949)>

from bookshelf.models import Book



\# Retrieve all Book instances

books = Book.objects.all()

books



\# Expected Output:

\# <QuerySet \[<Book: 1984 by George Orwell (1949)>]>

from bookshelf.models import Book



\# Get the book with the title "1984"

book = Book.objects.get(title="1984")



\# Update the title

book.title = "Nineteen Eighty-Four"

book.save()



\# Display updated books

Book.objects.all()



\# Expected Output:

\# <QuerySet \[<Book: Nineteen Eighty-Four by George Orwell (1949)>]>

from bookshelf.models import Book



\# Get the book by its updated title

book = Book.objects.get(title="Nineteen Eighty-Four")



\# Delete the book

book.delete()



\# Check all books after deletion

Book.objects.all()



\# Expected Output:

\# (1, {'bookshelf.Book': 1})

\# <QuerySet \[]>



