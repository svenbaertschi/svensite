from django.shortcuts import render

def index(request):
    return render(request, 'temptext.html', {'message':'<h1>nothing here yet</p>'})
