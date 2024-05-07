from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import  HttpResponse


def getUser(request):
    redirectUrl = reverse('userDetail')
    return redirect(redirectUrl)

def userDetail(request):
    return render(request, 'UserDetail.html')

def userDetailEdit(request):
    return render(request, 'UserDetailEdit.html')