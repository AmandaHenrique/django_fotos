from django.shortcuts import render
from app.models import Crush

# Create your views here.

def index(request):
    crushs = Crush.objects.all()
    contexto = {
        'crushs' : crushs
    }
    return render(request, 'main.html', contexto)



