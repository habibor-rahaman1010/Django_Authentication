from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyTemplateView.as_view(template_name = './index.html'), name='home'),
    path('all/books/', views.ShowBooks.as_view(), name='showbooks'),
    path('store/book/', views.StoreBook.as_view(), name='storebook'),
    path('book/update/<int:pk>', views.BookUpdate.as_view(), name='bookupdate'),
    path('book/delete/<int:pk>', views.DeleteBook.as_view(), name='deletebook'),
]