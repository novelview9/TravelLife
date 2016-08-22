from django.shortcuts import render


def tmap(request):
    return render(
        request,
        "tmap.html",
        context={},
    )
