# from django.http import HttpResponse


# def index(request):
#     return HttpResponse('Hola Mundo!!!')

    # return -> llama la funcion HTTPRESPONSE
    # :-> Python no existe el punto y coma se cierra con dos puntos 

from django.shortcuts import render

def index(request):
    return render(request,'index.html',{
        #context
    })