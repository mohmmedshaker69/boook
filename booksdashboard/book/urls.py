from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.IndexView.as_view(), name='index'),
    path('books/',views.BookList.as_view(), name='books'),
    path('update/<int:pk>',views.BookUpdate.as_view(),name='update'),
    path('delete/<int:pk>',views.BookDelete.as_view(),name='delete'),


    
]
