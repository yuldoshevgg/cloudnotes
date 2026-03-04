from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from notes import views

def home(request):
    return render(request, "home.html")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),

    path("notebooks/create/", views.create_notebook, name="create_notebook"),
    path("notebooks/update/<int:pk>/", views.update_notebook, name="update_notebook"),
    path("notebooks/delete/<int:pk>/", views.delete_notebook, name="delete_notebook"),
    path("notebooks/<int:pk>/", views.notebook_detail, name="notebook_detail"),
    path("notes/create/<int:notebook_id>/", views.create_note, name="create_note"),
    path("notes/update/<int:pk>/", views.update_note, name="update_note"),
    path("notes/delete/<int:pk>/", views.delete_note, name="delete_note"),
]