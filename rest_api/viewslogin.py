from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt 

from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

from .models import Formulario

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    email = data['email']
    password = data['password']

    try:
        formulario = Formulario.objects.get(email=email)
    except Formulario.DoesNotExist:
        return Response("Correo electrónico o contraseña incorrectos.", status=status.HTTP_401_UNAUTHORIZED)

    # validar la contraseña
    if not formulario.check_password(password):
        return Response("Correo electrónico o contraseña incorrectos.", status=status.HTTP_401_UNAUTHORIZED)

    # inicio de sesión exitoso
    token, created = Token.objects.get_or_create(user=formulario)
    response_data = {"token": token.key, "core": "pagina_juegos"}
    return Response(response_data)