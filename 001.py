from django.shortcuts import render

def hello_word(request):
    print(request.path)
    return render(request,'home.html')