from django.contrib import admin
from .models import Book

# Register the Book model with the admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these columns
    list_filter = ('publication_year',)                     # Filter by year
    search_fields = ('title', 'author')                     # Add search box
