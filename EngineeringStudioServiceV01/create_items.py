from django.core.management.base import BaseCommand
from EngineeringStudioService.EngineeringStudioServiceV01.accounting.models import *

class Command(BaseCommand):
    help = 'Create new items in the database'

    def handle(self, *args, **options):
        item_category = ['Fasteners', 'Hand Tools', 'Laptops', 'Electrical Components', 'Mechanical Components',
                         'Bearings']
        for i in item_category:
            ItemCategory.objects.update_or_create(name=i)

        ItemMaterial.objects.update_or_create(name='stainless steel', short_name='ss')
        ItemMaterial.objects.update_or_create(name='brass', short_name='br')
        ItemMaterial.objects.update_or_create(name='aluminium', short_name='al')


        self.stdout.write(self.style.SUCCESS('Items created successfully'))