from django.core.management.base import BaseCommand, CommandError
from movies.models import Movie, Showtime, Theater

# Here we are creating a custom management command to load our winner data into
# Django models.
# The Command class is loaded by Django at runtime and executed when the file
# that contains it is specified as the command to manage.py
# In our case this file is called `load_winners.py` so the command we will use
# to execute this file is `manage.py load_winners path/to/winners.json`
class Command(BaseCommand):
    help = 'Remove all movie data from the database'

    # The handle method is the main function of the command. This is the entry
    # point for our command and contains all our business logic.
    def handle(self, *args, **options):
        Movie.objects.all().delete()
        Theater.objects.all().delete()
        Showtime.objects.all().delete()
