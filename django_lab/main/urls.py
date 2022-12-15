from django.urls import path
from . import views
from django.contrib.auth import views as djangoViews
from .forms import UserLoginForm

urlpatterns = [
    path('login/', djangoViews.LoginView.as_view(template_name="registration/login.html", authentication_form=UserLoginForm), name='login'),
    path('logout', views.logout_user, name='logout'),
    path('', views.index, name='home'),
    path('fishing', views.fishing, name='fishing'),
]