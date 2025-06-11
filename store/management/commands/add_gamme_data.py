from django.core.management.base import BaseCommand
from store.models import PaintProduct

class Command(BaseCommand):
    help = 'Ajoute des données de gamme aux produits existants'

    def handle(self, *args, **options):
        # Mettre à jour les produits existants avec des gammes
        products = PaintProduct.objects.all()
        
        # Assigner des gammes basées sur le prix ou le nom
        for product in products:
            if product.price > 50 or 'luxe' in product.name.lower() or 'premium' in product.name.lower():
                product.gamme = 'luxe'
            else:
                product.gamme = 'pro'
            product.save()
            
        self.stdout.write(
            self.style.SUCCESS(f'Gammes assignées à {products.count()} produits')
        ) 