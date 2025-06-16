from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from store.models import Category, PaintProduct

class Command(BaseCommand):
    help = 'Ajoute des données de test pour INTER PAINT'

    def handle(self, *args, **options):
        self.stdout.write('Création des données de test...')
        
        # Créer des catégories
        categories_data = [
            {
                'name': 'Peinture Intérieure',
                'description': 'Peintures spécialement formulées pour l\'intérieur de votre maison. Résistantes aux taches et faciles à nettoyer.'
            },
            {
                'name': 'Peinture Extérieure',
                'description': 'Peintures résistantes aux intempéries pour vos façades et extérieurs. Protection longue durée.'
            },
            {
                'name': 'Primaires & Apprêts',
                'description': 'Préparez vos surfaces avec nos primaires de qualité pour une adhérence optimale.'
            },
            {
                'name': 'Peintures Spéciales',
                'description': 'Peintures spécialisées pour des usages particuliers : anti-humidité, anti-moisissure, etc.'
            }
        ]
        
        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(f'✓ Catégorie créée: {category.name}')
            else:
                self.stdout.write(f'⚠ Catégorie existante: {category.name}')
        
        # Créer des produits
        products_data = [
            {
                'name': 'Peinture Lavable Premium',
                'description': 'Peinture intérieure de qualité supérieure, résistante aux taches et facile à nettoyer. Idéale pour les murs et plafonds.',
                'price': 45.90,
                'color': 'Blanc',
                'stock': 150,
                'category': 'Peinture Intérieure',
                'gamme': 'luxe'
            },
            {
                'name': 'Peinture Façade Résistante',
                'description': 'Peinture extérieure haute résistance pour protéger vos façades des intempéries. Tenue longue durée garantie.',
                'price': 52.50,
                'color': 'Beige',
                'stock': 80,
                'category': 'Peinture Extérieure',
                'gamme': 'pro'
            },
            {
                'name': 'Primaire Universel Adhérent',
                'description': 'Primaire universel pour préparer toutes vos surfaces avant peinture. Améliore l\'adhérence et la durabilité.',
                'price': 28.75,
                'color': 'Blanc',
                'stock': 200,
                'category': 'Primaires & Apprêts',
                'gamme': 'pro'
            },
            {
                'name': 'Peinture Anti-Humidité',
                'description': 'Peinture spéciale anti-humidité pour les pièces humides. Résiste à la condensation et aux moisissures.',
                'price': 38.90,
                'color': 'Blanc',
                'stock': 60,
                'category': 'Peintures Spéciales',
                'gamme': 'luxe'
            },
            {
                'name': 'Peinture Salle de Bain',
                'description': 'Peinture spécialement conçue pour les salles de bain. Résistante à l\'humidité et aux projections d\'eau.',
                'price': 42.00,
                'color': 'Bleu Ciel',
                'stock': 45,
                'category': 'Peintures Spéciales',
                'gamme': 'pro'
            },
            {
                'name': 'Peinture Cuisine',
                'description': 'Peinture lavable pour cuisine, résistante aux graisses et aux taches. Facile à entretenir.',
                'price': 39.50,
                'color': 'Créme',
                'stock': 75,
                'category': 'Peinture Intérieure',
                'gamme': 'pro'
            },
            {
                'name': 'Peinture Chambre Enfant',
                'description': 'Peinture écologique et sans danger pour les chambres d\'enfants. Couleurs douces et apaisantes.',
                'price': 48.00,
                'color': 'Rose Pâle',
                'stock': 30,
                'category': 'Peinture Intérieure',
                'gamme': 'luxe'
            },
            {
                'name': 'Peinture Garage',
                'description': 'Peinture résistante pour garage et locaux techniques. Protection contre les hydrocarbures.',
                'price': 35.00,
                'color': 'Gris',
                'stock': 90,
                'category': 'Peintures Spéciales',
                'gamme': 'pro'
            }
        ]
        
        for prod_data in products_data:
            product, created = PaintProduct.objects.get_or_create(
                name=prod_data['name'],
                defaults={
                    'description': prod_data['description'],
                    'price': prod_data['price'],
                    'color': prod_data['color'],
                    'stock': prod_data['stock'],
                    'category': categories[prod_data['category']],
                    'gamme': prod_data['gamme']
                }
            )
            if created:
                self.stdout.write(f'✓ Produit créé: {product.name} - {product.price} MAD')
            else:
                self.stdout.write(f'⚠ Produit existant: {product.name}')
        
        self.stdout.write(self.style.SUCCESS('✅ Données de test créées avec succès!'))
        self.stdout.write('Vous pouvez maintenant accéder à l\'administration à l\'adresse: http://127.0.0.1:8000/admin/') 