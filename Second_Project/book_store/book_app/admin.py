from django.contrib import admin
from . import models

# Register your models here.
class BooksStoreModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_name', 'author', 'author_email', 'category', 'publish_country', 'first_publication', 'last_publication']
    
admin.site.register(models.BookStroeModel, BooksStoreModelAdmin)