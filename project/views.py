from django.shortcuts import render

from django.http import HttpResponse      #to launch for http

#pytube for downloading youtube videos
from pytube import YouTube

# Create your views here.

def youtubedownload(request):
    return render(request , 'main.html')

def download(request):
    url=request.GET.get('url')           #to pick from form 
    #print(url)

    #to check which video link we have to download, create object
    obj=YouTube(url)
    resolutions = []
    strm_all =obj.streams.all()

    for i in strm_all:
        resolutions.append(i.resolution)
    resolutions= list(dict.fromkeys(resolutions))
    embed_link = url.replace("watch?v=" , "embed/")
    #print('resolutions:' ,resolutions)
    return render(request , 'download.html' , {'rsl': resolutions , 'embd': embed_link })