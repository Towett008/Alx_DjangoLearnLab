

---



\### 🔴 \*\*delete.md\*\*

```markdown

\# Delete Operation



```python

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



