from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .models import Pokemon
from .forms import PokemonForm

def index(request):
    pokemons = Pokemon.objects.order_by('name')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request,id: int):
    pokemon = Pokemon.objects.get(pk=id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
        
    else:
        form = PokemonForm()
            
    return render (request, 'pokemon_form.html', {'form': form})