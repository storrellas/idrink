from django.core.management.base import BaseCommand, CommandError
from combiner.models import Ingredient, Drink

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        # Generate entities
        try:
            beefeater = Ingredient(name='beefeater', description='this is description for beefeater').save()
            dry_vermouth = Ingredient(name='dry_vermouth', description='this is description for dry_vermouth').save()
            orange = Ingredient(name='orange', description='this is description for dry_vermouth').save()

            drink = Drink( name="martini", description="this is a cool drink used among modernets", ingredient_list=[beefeater, dry_vermouth, orange]).save()
        except:
            raise CommandError('Failed to create entities')


        self.stdout.write(self.style.SUCCESS('Successfully created entities for drink'))
