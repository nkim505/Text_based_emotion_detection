from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.conf import settings
from . import inference_bert


# Create your views here.

def index(request):
    return render(request, 'main_app/index.html', {})


def aboutus(request):
    return render(request, 'main_app/aboutus.html', {})


def contacts(request):
    return render(request, 'main_app/contacts.html', {})


def chathome(request):
    return render(request, 'main_app/chathome.html',{})


def dl_emotion(request):

    target_sentence = request.POST['target_sentence']
    tokenizer = settings.TOKENIZER_KOBERT
    model = settings.MODEL_KOBERT

    result_bert = inference_bert.predict_sentiment(target_sentence, tokenizer, model)

    context = {'target_sentence':target_sentence, 'result_bert':result_bert}

    return render(request, "main_app/chatresult.html", context)
