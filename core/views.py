from django.shortcuts import render,HttpResponse
# Create your views here.
def index(request): #request es un objeto que contiene toda la información
    # de la petición que se hace al servidor
    #peticion desde el navegador
    return render(request, "core/index.html")
#otra vista
def about(request):
    return render(request, "core/about.html")






