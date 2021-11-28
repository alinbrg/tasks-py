from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse



class NewTaskForm(forms.Form):
    # task is  name of input and is variable
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

# Create your views here.
def index(request):
    # create task for each user
    
    if "tasks" not in request.session:
        request.session["tasks"] = []
    # after this django stores data in table, we need to create it too
    # run command in terminal 
    # python manage.py migrate

    return render(request, "todo/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        # variable form
        form = NewTaskForm(request.POST)
        if form.is_valid():
            # get data from form, add 
            # save it as variable and add to tasks
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            # after submiting return to tasks list
            return HttpResponseRedirect(reverse("todolist:index"))
        else:
            # if form fields arent valid, send back form
            # they submited with its errors
            return render(request, "todo/add.html", {
                "form": form
            })
    return render(request, "todo/add.html", {
        "form": NewTaskForm()
    })