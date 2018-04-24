from django.shortcuts import render, redirect, get_object_or_404
from . forms import CreateCoinForm, CreateUrlForm
from . models import CoinRedirectModel, BasicUrlModel

from random import randint

ALLOWED = 'abcdefghijklmnopqrstuvwxyz'
ALLOWED += ALLOWED.upper()
ALLOWED += '1234567890-+_!@#$%^&*()~[],<>|:'


def clean(s):
    return ''.join([c for c in s if c in ALLOWED])

def IndexView(request):
    return render(request, 'index.html')

def CoinRedirView(request, id=None):
    if request.method == 'POST':
        #add to database
        custom = clean(request.POST['customUrl'])
        if custom:
            url1 = request.POST['url1']
            url2 = request.POST['url2']
            obj = CoinRedirectModel.objects.create(customUrl=custom, url1=url1, url2=url2)
            obj.save()
            return render(request, 'complete.html', {
                'url': 'https://urlt.herokuapp.com/c/' + custom
            })
        else:
            raise ValueError("Disallowed custom URL")
    else:
        #Search or return empty
        if id:
            obj = get_object_or_404(CoinRedirectModel, customUrl=id)
            url = ''
            if randint(0, 1) == 1:
                url = obj.url1
            else:
                url = obj.url2
            return redirect(url)
        else:
            return render(request, 'form.html', {
                'form': CreateCoinForm(),
                'title': 'Create new 50/50 URL'
            })

def BasicRedirView(request, id=None):
    if request.method == 'POST':
        #add to database
        custom = clean(request.POST['customUrl'])
        if custom:
            url = request.POST['url']
            obj = BasicUrlModel.objects.create(customUrl=custom, url=url)
            obj.save()
            return render(request, 'complete.html', {
                'url': 'https://urlt.herokuapp.com/' + custom
            })
        else:
            raise ValueError("Disallowed custom URL")
    else:
        #Search or return empty
        if id:
            obj = get_object_or_404(BasicUrlModel, customUrl=id)
            return redirect(obj.url)
        else:
            return render(request, 'form.html', {
                'form': CreateUrlForm(),
                'title': 'Create new shortened URL'
            })