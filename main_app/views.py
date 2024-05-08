from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from main_app.forms import RegisterUserForm, LoginUserForm
from json import loads, dumps
from main_app.models import wishes, wishes_to_implements


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
    
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        objs = wishes_to_implements.objects.filter(wish_id=self.kwargs['id'])
        context["usernames"] = [el.implementer_username.username for el in objs]
        return context


def make_response(request, id):
    if request.method == "POST":
        session_key = loads(request.body)["sessionId"]
        session = Session.objects.get(session_key=session_key)
        print(session)
        uid = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(pk=uid)
        wish = wishes.objects.get(wish_id=id)
        try:
            wishes_to_implements.objects.get(wish_id=wish, implementer_username=user)
        except wishes_to_implements.DoesNotExist:
            w2e = wishes_to_implements(wish_id=wish, implementer_username=user)
            w2e.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)
