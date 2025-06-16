from django.core.management.base import BaseCommand
from store.models import Category

class Command(BaseCommand):
    help = 'Ajoute des catégories initiales à la base de données'

    def handle(self, *args, **options):
        categories = [
            {'name': 'Gamme Luxe'}
            {'name': 'Gamme Pro'},
        ]

        for cat_data in categories:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Catégorie "{category.name}" ajoutée.'))
            else:
                self.stdout.write(self.style.WARNING(f'Catégorie "{category.name}" existe déjà.'))

        self.stdout.write(self.style.SUCCESS('Toutes les catégories ont été traitées.')) 