import random

from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .models import Fish
from .models import Fishing

from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')

def fishing(request):
    fish_id = -1
    fish = Fish.objects.all()
    if request.method == "POST":
        if request.user.is_authenticated:
            fish_id = random.randint(1, fish.count())
            fish_weight = random.randint(100, 10000)
            Fishing.objects.create(fish_id=fish_id, user_id=request.user.id, weight=fish_weight)

    return render(request, 'main/fishing.html', {'fish': fish, 'fish_id': fish_id})
    # return HttpResponse("<h4>Hello</h4>")

def logout_user(request):
    logout(request)
    return redirect('home')

# class LoginUser(DataMixin, LoginView):
#     form_class = Authe
#     template_name = 'main/login.html'