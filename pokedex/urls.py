from django.urls import path
from . import views

app_name = "pokedex"

urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<int:id>/", views.pokemon, name="pokemon"),
    path("pokemon/add/", views.add_pokemon, name="add_pokemon"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path('edit_pokemon/<int:id>/', views.edit_pokemon, name="edit_pokemon"),
    path('delete_pokemon/<int:id>/', views.delete_pokemon, name="delete_pokemon"),
    path("trainers/", views.trainer_list, name="index_trainer"),
    path("trainer/<int:id>/", views.trainer_detail, name="trainer"),
    path("trainer/add/", views.add_trainer, name="add_trainer"),
    path("edit_trainer/<int:id>/", views.edit_trainer, name="edit_trainer"),
    path("delete_trainer/<int:id>/", views.delete_trainer, name="delete_trainer"),
]