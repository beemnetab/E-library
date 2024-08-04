from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('explore', views.explore, name='explore'),
path('sign-up', views.Registers, name='register'),
path('login', views.Login, name='login'),
path('addBook/<int:user_id>', views.addBook, name='addBook'),
path('addBook', views.addBook, name='addBook'),
path('contri/<int:user_id>', views.contri, name='contri'),
path('logout', views.logout, name='logout'),
path('editBook/<int:book_id>', views.editBook, name='editBook'),
path('viewBook/<int:book_id>', views.viewBook, name='viewBook'),
]
