# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import io
from google.cloud import vision
from .models import Company, Product, TextRating, EmotionRating
from django.http import HttpResponse
from havenondemand.hodclient import HODClient
from havenondemand.hodclient import *
from django.shortcuts import redirect
import os
from django.views.decorators.csrf import csrf_exempt


myAPIkey = '7fb90fc7-7f5a-478c-8bcc-fc3dbc78b40b'


def get_homepage(request):
    return render(request, 'index.html', {
        "title": "PenViewer"
    })


def get_emotion(path):
    vision_client = vision.Client()
    with io.open(os.getcwd() + path, 'rb') as image_file:
        content = image_file.read()
    image = vision_client.image(content=content)
    faces = image.detect_faces()
    face = faces[0]
    data = {
        "joy": face.joy.value,
        "surprise": face.surprise.value,
        "sorrow": face.sorrow.value
    }
    return data


def get_product_list(request, cslug=None):
    company = Company.objects.get(cslug=cslug)
    return render(request, 'company.html', {
        "title": company.cname
    })


def get_product_analytics(request, cslug=None, pslug=None):
    product = Product.objects.get(pslug=pslug)
    text = TextRating.objects.filter(pkey=product)
    image = TextRating.objects.filter(pkey=product)
    return render(request, 'product.html', {
        "title": product.pname
    })

@csrf_exempt
def set_text_rating(request):
    if request.method == 'GET':
        return render(request, 'text.html', {
            "products": Product.objects.all()
        })
    else:
        data = request.POST
        cc = {
            "gender": data["gender"],
            "longitude": data["longitude"],
            "age": data["age"],
            "latitude": data["latitude"],
            "text": request.POST['text']
        }

        text = request.POST['text']
        client = HODClient(myAPIkey, version="v1")
        data1 = {'text': text}
        r = client.post_request(data1, 'analyzesentiment', async=False)
        sentiment = r['aggregate']['sentiment']
        score = r['aggregate']['score']

        product = Product.objects.get(pslug=data["pslug"])
        cc["pkey"] = product
        cc["rating"] = str(score)
        data = TextRating.objects.create(**cc)
        data.save()
        return redirect('/text/create')


@csrf_exempt
def set_image_rating(request):
    if request.method == 'GET':
        return render(request, 'emotion.html', {
            "products": Product.objects.all()
        })
    else:

        data = request.POST
        cc = {
            "gender": data["gender"],
            "longitude": data["longitude"],
            "age": data["age"],
            "latitude": data["latitude"],
        }

        # myfile = request.FILES['emotion_image']
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)
        # pp(uploaded_file_url)

        product = Product.objects.get(pslug=data["pslug"])
        cc["pkey"] = product
        cc["emotion"] = 'dsgfadg'
        cc['emotion_image'] = request.FILES['emotion_image']

        data = EmotionRating.objects.create(**cc)
        data.save()
        t = get_emotion(data.emotion_image.url)
        print t
        if t["joy"] == 'VERY_LIKELY':
            data.emotion = '1'
        elif t["sorrow"] == 'VERY_LIKELY':
            data.emotion = '-1'
        else:
            data.emotion = '0'
        data.save()
        return redirect('/image/create')
