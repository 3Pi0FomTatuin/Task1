from django.contrib.auth.views import LoginView, LogoutView
from django.urls import re_path
from django.views.defaults import page_not_found

from shortener_app.views import CustomCreateView
from . import views
from .forms import CustomAuthenticationForm

urlpatterns = [
    re_path(r'^$', views.index, name='home'),
    re_path(r'^@login/$', LoginView.as_view(template_name='shortener_app/login.html', redirect_authenticated_user=True,
                                            authentication_form=CustomAuthenticationForm), name='login'),
    re_path(r'^@logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^@signup/$', CustomCreateView.as_view(), name='signup'),
    re_path(r'^@shorten/', views.shorten),
    re_path(r'^@get_user_links/', views.get_user_links),
    re_path(r'^favicon.ico$', page_not_found, {'exception': Exception()}),
    re_path(r'^', views.redirect),
]
