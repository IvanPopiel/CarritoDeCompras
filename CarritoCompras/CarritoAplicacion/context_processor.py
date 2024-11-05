#Este apartado nos permite guardar nuestro carrito de forma global en la aplicacion

def ordenCompra(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += float(value["precioFinal"])
    return {"ordenCompra": total}

    #de aca vuelvo a setting
