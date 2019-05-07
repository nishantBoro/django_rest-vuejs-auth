from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from DjangoRestAuth.models import Mods
from DjangoRestAuth.serializers import ModSerializer


# an example protected view:
class ModsView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Mods.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ModSerializer(queryset, many=True)
        return Response(serializer.data)
