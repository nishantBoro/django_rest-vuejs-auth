from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from DjangoRestAuth.models import Mods
from DjangoRestAuth.serializers import ModSerializer


# an example protected view:
class ModsView(generics.RetrieveAPIView):
    queryset = Mods.objects.all()
    serializer_class = ModSerializer()  # prepare JSON output for the queryset
    permission_classes = IsAuthenticated

    def as_view(self):
        queryset = self.get_queryset()
        serializer = ModSerializer(queryset, many=True)
        return Response(serializer.data)
