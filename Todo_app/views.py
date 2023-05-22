from django.shortcuts import render
from rest_framework.views import *
from .serializers import *
from rest_framework.response import Response
# Create your views here.

class CreateToDo(APIView):
    
    def post(self,request):
        Window(data = request.data)

        task_obj = Window(data = request.data)
        if task_obj.is_valid():
            task_obj.save()
            all_books = Tasks.objects.all()
            ser_n_obj = Window(all_books,many = True)
            return Response(ser_n_obj.data)
        else:
            return Response(task_obj.errors)

class GetToDo(APIView):
    
    def get(self,request,tid):
        t1 = Tasks.objects.get(id=tid)
        task_obj = Window(t1)
        return Response(task_obj.data)
    
class UpdateToDo(APIView):
    
    def put(self,request,tid):
        t1 = Tasks.objects.get(id=tid)
        task_obj = Window(t1, data = request.data)
        if task_obj.is_valid():
            task_obj.save()
            all_books = Tasks.objects.all()
            task_n_obj = Window(all_books,many = True)
            return Response(task_n_obj.data)  
        else:
            return Response(task_obj.errors)
    
class DeleteToDo(APIView):
    
    def delete(self,request,tid):
        t1 = Tasks.objects.get(id = tid)
        t1.delete()
        all_tasks = Tasks.objects.all()
        task_n_obj = Window(all_tasks,many = True)
        return Response(task_n_obj.data)        
     
class AllToDo(APIView):
    
    def get(self,request):
            all_tasks = Tasks.objects.all()
            task_n_obj = Window(all_tasks,many = True)
            return Response(data = task_n_obj.data)
        