from django.db import models

# Create your models here.

class BookStroeModel(models.Model):
    CATEGORY = (
        ('Programming', 'Programming'),
        ('History', 'History'),
        ('Database', 'Database'),
        ('Operatng System','Operatng System'),
        ('Mystrey', 'Mystrey')
    )
    id = models.IntegerField(primary_key=True, auto_created=True)
    book_name = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    author_email = models.CharField(max_length=40)
    category = models.CharField(max_length=50, choices=CATEGORY)
    first_publication = models.DateTimeField(auto_now_add=True)
    last_publication = models.DateTimeField(auto_now=True)
    publish_country = models.CharField(max_length=30)
    
    def __str__(self):
        return f'Id: {self.id} - {self.book_name}'