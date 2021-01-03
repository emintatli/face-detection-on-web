from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render  
from django.http import HttpResponse  
from todo.functions import handle_uploaded_file  
from todo.forms import StudentForm  
from todo.functions import resimincele
def index(request):
    return render(request,"index.html")
# Create your views here.

def index(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            return handle_uploaded_file(request.FILES['file'])  
             
    else:  
        student = StudentForm()  
        return render(request,"index.html",{'form':student})  
    
# Create your views here.
