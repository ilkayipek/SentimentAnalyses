from typing import Union, List, Any, Generator

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from transformers import pipeline
import instaloader
from transformers.pipelines.pt_utils import PipelineIterator


def homePage(request):
    return render(request, 'HomePage.html')

def about(request):
    return render(request, 'About.html')

def communicate(request):
    return render(request, 'Communicate.html')

def getSentimentAnlyse(request):
    if request.method == 'POST':
        postUrl = request.POST.get('veri')
        print(postUrl)

        comments, post = getComments(postUrl)
        #print(f"çekilen yorumlar: {comments}")
        print(post.likes)

        result = sentimentAnalysis(comments)
        print(f"yorumların Analizi: {result}")

        optimizateData = dataOptimization(result)
        print(post.video_url)
        context = {'post': post, "dataResult": optimizateData}
        return render(request, 'partials/_sentimentAnalyseResult.html', context)


# Duygu analizi modelini yükle
nlp = pipeline("sentiment-analysis", model="savasy/bert-base-turkish-sentiment-cased")

#Duygu Analizini Yapabilmemiz İçin Data'nın Analizini Döndüren Fonksiyon
def sentimentAnalysis(data):
    #Duygu Analizi İçin Daha Önceden Eğitilmiş Modele Datayı Gönder
    try:
        # Çekilen Yorumları Analiz Fonksiyonuna Gönderir ve Sonuçları Alır
        results = nlp(data)
        return results
    except Exception as e:
        print(f"Analiz sırasında Bir Hata Oluştu: {e}")


def getComments(postUrl):
    # Kullanıcı adı ve şifre
    username = "motivasyonmest"
    password = "7631245ii"

    # Instaloader nesnesi oluşturun
    loader = instaloader.Instaloader()

    # Giriş yapın
    loader.login(username, password)

    # Gönderi nesnesi oluşturun
    # Kullanıcıdan Gönderi URL'sini Al

    post_shortcode = postUrl.split('/')[-2]

    # Yorumları Tutacağımız Boş Bir Array Oluştur
    data = []

    try:
        # Gönderinin nesnesini oluştur
        post = instaloader.Post.from_shortcode(loader.context, post_shortcode)
        print("Yorumlar Getiriliyor..")

        for comment in post.get_comments():
            # Her Yorumu data'ya ekle
            data.append(comment.text)

        print("Yorumlar getirildi.")
        print("Çekilen Yorum Sayısı: ", len(data), data)

    except instaloader.exceptions.BadResponseException as e:
        print("Yorumlar Alınırken Bir Hata Oluştu:", e)
    except Exception as e:
        print("Yorumlar Alınırken Beklenmeyen bir hata oluştu:", e)

    return data, post


def dataOptimization(commentsAnayses):
    # Analiz Sonucunda Sonuçları İstatistiğe Dökeceğimiz Sayaçlar
    positive = 0
    negative = 0
    neutral = 0

    for i in range(len(commentsAnayses) - 1):
        label = commentsAnayses[i]["label"]
        score = commentsAnayses[i]["score"]

        if score < 0.7:
            label = "natural"
            neutral = neutral + 1

        if label == "positive":
            positive = positive + 1
        elif label == "negative":
            negative = negative + 1
           
    print("pozitif sayısı: ", positive)
    print("negatif sayısı: ", negative)
    print("nötr sayısı: ", neutral)

    ratio = positive/ negative

    if ratio < 0:
        ratio *= -1

    ratio *= 10
    resultData = {"positive": positive, "negative": negative, "neutral": neutral, "ratio": ratio }
    
    return resultData

