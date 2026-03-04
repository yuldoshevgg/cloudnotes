from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Notebook, Note
from .forms import NotebookForm, NoteForm


# ---------- BASIC PAGES ----------

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


# ---------- NOTEBOOK CRUD ----------

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


# ---------- NOTE CRUD ----------

@login_required
def notebook_detail(request, pk):
    notebook = get_object_or_404(Notebook, pk=pk, owner=request.user)
    notes = notebook.notes.all()
    return render(request, "notes/notebook_detail.html", {
        "notebook": notebook,
        "notes": notes
    })


@login_required
def create_note(request, notebook_id):
    notebook = get_object_or_404(Notebook, pk=notebook_id, owner=request.user)

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.notebook = notebook
            note.save()
            form.save_m2m()
            return redirect("notebook_detail", pk=notebook.id)
    else:
        form = NoteForm()

    return render(request, "notes/create_note.html", {"form": form})


@login_required
def update_note(request, pk):
    note = get_object_or_404(Note, pk=pk, notebook__owner=request.user)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("notebook_detail", pk=note.notebook.id)
    else:
        form = NoteForm(instance=note)

    return render(request, "notes/update_note.html", {"form": form})


@login_required
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk, notebook__owner=request.user)

    if request.method == "POST":
        notebook_id = note.notebook.id
        note.delete()
        return redirect("notebook_detail", pk=notebook_id)

    return render(request, "notes/delete_note.html", {"note": note})