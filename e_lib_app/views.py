from django.shortcuts import redirect, render
from .forms import BooksForm
from . import models
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def Registers(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		firstName = request.POST['first--name']
		lastName = request.POST['last--name']

		# Check if a user with the same username already exists
		if User.objects.filter(username=email).exists():
			messages.info(request,'User already exists')
			return render(request, 'register.html')
		else:
			# Create a new user
			register = User.objects.create_user(username=email,password=password,first_name=firstName,last_name=lastName)
			# No need to call save() after create_user(), as it's already saved
			return redirect('login')
	else:
		return render(request, 'register.html')
	

def Login(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']

		user = auth.authenticate(username=email, password=password)

		if user is not None:
			auth.login(request, user)
			print('User logged in successfully')
			return redirect('home')
		else:
			messages.info(request,'Invalid Credentials')
			return render(request, 'login.html')
	else:
		return render(request, 'login.html')

def home(request):
	return render(request, 'home.html',{'company': models.Company.objects.get(id=1)})

def explore(request):
	edu_books = models.Book.objects.filter(category='Education')
	fiction_books = models.Book.objects.filter(category='Fiction')
	science_books = models.Book.objects.filter(category='Science')
	return render(request, 'explore.html',{'edu_books':edu_books,'fiction_books':fiction_books,'science_books':science_books})

@login_required
def addBook(request,user_id):
	user = User.objects.get(id=user_id)
	if request.method == 'POST':
		form = BooksForm(request.POST, request.FILES)
		if form.is_valid():
			book = form.save(commit=False)
			# book.author = user.first_name + " " + user.last_name
			book.adder = user.id
			print(book.author)
			book.save()
			print()
			print()
			print(book.author)
			print("Book saved successfully")
			print()
			print()
			return redirect('home')
		else:
			print(form.errors)
	else:
		form = BooksForm()
	return render(request, 'addBook.html', {'form': form})

def contri(request,user_id):
	books = models.Book.objects.filter(adder=user_id)
	return render(request, 'contri.html', {'books': books})


def logout(request):
	auth.logout(request)
	return redirect('home')


def editBook(request,book_id):
	book = models.Book.objects.get(id=book_id)
	if request.method == 'POST':
		form = BooksForm(request.POST, request.FILES,instance=book)
		if form.is_valid():
			form.save()
			print()
			print()
			print("Book updated successfully")
			print()
			print()
			return redirect('home')
		else:
			print(form.errors)
	else:
		form = BooksForm(instance=book)
	return render(request, 'editBook.html', {'form': form,'book':book})

def viewBook(request,book_id):
	book = models.Book.objects.get(id=book_id)
	book.summary = book.summary.replace('\n', '<br/>')
	return render(request, 'viewBook.html', {'book': book})
