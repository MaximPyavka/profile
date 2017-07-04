from django.core.management import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    # A command must define handle()
    def handle(self, *args, **options):
        for i in apps.get_models():
            print("Model - {}, objects created - {}".format(i.__name__, i.objects.all().count()))
