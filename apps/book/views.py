from django.shortcuts import render
from . import models
from django.http import HttpResponse
from .forms import PostBookForm
# Create your views here.
def book_detail(request, isbn):
    book = models.Book.objects.get(pk=isbn)

    context = {
            "book": book,
            #"tags": ', '.join(str(tag) for tag in book.tags.all()),
            #"authors": ', '.join(str(author) for author in book.authors.all())

        }
    return render(request, 'book_details.html', context)

#def book_post(request):
    #breakpoint()
    #return render ( request, 'post.html')

def book_post(request):
    #breakpoint()
    if request.method == 'GET':
        form = PostBookForm()
        context = {"form": form}
        
        return render(
            request, "book_post.html", context
        )
    

    elif request.method == 'POST':
        data = request.POST
        form = PostBookForm(data)

        if form.is_valid():
            data = form.cleaned_data
            # TODO Save to database
            # TODO Redirect to home page