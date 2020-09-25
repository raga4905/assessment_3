from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Widget

# Create your views here.
def index(request):
    widgets = Widget.objects.all()
    return render(request, 'index.html', {'widgets': widgets})

class WidgetCreate(CreateView):
    model = Widget
    fields = "__all__"

