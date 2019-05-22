import short_url
from django.contrib.auth import authenticate
from django.contrib.auth import login as _login
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.http import require_GET
from django.views.generic import CreateView

from shortener_app.forms import CustomUserCreationForm
from shortener_app.models import Shortening

ENCODER = short_url.UrlEncoder(alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_.~')


def index(request):
    return render(request, 'shortener_app/index.html')


def login(request):
    return render(request, 'shortener_app/login.html')


class CustomCreateView(CreateView):
    template_name = 'shortener_app/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy(index)

    def form_valid(self, form):
        valid = super().form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        _login(self.request, new_user)
        return valid


@require_GET
def shorten(request):
    new_shortening = Shortening.objects.create(long_url=request.GET['url'],
                                               owner=request.user if request.user.is_authenticated else None)
    new_shortening.short_url = ENCODER.encode_url(new_shortening.id)
    new_shortening.save()
    return JsonResponse(
        (new_shortening.long_url, new_shortening.short_url),
        safe=False
    )


def redirect(request):
    try:
        shortening_id = ENCODER.decode_url(request.path[1:])
    except ValueError:
        raise Http404("Shortening does not exist.")
    try:
        shortening = Shortening.objects.get(id=shortening_id)
    except ObjectDoesNotExist:
        raise Http404("URL is incorrect.")

    return HttpResponseRedirect(shortening.long_url)


@require_GET
def get_user_links(request):
    return JsonResponse(
        list(Shortening.objects.filter(owner_id=request.GET['id']).values_list('long_url', 'short_url')),
        safe=False)
