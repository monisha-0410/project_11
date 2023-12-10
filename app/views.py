from django.shortcuts import render

# Create your views here.
def mike(request):
    return render(request,'mike.html')

def john(request):
    return render(request,'john.html')
