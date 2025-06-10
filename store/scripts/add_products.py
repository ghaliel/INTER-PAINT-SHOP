from store.models import Category, PaintProduct

def run():
    c1, _ = Category.objects.get_or_create(name='Intérieur', defaults={'description':'Peintures pour murs et plafonds intérieurs'})
    c2, _ = Category.objects.get_or_create(name='Extérieur', defaults={'description':'Peintures résistantes aux intempéries pour façades'})
    c3, _ = Category.objects.get_or_create(name='Spécialité', defaults={'description':'Peintures à effets, magnétiques, tableau noir'})
    c4, _ = Category.objects.get_or_create(name='Accessoires', defaults={'description':'Pinceaux, rouleaux, bâches et autres accessoires de peinture'})

    products_data = [
        {'name':'Peinture Murale Blanche Mate', 'description':"Peinture à l'eau de haute qualité avec blancheur éclatante, pouvoir couvrant de 12 à 15 m2/Kg. Convient pour intérieur et extérieur, lessivable. Conditionnement: 5kg, 10kg, 20kg, 30kg, 40kg.", 'price':49.99, 'color':'Blanc', 'stock':80, 'category':c1, 'image_url':'static/images/default_paint_product.png'},
        {'name':'Peinture Lavable Beige Clair', 'description':"Peinture intérieure lavable couleur beige clair, haute couvrance. Facile d'application et lessivable. Convient pour murs et plafonds.", 'price':35.50, 'color':'Beige', 'stock':60, 'category':c1, 'image_url':'static/images/default_paint_product.png'},
        {'name':'Peinture Acrylique Vert Amande', 'description':"Peinture acrylique mate pour intérieur, séchage rapide, 2.5L. Offre un aspect velouté et une bonne résistance à l'humidité. Idéale pour chambres et salons.", 'price':28.00, 'color':'Vert Amande', 'stock':45, 'category':c1, 'image_url':'static/images/default_paint_product.png'},
        {'name':'Sous-couche Universelle', 'description':"Sous-couche acrylique pour tous supports, 10L. Améliore l'adhérence et l'uniformité de la peinture de finition. Séchage rapide.", 'price':40.00, 'color':'Blanc', 'stock':100, 'category':c4, 'image_url':'static/images/default_paint_product.png'},
        {'name':'Peinture Cuisine & Salle de Bain', 'description':"Peinture satinée anti-humidité et lessivable, 5L. Spécialement conçue pour les pièces humides, résistante aux taches et moisissures.", 'price':55.00, 'color':'Blanc', 'stock':70, 'category':c1, 'image_url':'static/images/default_paint_product.png'},
        
        {'name':'Peinture Façade Blanche', 'description':"Peinture extérieure microporeuse, haute durabilité, 10L. Résistante aux intempéries, fissures et UV. Excellente tenue dans le temps.", 'price':75.00, 'color':'Blanc', 'stock':50, 'category':c2, 'image_url':'static/images/default_paint_product.png'},
        {'name':'Peinture Bois Protection UV', 'description':"Lasure bois protection UV, toutes essences, 2.5L. Protège le bois des agressions climatiques et préserve sa couleur naturelle.", 'price':42.00, 'color':'Transparent', 'stock':30, 'category':c2, 'image_url':'static/images/default_paint_product.png'},
        {'name':'Peinture Métal Antirouille', 'description':"Peinture brillante pour métaux, haute protection antirouille, 1L. Applicable directement sur rouille, offre une finition durable.", 'price':22.00, 'color':'Gris Anthracite', 'stock':40, 'category':c2, 'image_url':'static/images/default_paint_product.png'},
        {'name':'Vernis Extérieur Transparent', 'description':"Vernis haute résistance pour boiseries extérieures, 1L. Offre une protection longue durée contre l'humidité et les UV, sans jaunir.", 'price':28.50, 'color':'Transparent', 'stock':35, 'category':c2, 'image_url':'static/images/default_paint_product.png'},
        {'name':'Peinture Sol Antidérapante', 'description':"Peinture de sol trafic intense, antidérapante, 5L. Idéale pour garages, terrasses ou ateliers. Résistante à l'abrasion et aux produits chimiques.", 'price':65.00, 'color':'Gris', 'stock':25, 'category':c2, 'image_url':'static/images/default_paint_product.png'},
        
        {'name':'Peinture Tableau Noir', 'description':"Peinture ardoise pour créer un tableau noir, 1L. Permet d'écrire et d'effacer à la craie. Idéale pour chambres d'enfants ou cuisines.", 'price':18.00, 'color':'Noir', 'stock':55, 'category':c3, 'image_url':'static/images/default_paint_product.png'},
        {'name':'Peinture Magnétique', 'description':"Peinture sous-couche magnétique, 1L. Transforme toute surface en tableau magnétique. Compatible avec tout type de peinture de finition.", 'price':25.00, 'color':'Gris', 'stock':30, 'category':c3, 'image_url':'static/images/default_paint_product.png'},
        {'name':'Peinture Effet Béton Ciré', 'description':"Kit peinture effet béton ciré pour sols et murs, 2kg. Crée une ambiance industrielle et moderne. Facile à appliquer.", 'price':90.00, 'color':'Gris', 'stock':15, 'category':c3, 'image_url':'static/images/default_paint_product.png'},
        {'name':'Peinture Phosphorescente', 'description':"Peinture qui brille dans le noir, idéale pour déco enfants, 0.5L. Crée des ambiances lumineuses originales. Non toxique.", 'price':30.00, 'color':'Vert', 'stock':20, 'category':c3, 'image_url':'static/images/default_paint_product.png'},
        {'name':'Peinture Anti-graffiti', 'description':"Peinture de protection anti-graffiti, facile à nettoyer, 5L. Empêche l'adhérence des graffitis et facilite leur élimination.", 'price':85.00, 'color':'Transparent', 'stock':10, 'category':c2, 'image_url':'static/images/default_paint_product.png'},

        {'name':'Kit Pinceaux Pro', 'description':"Assortiment de pinceaux professionnels pour tous types de peinture. Poils de haute qualité, pour une application précise et uniforme.", 'price':15.00, 'color':'N/A', 'stock':120, 'category':c4, 'image_url':'static/images/default_paint_product.png'},
        {'name':'Rouleau à Peinture Anti-goutte', 'description':"Rouleau haute qualité pour application sans traces ni gouttes. Idéal pour les grandes surfaces, assure un rendu homogène.", 'price':12.00, 'color':'N/A', 'stock':90, 'category':c4, 'image_url':'static/images/default_paint_product.png'},
        {'name':'Bâche de Protection', 'description':"Bâche de protection résistante pour sols et meubles, 4x5m. Protège efficacement contre les éclaboussures et la poussière.", 'price':8.00, 'color':'Transparent', 'stock':200, 'category':c4, 'image_url':'static/images/default_paint_product.png'},
        {'name':'Ruban de Masquage Précision', 'description':"Ruban adhésif de masquage haute précision, 50m. Permet des bords nets et précis sans bavures.", 'price':6.50, 'color':'Jaune', 'stock':150, 'category':c4, 'image_url':'static/images/default_paint_product.png'},
        {'name':'Bac à Peinture avec Grille', 'description':"Bac à peinture pratique avec grille d'essorage intégrée. Facilite l'imprégnation du rouleau et évite les surplus.", 'price':10.00, 'color':'Bleu', 'stock':80, 'category':c4, 'image_url':'static/images/default_paint_product.png'},
    ]

    for product_data in products_data:
        product, created = PaintProduct.objects.get_or_create(
            name=product_data['name'],
            defaults={
                'description': product_data['description'],
                'price': product_data['price'],
                'color': product_data['color'],
                'stock': product_data['stock'],
                'category': product_data['category'],
                'image_url': product_data['image_url']
            }
        )
        if created:
            print(f"Produit {product.name} créé.")
        else:
            print(f"Produit {product.name} existe déjà.") 