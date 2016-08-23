from django.views.generic import View
from django.shortcuts import render

from tour.models import TouristSpotData


class MainView(View):

    def get(self, request, *args, **kwargs):
        tours = TouristSpotData.objects.all()
        images = []
        for tour in tours:
            images.append(tour.image_url)
        return render(
                request,
                "main/main.html",
                context={
                    "image1": images[4895],
                    "image2": images[8343],
                    "image3": images[4],
                    "image4": images[7],
                    "image5": images[453],
                    "image6": images[1],
                    "image7": images[124],
                    "image8": images[56],
                },
        )
