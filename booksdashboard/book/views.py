from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category 
from .forms import BookForm , CategoryForm
from django.views.generic import ListView, DeleteView, UpdateView, TemplateView
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'pages/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookForm()
        context['formcategory'] = CategoryForm()
        context['books'] = Book.objects.all()
        context['categories'] = Category.objects.all()
        context['all_books'] = Book.objects.filter(active=True).count()
        context['books_sold'] = Book.objects.filter(status='sold').count()
        context['books_rented'] = Book.objects.filter(status='rented').count()
        context['books_available'] = Book.objects.filter(status='available').count()
        return context
    


    def post(self,request,*args,**kwargs):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        formcategory = CategoryForm(request.POST)
        if formcategory.is_valid():
            formcategory.save()
        return redirect('index')





class BookList(ListView):
    model = Book
    template_name = 'pages/books.html'
    queryset = Book.objects.all()
    context_object_name = 'books'


class BookUpdate(UpdateView):
    model = Book
    template_name = 'pages/update.html'
    success_url = reverse_lazy('index')
    fields = '__all__'



class BookDelete(DeleteView):
    model = Book
    template_name ='pages/delete.html'
    # context_object_name = 'book'
    success_url = reverse_lazy('index')












    # def delete(request, id):
#     book_delete = get_object_or_404(Book, id=id)
#     if request.method == 'POST':
#         book_delete.delete()
#         return redirect('index')
#     return render(request, 'pages/delete.html', {'book': book_delete})





# def update(request, id):
#     book_instance = get_object_or_404(Book, id=id)
    
#     if request.method == 'POST':
#         book_save = BookForm(request.POST, request.FILES, instance=book_instance)
#         if book_save.is_valid():
#             book_save.save()
#             return redirect('/')
#     else:
#         book_save = BookForm(instance=book_instance)

#     form = book_save 

#     return render(request, 'pages/update.html', {'form': form})




# def books(request):
#     books = Book.objects.all()
#     categories = Category.objects.all()
#     return render(request, 'pages/books.html', {'books': books, 'categories': categories})



# class IndexView(TemplateView):
#     template_name = 'pages/index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = BookForm()
#         context['formcategory'] = CategoryForm()
#         context['books'] = Book.objects.all()
#         context['categories'] = Category.objects.all()
#         context['allbooks'] = Book.objects.filter(active=True).count()
#         context['booksold'] = Book.objects.filter(status='sold').count()
#         context['bookrental'] = Book.objects.filter(status='rented').count()
#         context['bookavailable'] = Book.objects.filter(status='available').count()
#         return context

#     def post(self, request, *args, **kwargs):
#         form = BookForm(request.POST, request.FILES)
#         formcategory = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#         if formcategory.is_valid():
#             formcategory.save()
#         return redirect('index')












# def index(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST, request.FILES)
#         if form.is_valid(): 
#             form.save()
#         formcategory = CategoryForm(request.POST)
#         if formcategory.is_valid():
#             formcategory.save()
    
#     books = Book.objects.all()
#     categories = Category.objects.all()
#     all_books = Book.objects.filter(active = True).count()
#     booksold = Book.objects.filter(status='sold').count()
#     bookrental = Book.objects.filter(status='rented').count()
#     bookavaliable = Book.objects.filter(status='avaliable').count()


#     form = BookForm()
#     formcategory = CategoryForm
    

    
#     return render(request, 'pages/index.html', 
#                   {'books': books, 'categories': categories,
#                     'form': form, 'formcategory':formcategory,
#                     'allbooks':all_books,'booksold':booksold,
#                     'bookrental':bookrental,'bookavaliable':bookavaliable})



# class IndexView(ListView):
#     template_name = 'pages/index.html'
#     model = Book
#     queryset = Book.objects.all()
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = BookForm()
#         context['formcategory'] = CategoryForm()
#         context['books'] = Book.objects.all()
#         context['categories'] = Category.objects.all()
#         context['all_books'] = Book.objects.filter(active=True).count()
#         context['books_sold'] = Book.objects.filter(status='sold').count()
#         context['books_rented'] = Book.objects.filter(status='rented').count()
#         context['books_available'] = Book.objects.filter(status='available').count()
#         return context