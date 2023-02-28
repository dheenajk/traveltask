from django.http import HttpResponse
from django.shortcuts import render
from. models import place
from. models import face

# Create your views here.
def demo(request):
    # name="Result is Here"
    obj1 = place.objects.all()
    obj2 = face.objects.all()
    return render(request, "index.html", {'result': obj1,'result1':obj2},)
#                   ,{"abc":name})
# def function(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     div=x/y
#     mult=x*y
#     sub=x-y
#     return render(request,'result.html',{'addition':add,'division':div,'multip':mult,'subtract':sub})