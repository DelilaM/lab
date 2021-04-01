from django.urls import path
from books import views

urlpatterns = [
    path('books/', views.books_list),
    path('books/<int:pk>/', views.books_detail),
]