# Generated by Django 3.0.4 on 2020-03-19 11:29

from django.db import migrations


def attach_ingredients_to_prices(apps, schema_editor):
   '''
   For Prices that haven't moved over to Ingredients yet, set the
   Ingredient from the Product
   '''
   Price = apps.get_model('products','Price')
   prices = Price.objects.filter(ingredient__isnull=True)

   for p in prices:
      p.ingredient = p.product.ingredient
      p.save()

def null_revert(apps, schema_editor):
   '''
   To "revert" this migration, do nothing.
   '''
   pass

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_price_ingredient'),
    ]

    operations = [
      migrations.RunPython(attach_ingredients_to_prices,null_revert)
    ]
