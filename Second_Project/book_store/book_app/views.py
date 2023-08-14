from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models
from . import forms

# Create your views here.
class MyTemplateView(TemplateView):
    template_name = './index.html'
    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        context = {'name': 'habibor Rahaman', 'age': 23}
        context.update(kwargs)
        return context
    
class StoreBook(FormView):
    template_name = './storeBook.html'
    form_class = forms.BookStoreForm
    success_url = reverse_lazy('showbooks')

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


class ShowBooks(ListView):
    template_name = './showbooks.html'
    model = models.BookStroeModel
    context_object_name = 'books'
        

class BookUpdate(UpdateView):
    form_class = forms.BookStoreForm
    template_name = './storeBook.html'
    model = models.BookStroeModel
    success_url = reverse_lazy('showbooks')

class DeleteBook(DeleteView):
    model = models.BookStroeModel
    template_name = './confirm.html'
    success_url = reverse_lazy('showbooks')
    
