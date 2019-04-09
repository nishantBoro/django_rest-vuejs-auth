from rest_framework import serializers
from DjangoRestAuth.models import Mods


# output serializer class for example view
class ModSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mods
        fields = '__all__'
        read_only_fields = '__all__'
