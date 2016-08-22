from django.views.generic import View
from django.shortcuts import render

class MainView(View):
    
    def get(self, request, *args, **kwargs):

        return render(
                request,
                "main/main.html",
                context={},
        )
