from store.models import PaintProduct

def run():
    updates = [
        {'name': 'Peinture Façade Blanche', 'image_url': 'https://images.unsplash.com/photo-1596700684206-8b0106295328?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'},
        {'name': 'Peinture Bois Protection UV', 'image_url': 'https://images.unsplash.com/photo-1627914619420-7f415c1e1c31?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'},
        {'name': 'Peinture Anti-graffiti', 'image_url': 'https://images.unsplash.com/photo-1616853258814-11116c4f52e5?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'},
        {'name': 'Rouleau à Peinture Anti-goutte', 'image_url': 'https://images.unsplash.com/photo-1574069818820-27f6b9b3e1c6?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'},
        {'name': 'Bâche de Protection', 'image_url': 'https://images.unsplash.com/photo-1615364177264-b6c860c29a8f?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'},
        {'name': 'Ruban de Masquage Précision', 'image_url': 'https://images.unsplash.com/photo-1582030635905-3b1a8f946859?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'},
        {'name': 'Bac à Peinture avec Grille', 'image_url': 'https://images.unsplash.com/photo-1615364177264-b6c860c29a8f?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'},
    ]

    for item in updates:
        try:
            product = PaintProduct.objects.get(name=item['name'])
            product.image_url = item['image_url']
            product.save()
            print(f"Image de {product.name} mise à jour.")
        except PaintProduct.DoesNotExist:
            print(f"Produit {item['name']} non trouvé.") 