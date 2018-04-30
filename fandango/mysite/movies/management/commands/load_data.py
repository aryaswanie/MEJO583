import datetime
import json

from django.core.management.base import BaseCommand, CommandError
from movies.models import Movie, Showtime, Theater

#codes from class 18
#thanks for my classmates for helping me with command codes!
class Command(BaseCommand):
    help = 'Load movie data into the database'
    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)
    def handle(self, *args, **options):
        json_path = options['json_file']
        self.stdout.write(self.style.SUCCESS('Loading JSON from "{}"'.format(json_path)))
        data = json.load(open(json_path))
        total = len(data)
        self.stdout.write(self.style.SUCCESS('Processing {} rows'.format(total)))
        skipped = []


        for i, row in enumerate(data):
            theaters = row['theaters']
            for j, theater in enumerate(theaters):
                try:
                    name = theater['name']
                    address = theater['address1']
                    phone = theater['phone']
                    geo = theater['geo']
                    city = theater['city']
                    id = theater['id']


                    theaterInstance, _ = Theater.objects.get_or_create(
                        name = name,
                        address = address,
                        phone = phone,
                        lat = 0.0000,
                        long = 0.0000,
                        city = city,
                        th_id = id,
                    )

                    movies = theater.get('movies')
                    if(movies):
                        movieList = []
                        for m, movie in enumerate(movies):

                            movieInstance, _ = Movie.objects.get_or_create(
                                title = movie['title'],
                                runtime = movie['runtime'],
                                poster = movie['poster']['size']['full'][2:],
                                movie_genre = movie['genres'][0],
                                rating = movie['rating'],
                                movie_id = movie['id'],
                            )
                            theaterInstance.movie_set.add(movieInstance)
                            movieInstance.theaters.add(theaterInstance)
                                                    )
                except:
                    skipped.append(theater)
                    print(th_name)
                    continue

                self.stdout.write(self.style.SUCCESS('Processed {}/{}'.format(i + 1, total)), ending='\r')
                self.stdout.flush()

        if skipped:
            self.stdout.write(self.style.WARNING("Skipped {} records".format(len(skipped))))
            with open('skipped.json', 'w') as fh:
                json.dump(skipped, fh)
