from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import json
import datetime
from django.conf import settings
from django.views import View
import random
# PATH = 'C:\\Users\\anasn\\PycharmProjects\\HyperNews Portal\\HyperNews Portal\\task\\news.json'
PATH = settings.NEWS_JSON_PATH

class Search(View):
    def get(self, request):
        total = []
        item = request.GET.get('q')
        if not item:
            data = sorted(open_file(), key=lambda x: (x['created'], (x['link'])), reverse=True)
            return render(request, 'news/main1.html', {'data': data})

        else:
            for article in open_file():
                if item in article['title']:
                    total.append(article)
        data = sorted(total, key=lambda x: (x['created'], (x['link'])), reverse=True)
        if len(data) == 0:
            return HttpResponse('Not found')
        return render(request, 'news/main1.html', {'data': data})


class Create(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'news/create.html')
    
    def post(self, request, *args, **kwargs):
        lst = []
        title_new = request.POST.get('title')
        text_new = request.POST.get('text')
        time_new = str(datetime.datetime.today())
        link_new = random.randint(10, 100)
        new_dict = {'created': time_new, 'title': title_new,  'text': text_new, 'link': link_new}
        lst = lst + open_file()
        lst.append(new_dict)
        with open(PATH, 'w') as outfile:
            json.dump(lst, outfile)

        return redirect('/news/')


def redirect_view(request):
        return HttpResponseRedirect("news/")


def open_file():
    with open(PATH, 'r') as jfile:
        return json.load(jfile)


def news(request, link):

    jarr = open_file()
    for article in jarr:
        if article["link"] == int(link):
            data = article

    return render(request, "news/news1.html", {"data": data})
