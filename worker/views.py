from django.shortcuts import render

# Create your views here.

def drawmap(request, id):
    
    return render(request, 'common/draw_map.html', {'searched_book':'searched_book', 'type' : 'worker'} )
    #common에 있는 지도 그리는 template으로 보내는 형태, 근로자가 보내므로 type은 worker인 dictionary 데이터 보냄.
    #적절하게 searched_book 데이터 바꿀 것.