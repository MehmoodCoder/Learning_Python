import operator
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html',{"key":"I am from Python"})

def downloads(request):
    return HttpResponse('<font face = "sans-serif" color = "navy" size = "7px"><center><h4> No Downloads Available !</h4></center></font>')

def result(request):
    
    # name = request.GET['name']
    message = request.GET['message']

    word = message.split()
    word_count = len(word)
    dict_words = {}

    for i in word:
        if i in dict_words:
            dict_words[i] += 1
        else:
            dict_words[i] = 1

    sorted_dict = sorted(dict_words.items(), key=operator.itemgetter(1), reverse=True)
    
    return render(request, 'result.html', {"message": message, "word_count": word_count, "dict_words": sorted_dict})




