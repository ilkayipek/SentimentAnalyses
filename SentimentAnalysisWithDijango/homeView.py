from django.shortcuts import render
from django.http import HttpResponse

def submit_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        return HttpResponse(f"Merhaba, {username}!")
    else:
        return render(request, 'homepage.html')
