from django.http.response import HttpResponse
from django.shortcuts import render
from common.models import BookList
from django.contrib import messages

# Create your views here.
def searchbook(request):
    booklist = BookList.objects.all()

    search_key = request.GET.get('search_key')
    if search_key:
        booklist = booklist.filter(title__icontains=search_key)

    return render(request, 'visitor/search_screen.html',{'booklist':booklist})


# def searchedbooklist(request):
#     all_book_list = BookList.objects.all()
#     search_key = request.GET.get('search_key')
#     if search_key :
#         booklist = all_book_list.filter(title__icontains=search_key)

#         return render(request, 'visitor/searched_booklist.html', {'booklist':booklist})

def startornot(reqeust):
    
    return render(request, 'visitor/start_or_not.html',{'book':book})