from django.shortcuts import render

def my_view(request):
    return render(request, 'counseling/index.html')