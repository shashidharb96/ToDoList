from django.shortcuts import render
from .models import table_ToDo
from django.views.generic import ListView , DetailView , DeleteView , UpdateView , CreateView
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import table_ToDo
from .serializers import table_ToDoSerializer
from rest_framework import status
from rest_framework.views import APIView


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



class API_LIST(APIView):
    def get(self, request):
        lists=table_ToDo.objects.all()
        serializer=table_ToDoSerializer(lists, many=True)
        return Response(serializer.data)


    def post(self):
        pass


