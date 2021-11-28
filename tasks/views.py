from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, "tasks/index.html")

def alina(request):
  return HttpResponse("hello, alina")

def greet(request, name):
  # return HttpResponse(f"hello, {name.capitalize()}")
  return render(request, "tasks/greet.html", {
    "name": name.capitalize()
  })

