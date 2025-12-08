

---



\### 🟠 \*\*update.md\*\*

```markdown

\# Update Operation



```python

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



