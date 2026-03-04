from django.db import models
from django.contrib.auth.models import User


class Notebook(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notebooks")
    shared_with = models.ManyToManyField(User, related_name="shared_notebooks", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE, related_name="notes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)
    notes = models.ManyToManyField(Note, related_name="tags", blank=True)

    def __str__(self):
        return self.name