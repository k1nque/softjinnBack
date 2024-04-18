from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
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
        ideas = [{"shortDescription": idea.title, "details": idea.description} for idea in wishes.objects.all()]
        return HttpResponse(content=dumps(ideas))
