from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from DjangoRestAuth.models import Mods
from DjangoRestAuth.serializers import ModSerializer


# View for 'Mods' model
class ModsView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)  # checks if user is authenticated to view the model objects

    def get_queryset(self):
        return Mods.objects.all()  # return all model objects

    def get(self, request, *args, **kwargs):  # GET request handler for the model
        queryset = self.get_queryset()
        serializer = ModSerializer(queryset, many=True)
        return Response(serializer.data)
