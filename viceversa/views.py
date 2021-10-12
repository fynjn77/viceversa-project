from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse('soooooo')
    return render(request, 'home.html')


def reverse(request):
    # return HttpResponse('soooooo')
    user_text = request.GET['usertext']
    user_text = user_text[::-1]
    return render(request, 'reverse.html',{'usertext':user_text})