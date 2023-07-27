from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        category_list = [
            {'category_name': 'chancellery', 'category_description': 'pens, pencils...'},
            {'category_name': 'household chemicals', 'category_description': 'powder, soap...'},
            {'category_name': 'building materials', 'category_description': 'nails, screws...'}
        ]

        Category.objects.all().delete()

        categories_for_create = []

        for categories in category_list:
            categories_for_create.append(
                Category(**categories)
            )

        Category.objects.bulk_create(categories_for_create)