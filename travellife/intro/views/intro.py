from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class IntroView(View):

    def get(self, request, *args, **kwargs):

        return render(
                request,
                "intro/intro.html",
                context={},
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username", )
        password = "1234"
        user = authenticate(
                username=username,
                password=password,
        )

        if user:
            login(request, user)

            return render(
                    request,
                    "intro/intro.html",
                    context={},
            )
        user = User.objects.create_user(
                username=username,
                password=password,
        )

        return render(
                request,
                "intro/intro.html",
                context={},
        )
