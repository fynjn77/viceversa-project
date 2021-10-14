from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse('soooooo')
    return render(request, 'home.html')


def reverse(request):
    # return HttpResponse('soooooo')
    user_text = request.GET['usertext']
    reverse_text = user_text[::-1]
    counter_words = len(user_text.split())
    return render(request, 'reverse.html',{'reverse_text': reverse_text,
                                           'user_text': user_text,
                                           'counter_words': counter_words})



