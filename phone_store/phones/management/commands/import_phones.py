from django.core.management.base import BaseCommand
import csv
from phones.models import Phone

class Command(BaseCommand):
    help = 'Import phones from a CSV file'
    def handle(self, *args, **options):
        with open('phone.csv') as csvfile:
            reader = csv.DictReader(csvfile,  delimiter=';')
            for row in reader:
                name = row['name']
                price = row['price']
                release_date = row['release_date']
                lte_exists = row['lte_exists']=='True'
                image = row['image']

                Phone.objects.create(
                    name=name,
                    price=price,
                    release_date=release_date,
                    lte_exists=lte_exists,
                    image=image,

                )
            self.stdout.write(self.style.SUCCESS('Импорт телефонов выполнен!'))


