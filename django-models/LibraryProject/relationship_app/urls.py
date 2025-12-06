from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    # class-based authentication views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'),name=='login')
    path('logout/',  LogoutView.as_view(template_name='relationship_app/logout.html'),name=='logout')

    # Function based view
    path('register/', views.register_view, name='register'),
]
