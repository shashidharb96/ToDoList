
from django.urls import path
from . import views

urlpatterns = [

    path('home/', views.ToDoListView.as_view(), name='home'),
    path('home/<int:pk>/', views.ToDoDetailView.as_view(), name = 'post-detail'),
    path('home/new/', views.ToDoCreateView.as_view(), name = 'post-create'),
    path('home/<int:pk>/update/', views.ToDoUpdateView.as_view(), name = 'post-update'),
    path('home/<int:pk>/delete/', views.ToDoDeleteView.as_view(), name = 'post-delete'),
    ]