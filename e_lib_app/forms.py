from django import forms
from .models import Book, Company

class BooksForm(forms.ModelForm):
	CATEGORY_CHOICES = [
		('Education', 'Education'),
		('Fiction', 'Fiction'),
		('Science', 'Science'),
		# Add more categories or Edit as needed
	]

	category = forms.ChoiceField(choices=CATEGORY_CHOICES)

	class Meta:
		model = Book
		fields = ['title', 'author',  'summary', 'book', 'category', 'pages']

