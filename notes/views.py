from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Notebook
from .forms import NotebookForm


def home(request):
    return render(request, "home.html")


@login_required
def dashboard(request):
    notebooks = Notebook.objects.filter(owner=request.user)
    return render(request, "dashboard.html", {"notebooks": notebooks})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})


@login_required
def create_notebook(request):
    if request.method == "POST":
        form = NotebookForm(request.POST)
        if form.is_valid():
            notebook = form.save(commit=False)
            notebook.owner = request.user
            notebook.save()
            return redirect("dashboard")
    else:
        form = NotebookForm()

    return render(request, "notebooks/create.html", {"form": form})


@login_required
def update_notebook(request, pk):
    notebook = get_object_or_404(Notebook, pk=pk, owner=request.user)

    if request.method == "POST":
        form = NotebookForm(request.POST, instance=notebook)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = NotebookForm(instance=notebook)

    return render(request, "notebooks/update.html", {"form": form})


@login_required
def delete_notebook(request, pk):
    notebook = get_object_or_404(Notebook, pk=pk, owner=request.user)

    if request.method == "POST":
        notebook.delete()
        return redirect("dashboard")

    return render(request, "notebooks/delete.html", {"notebook": notebook})