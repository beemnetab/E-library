from django.db import models

class Company(models.Model):
    name = models.TextField()
    logo = models.ImageField(upload_to='static/image/')

    def __str__(self):
        return f"{self.name}"
    

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    summary = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book = models.FileField(upload_to='static/pdfs/')
    adder = models.IntegerField()
    category = models.TextField()
    pages = models.IntegerField()
    
    def __str__(self):
        return f"{self.title}"
    