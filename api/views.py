from rest_framework import viewsets
from pokedex.models import Pokemon
from pokedex.models import Trainer
from .serializers import PokemonSerializers, TrainerSerializers
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope
from rest_framework.permissions import IsAuthenticated, AllowAny

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.order_by('name')
    serializer_class = PokemonSerializers
    
    authentication_classes = [OAuth2Authentication]
    required_scopes = ['write']
    
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), TokenHasScope()]
        return [AllowAny()]

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.order_by('name')
    serializer_class = TrainerSerializers
    
    authentication_classes = [OAuth2Authentication]
    required_scopes = ['write']
    
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), TokenHasScope()]
        return [AllowAny()]
