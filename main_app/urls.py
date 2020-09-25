from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addwidget/', views.WidgetCreate.as_view(), name="add_widget"),
    path('delete_widget/<int:pk>/delete/', views.WidgetDelete.as_view(), name='delete_widget'), 
]
