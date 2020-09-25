from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import Widget

# Create your views here.
def index(request):
    widgets = Widget.objects.all()
    return render(request, 'index.html', {'widgets': widgets})

class WidgetCreate(CreateView):
    model = Widget
    fields = "__all__"


class WidgetDelete(DeleteView):
    model = Widget
    success_url = '/'
