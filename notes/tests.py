import pytest
from django.contrib.auth.models import User
from .models import Notebook


@pytest.mark.django_db
def test_create_notebook():
    user = User.objects.create_user(username="testuser", password="pass123")
    notebook = Notebook.objects.create(title="Test", owner=user)

    assert notebook.title == "Test"
    assert notebook.owner.username == "testuser"