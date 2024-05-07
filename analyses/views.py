

from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

data = {
    1: "Analiz1",
    2: "Analiz2",
    3: "Analiz3"
}

posts =  [
        {"id": 1, "username": "lcwakiki", "description": "Jean elbisesi, nakışlı gömleği ve şort eteği ile küçük hanımlar bu yaz yine çok şık!",
        "totalComment": 100, "totalLike": 2000, "url": "https://scontent.cdninstagram.com/v/t39.30808-6/440127905_18435588901038736_7539407677929740553_n.jpg?stp=dst-jpg_e35_p1080x1080&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMzUweDE2ODcuc2RyLmYzMDgwOCJ9&_nc_ht=scontent.cdninstagram.com&_nc_cat=104&_nc_ohc=nmNGTBGWx0MQ7kNvgEmGumG&edm=APs17CUAAAAA&ccb=7-5&ig_cache_key=MzM1NjAyMjA2MzgwODQ4ODIyNg%3D%3D.2-ccb7-5&oh=00_AfA44Y0RaI3mus0MV54RhYWfd0PJZxw6F1dskES72qQYLg&oe=663BCCD6&_nc_sid=10d13b"},
{"id": 2, "username": "lcwakiki", "description": "Jean elbisesi, nakışlı gömleği ve şort eteği ile küçük hanımlar bu yaz yine çok şık!",
        "totalComment": 100, "totalLike": 2000,"url": "https://scontent.cdninstagram.com/v/t39.30808-6/440127905_18435588901038736_7539407677929740553_n.jpg?stp=dst-jpg_e35_p1080x1080&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMzUweDE2ODcuc2RyLmYzMDgwOCJ9&_nc_ht=scontent.cdninstagram.com&_nc_cat=104&_nc_ohc=nmNGTBGWx0MQ7kNvgEmGumG&edm=APs17CUAAAAA&ccb=7-5&ig_cache_key=MzM1NjAyMjA2MzgwODQ4ODIyNg%3D%3D.2-ccb7-5&oh=00_AfA44Y0RaI3mus0MV54RhYWfd0PJZxw6F1dskES72qQYLg&oe=663BCCD6&_nc_sid=10d13b"},
{"id": 3, "username": "lcwakiki", "description": "Jean elbisesi, nakışlı gömleği ve şort eteği ile küçük hanımlar bu yaz yine çok şık!",
        "totalComment": 100, "totalLike": 2000, "url": "https://scontent.cdninstagram.com/v/t39.30808-6/440127905_18435588901038736_7539407677929740553_n.jpg?stp=dst-jpg_e35_p1080x1080&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMzUweDE2ODcuc2RyLmYzMDgwOCJ9&_nc_ht=scontent.cdninstagram.com&_nc_cat=104&_nc_ohc=nmNGTBGWx0MQ7kNvgEmGumG&edm=APs17CUAAAAA&ccb=7-5&ig_cache_key=MzM1NjAyMjA2MzgwODQ4ODIyNg%3D%3D.2-ccb7-5&oh=00_AfA44Y0RaI3mus0MV54RhYWfd0PJZxw6F1dskES72qQYLg&oe=663BCCD6&_nc_sid=10d13b"},
    ]


def analyse(request):
    redirectUrl = reverse('userAnalyses')
    return redirect(redirectUrl)

def analyses(request):

    return render(request, 'SentimentAnalyses.html', {
        "analysesList": posts
    })

def analyseDetail(request, analyseId):
    analyse = data[analyseId]
    return render(request, 'SentimentAnalyseDetail.html', {
        "analyse": analyse
    })

