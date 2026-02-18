from django.db import migrations

def add_10_destinations(apps, schema_editor):
    # Get the Destination model
    Destination = apps.get_model('tourism', 'Destination')
    
    data = [
        {"name": "Munnar", "url": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944", "price": 4500},
        {"name": "Alleppey", "url": "https://images.unsplash.com/photo-1593179241557-bce1eb92e47e", "price": 6000},
        {"name": "Wayanad", "url": "https://images.unsplash.com/photo-1581630132331-507c393d2566", "price": 3500},
        {"name": "Kochi", "url": "https://images.unsplash.com/photo-1589982840479-009968478465", "price": 2500},
        {"name": "Thekkady", "url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1", "price": 5000},
        {"name": "Varkala", "url": "https://images.unsplash.com/photo-1626081491410-62e924d55734", "price": 3000},
        {"name": "Kumarakom", "url": "https://images.unsplash.com/photo-1593693397690-362cb9666fc2", "price": 7500},
        {"name": "Kovalam", "url": "https://images.unsplash.com/photo-1601058268499-e52658b8bb88", "price": 4000},
        {"name": "Vagamon", "url": "https://images.unsplash.com/photo-1600100397608-f09074aa8891", "price": 2800},
        {"name": "Bekal", "url": "https://images.unsplash.com/photo-1616428717753-2947f6d39695", "price": 5500},
    ]
    
    for item in data:
        Destination.objects.get_or_create(
            name=item["name"], 
            image_url=item["url"],
            price_per_person=item["price"]
        )

class Migration(migrations.Migration):
    dependencies = [
        ('tourism', '0001_initial'), # This MUST match your first file name
    ]

    operations = [
        migrations.RunPython(add_10_destinations),
    ]