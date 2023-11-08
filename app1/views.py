from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "app1/home.html")


def index(request):
    from_scale = request.GET.get("from_scale")
    to_scale = request.GET.get("to_scale")
    valor = request.GET.get("valor")

    celsius = "Nenhum Valor"
    fahrenheit = "Nenhum Valor"
    kelvin = "Nenhum Valor"

    if from_scale == "celsius" and to_scale == "fahrenheit":
        celsius = float(valor)
        fahrenheit = (9 * celsius + 160) / 5
        fahrenheit = round(fahrenheit, 2)
    elif from_scale == "celsius" and to_scale == "kelvin":
        celsius = float(valor)
        kelvin = celsius + 273.15
        kelvin = round(kelvin, 2)
    elif from_scale == "fahrenheit" and to_scale == "celsius":
        fahrenheit = float(valor)
        celsius = (5 * (fahrenheit - 32)) / 9
        celsius = round(celsius, 2)
    elif from_scale == "fahrenheit" and to_scale == "kelvin":
        fahrenheit = float(valor)
        c = (5 * (fahrenheit - 32)) / 9
        kelvin = c + 273.15
        kelvin = round(kelvin, 2)
    elif from_scale == "kelvin" and to_scale == "celsius":
        kelvin = float(valor)
        celsius = kelvin - 273.15
        celsius = round(celsius, 2)
    elif from_scale == "kelvin" and to_scale == "fahrenheit":
        kelvin = float(valor)
        c = kelvin - 273.15
        fahrenheit = (c * 9 / 5) + 32
        fahrenheit = round(fahrenheit, 2)

    return render(request, 'app1/valor.html', {'celsius': celsius, 'fahrenheit': fahrenheit, 'kelvin': kelvin})
