from django.conf import settings

from celery import Task

from tour.utils.update_model import update_tour_model


class UpdateTourModelTask(Task):

    def run(self):
        update_tour_model()
