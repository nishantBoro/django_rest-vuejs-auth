from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from DjangoRestAuth.models import Mods
from DjangoRestAuth.serializers import ModSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
import json
from django.contrib.auth.hashers import make_password
from django.db.utils import IntegrityError


# View for 'Mods' model
class ModsView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)  # checks if user is authenticated to view the model objects

    def get_queryset(self):
        return Mods.objects.all()  # return all model objects

    def get(self, request, *args, **kwargs):  # GET request handler for the model
        queryset = self.get_queryset()
        serializer = ModSerializer(queryset, many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(['GET', 'POST'])
def register(request):
    body = json.loads(request.body)
    if body['password'] == body['confirm']:
        try:
            user = User.objects.create_user(username=body['username'], email=body['email'], password=make_password(body['password']))
            return Response("Success", status=202)
        except IntegrityError:
            return Response("User already exists", status=401)            
    else:
        return Response("Passwords don't match", status=401)
