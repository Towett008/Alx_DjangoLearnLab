from django.urls import path
from . import views
<<<<<<< HEAD
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView

=======
from django.contrib.auth.views import LoginView, LogoutView
>>>>>>> 93f3fda (Implement role-based access control with UserProfile, role-specific views, URLs, and templates)

urlpatterns = [
    # Home page
    path('', views.home_view, name='home'),

    # Book and Library views
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication (class-based views required by checker)
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),

    # Role-based views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]
