from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login


class IntroView(View):

    def get(self, request, *args, **kwargs):

        return render(
                request,
                "intro/intro.html",
                context={},
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        try:
            user = User.objects.get(username=username)

            if user:
                login(request, user)

                return render(
                        request,
                        "intro/intro.html",
                        context={},
                )

        except:

            user = User.objects.create_user(
                                username=username,
            )
            user.set_unusable_password()
            user.save()

            return render(
                    request,
                    "intro/intro.html",
                    context={},
            )
