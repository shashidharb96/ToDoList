from django.shortcuts import render
from .models import table_ToDo
from django.views.generic import ListView , DetailView , DeleteView , UpdateView , CreateView



def Home(request):
    context = {
        'posts' : table_ToDo.objects.all()
    }
    return render(request,'list/home.html',context , {'title':'Home'})

class ToDoListView(ListView): 
    model= table_ToDo
    template_name='list/home.html'
    context_object_name='posts'

class ToDoDetailView(DetailView):
    model=table_ToDo

class ToDoCreateView(CreateView):
    model=table_ToDo
    fields=['title','data']
    success_url='/list/home/'
 
class ToDoUpdateView(UpdateView):
    model=table_ToDo
    fields=['title','data']
    success_url='/list/home/'

class ToDoDeleteView(DeleteView):
    model=table_ToDo
    success_url='/list/home/'