from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . import models 
from .forms import PostBookForm

# Create your views here.
def book_detail(request, isbn):
    book = models.Book.objects.get(pk=isbn)

    # Set the max viewed book
    max_viewed_books: int = 5

    # Get the current stored session
    viewed_books: list = request.session.get('viewed_books', [])

    # Create the data to be stored in the session
    viewed_book: list[str] = [book.isbn, book.title]

    # Remove if it exist already
    if viewed_book in viewed_books:
        viewed_books.remove(viewed_book)

    # Insert the viewed book at index 0
    viewed_books.insert(0, viewed_book)

    # Get the limit
    viewed_books = viewed_books[:max_viewed_books]

    # replace in the session
    request.session['viewed_books'] = viewed_books

    context = {
        "book": book,

    }
    return render(request, 'book_detail.html', context)

# def book_post(request):
#     #breakpoint()
#     return render(request, 'post.html')

def book_post(request):
    # Get our form in the two states.
    # - pre-submit
    #    - http method: `GET`
    # - post-submit
    #    -- http method: `POST`

    #breakpoint()
    if request.method == 'GET':
        # pre-submit
        form = PostBookForm()
        context = {"form": form}

        return render(
            request,
            'book_post.html',
            context
        )
    elif request.method == 'POST':
        # post-submit
        data = request.POST
        form = PostBookForm(data)

        # Validation
        if form.is_valid():
            data = form.cleaned_data
            # TODO: Save to database
            book = models.Book(
                isbn=data['isbn'],
                title=data['title'],
                page_count=data['pages'],
                description=data['description'],
                category=data['category'],
                published_date = data['published_year'],
                publisher=data['publisher'],
                lang=data['language'],
                edition=data['edition'],
                book_format=data['book_format']
            )
            # save book first, to avoid `ValueError: Cannot add *: instance is on database "default", value is on database "None"`
            book.save()

            book.tags.set(data['tags'])
            book.save()

            # TODO: Redirect to home page using `app-name: url-name`
            return redirect('myread-urls:home-page')




