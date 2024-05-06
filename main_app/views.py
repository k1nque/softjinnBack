from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from main_app.forms import RegisterUserForm, LoginUserForm
from json import loads, dumps
from main_app.models import wishes


def home(request):
    return render(request, "index.html")


@csrf_exempt
def createNewIdea(request):
    if request.method == "POST":
        data = loads(request.body)
        print(data)
        wish = wishes(title=data["shortDescription"], description=data["details"])
        wish.save()
        return HttpResponse(status_code=200)
    else:
        return HttpResponse(status_code=400)


@csrf_exempt
def getAllIdeas(request):
    if request.method == "GET":
        ideas = [{"id": str(idea.wish_id), "shortDescription": idea.title, "details": idea.description} for idea in wishes.objects.all()]
        return HttpResponse(content=dumps(ideas))
    

def logout_user(request):
    logout(request)
    return redirect('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('home')
    

class ShowIdea(DetailView):
    model = wishes
    template_name = 'idea.html'
    context_object_name = 'idea'
    

    def get_object(self):
        return wishes.objects.get(wish_id=self.kwargs['id'])
