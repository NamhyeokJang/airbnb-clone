from django.core.management.base import BaseCommand

# from rooms import models as room_models
from rooms.models import Facility


class Command(BaseCommand):

    help = "Created Facilities"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times", help="How many times do you want me"
    #     )

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for facility in facilities:
            Facility.objects.create(name=facility)

        self.stdout.write(self.style.SUCCESS("Facilities created"))
