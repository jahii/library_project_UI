from django.http.response import HttpResponse
from django.shortcuts import render
from common.models import BookList
from django.contrib import messages

# Create your views here.
def searchbook(request):
    booklist = BookList.objects.all().order_by('title')

    search_key = request.GET.get('search_key')
    if search_key:
        booklist = booklist.filter(title__icontains=search_key)

    return render(request, 'visitor/search_screen.html',{'booklist':booklist})


def drawmap(request, id):
    searched_book = BookList.objects.get(id=id)

    
    return render(request, 'common/draw_map.html', {'searched_book':searched_book})