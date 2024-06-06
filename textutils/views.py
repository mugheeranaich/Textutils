from django.http import  HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analize(request):

    djtext= request.GET.get('text','default')
    removepunc= request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremove = request.GET.get('newlineremove','off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analized = ""

        for char in djtext:
            if char not in punctuations:
                analized = analized + char

        params = {'purpose': 'Removed New Line', 'analize_text': analized}
        djtext= analized


    if fullcaps == 'on':
       analized = ""

       for char in djtext:
           analized = analized + char.upper()

       params = {'purpose': 'Removed New Line', 'analize_text': analized}
       djtext= analized

    if newlineremove == 'on':
        analized = ""

        for char in djtext:
            if char != '\n' and char != '\r':
                analized = analized + char

        params = {'purpose': '', 'analize_text': analized}
        djtext= analized

    if newlineremove !='on' and removepunc != 'on' and fullcaps != 'on':
        return HttpResponse("Nothing is selected try again")

    return render(request, 'analize.html', params)