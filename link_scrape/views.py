from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect as redirect
from .models import Link, Img, H1, H2, Paragraph
# Create your views here.

def scrape(request):
    if(request.method=="POST"):
        site = request.POST.get('site', '')
        tag = request.POST.get("tag",'')
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')
        if(tag=="a"):
            try:
                for link in soup.find_all('a'):
                    link_address = link.get('href')
                    link_text= link.string
                    Link.objects.create(address=link_address, name = link_text)
            except:
                print('error')
            return redirect('/')
        elif(tag=="img"):
            try:
                for img in soup.find_all('img'):
                    img_alt = img['alt']
                    img_src = img['src']
                    Img.objects.create(address=img_alt, name=img_src)

            except Exception as e:
                print("IMG error:{}".format(e))
            return redirect('img')
        elif(tag=="h1"):
            print("here")
            try:
                for h1 in soup.find_all('h1'):
                    inner_text = " ".join(h1.text.split())
                    className = h1['class']
                    H1.objects.create(inner_text=inner_text, class_name=className)
            except Exception as e:
                print("H1 error:{}".format(e))
            return redirect('h1s')
        elif(tag=="h2"):
            try:
                for h2 in soup.find_all('h2'):
                    inner_text = " ".join(h2.text.split())
                    className = h2['class']
                    H2.objects.create(inner_text=inner_text, class_name=className)
            except Exception as e:
                print("H2 error:{}".format(e))
            return redirect('h2s')
        elif(tag=="p"):
            try:
                for h2 in soup.find_all('p'):
                    inner_text = " ".join(h2.text.split())
                    className = h2['class']
                    Paragraph.objects.create(inner_text=inner_text, class_name=className)
            except Exception as e:
                print("H2 error:{}".format(e))
            return redirect('paragraphs')
            
    else:
        links = Link.objects.all()
        return render(request, 'link_scrape/scrape.html', {"links": links, "delete": 'delete'})

def img_view(request):
    images = Img.objects.all()
    return render(request, 'link_scrape/img.html', {"imgs": images})

def h1_view(request):
    h1s = H1.objects.all()
    print(h1s)
    return render(request, 'link_scrape/h_page.html', {"h_tags": h1s})

def h2_view(request):
    h2s = H2.objects.all()
    return render(request, 'link_scrape/h_page.html', {"htags": h2s})

def para_view(request):
    paragraphs = Paragraph.objects.all()
    return render(request, 'link_scrape/para.html', {"paragraphs": paragraphs})


def delete(request):
    del_list = [Link, H1, H2, Paragraph, Img]
    for i in del_list:
        print("FARTS")
        obs = i.objects.all()
        print(obs, "obs")
        obs.delete()
    return redirect('/') 

def delete_img(request):
    del_list = [Link, H1, H2, Paragraph, Img]
    for i in del_list:
        obs = i.objects.all()
        obs.delete()
    return redirect('/') 
    # with open(r'C:/Users/acalo/Documents/mycode/webdev/webdevloose/homepage.html', 'r') as f:

    #     contents = f.read()

    #     soup = BeautifulSoup(contents, 'lxml')
  




