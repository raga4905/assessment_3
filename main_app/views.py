from django.shortcuts import render
from .models import Widget

# Create your views here.
def index(request):
    widgets = Widget.objects.all()
    return render(request, 'index.html', {'widgets': widgets})