from rest_framework import serializers
from pokedex.models import Pokemon, Trainer
import base64
from django.core.files.base import ContentFile

class PokemonSerializers(serializers.ModelSerializer):
    picture = serializers.CharField(required=True, allow_blank=False)
    
    class Meta:
        model = Pokemon
        fields = '__all__'
    
    def validate_picture(self, value):
        if value:
            try: 
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                return ContentFile (
                    base64.b64decode(imgstr),
                    name=f'temp.{ext}'
                )
            except Exception:
                raise serializers.ValidationError("Imagen no válida")
        return None

class TrainerSerializers(serializers.ModelSerializer):
    picture = serializers.CharField(required=True, allow_blank=False)
    
    class Meta:
        model = Trainer
        fields = '__all__'
    
    def validate_picture(self, value):
        if value:
            try: 
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                return ContentFile (
                    base64.b64decode(imgstr),
                    name=f'temp.{ext}'
                )
            except Exception:
                raise serializers.ValidationError("Imagen no válida")
        return None