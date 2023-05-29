from django.shortcuts import render

# Create your views here.

d={'name':'honey','age':1}

def  index1(request):
    return render(request,'index1.html',context=d)
