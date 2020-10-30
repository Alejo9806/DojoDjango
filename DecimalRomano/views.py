from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

# Create your views here.

def bienvenida(request):
    return HttpResponse("<h1>Bienvenido al mejor conversor de numeros decimales a romanos</h1> <h3>Ingresa a la ruta convertir/*Numero en decimal* para que obtengas un json con el numero en romano :)")


class convertir(APIView):
    
    def get(self, request,number, format=None):

        numeros = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        numerales = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        entero = number
        numeral =''
        i=0
        if(entero == 0):
            return Response("El numero no es valido para convertir a romano")
        while entero >0:
            for _ in range(entero // numeros[i]):
                numeral+= numerales[i]
                entero -= numeros[i]

            i +=1
        return Response({numeral})
