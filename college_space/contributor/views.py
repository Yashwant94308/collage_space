from django.shortcuts import render, redirect
from .models import Routines, Books
from .forms import DocumentForm, BookDocumentForm
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.

def index(request):

    return render(request, 'contributor/index.html')


def contact(request):

    return render(request, 'contributor/contact.html')


def routines(request):
    documents = Routines.objects.order_by('-routine_uploaded_at')
    context = {'documents': documents}
    return render(request, 'contributor/routines.html', context=context)


# @user_passes_test(lambda u: u.is_superuser)
@login_required
def routines_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/routines')
    else:
        form = DocumentForm()
    context = {'form': form}
    return render(request, 'contributor/routine_upload.html', context=context)


def books(request):
    book_document = Books.objects.order_by('-books_uploaded_at')
    context = {'book_document': book_document}
    return render(request, 'contributor/books.html', context=context)


@login_required
def books_upload(request):
    if request.method == 'POST':
        form = BookDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/books')
    else:
        form = BookDocumentForm()
    context = {'form': form}
    return render(request, 'contributor/books_upload.html', context=context)
