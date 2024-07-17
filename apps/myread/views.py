# inbuilt-imports
# framework-import
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Count

# custom imports
from . import models 
from apps.reader.models import Reader
from apps.book.models import Book
# from . import utils
# Create your views here.

def Home_page(request):
    # views can return valid formats like html , json, xml, etc
    # how to get distinct in ORM
    # Hint : use .distinct() and .count()
    book_per_cat_cnt = Book.objects.values('category').annotate(cnt=Count('*'))
    engaged_reader_cnt = models.MyRead.objects.distinct('reader_username').count()
    total_reader_cnt = Reader.objects.count()

    
    context = {
    'total_reader_cnt': total_reader_cnt,
    'engaged_reader_cnt': engaged_reader_cnt,
    'book_per_cat_cnt': book_per_cat_cnt
    }

   

    # return a response
    return render(request, 'home_page.html', context)

class HomePage(TemplateView):
    # specify the template to display
    template_name = 'home_page.html'