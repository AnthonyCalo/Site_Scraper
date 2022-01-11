from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect as redirect
from .models import Link
# Create your views here.

def scrape(request):
    if(request.method=="POST"):
        site = request.POST.get('site', '')
        try:
            page = requests.get(site)
            soup = BeautifulSoup(page.text, 'html.parser')
            for link in soup.find_all('a'):
                link_address = link.get('href')
                link_text= link.string
                Link.objects.create(address=link_address, name = link_text)
        except:
            print('error')
        return redirect('/')
    else:
        links = Link.objects.all()
        return render(request, 'link_scrape/scrape.html', {"links": links})
def delete(request):
    links = Link.objects.all()
    links.delete()
    return redirect('/') 
    # with open(r'C:/Users/acalo/Documents/mycode/webdev/webdevloose/homepage.html', 'r') as f:

    #     contents = f.read()

    #     soup = BeautifulSoup(contents, 'lxml')
  




