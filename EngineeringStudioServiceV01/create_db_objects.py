# ./manage.py shell < create_db_objects.py
# python manage.py shell < create_db_objects.py


from .accounting.models import *
from django.contrib.auth.models import User
from django.core.management import call_command
import subprocess

# Run the makemigrations command
# subprocess.run(["python", "manage.py", "makemigrations"], check=True)
# subprocess.run(["python", "manage.py", "migrate"], check=True)


# if not User.objects.filter(username='admin').exists():
#     # Create a superuser
#     call_command("createsuperuser", username="admin", email="admin@example.com", interactive=False)

# You can also set other attributes like password, is_staff, etc.
# superuser = User.objects.get(username="admin")
# superuser.set_password("admin")
# superuser.is_staff = True
# superuser.save()


def create_db_objects():
    item_category = ['Fasteners', 'Hand Tools', 'Laptops', 'Electrical Components', 'Mechanical Components', 'Bearings']
    for i in item_category:
        ItemCategory.objects.create(name=i)


    ItemMaterial.objects.create(name='stainless steel', short_name='ss')
    ItemMaterial.objects.create(name='brass', short_name='br')
    ItemMaterial.objects.create(name='aluminium', short_name='al')

    grades = [8.8, 10.9, 12.9]
    for i in grades:
        GradeClass.objects.create(grade=i)

    standarts = ['iso', 'DIN', 'AISI']
    codes = [912, 933, 943]
    for i in range(len(standarts)):
        s = Standard.objects.create(name=standarts[i])
        StandardCode.objects.create(standard=s, code=codes[i])

    fastener_sizes = ['M2', 'M3', 'M4', 'M5', 'M10', 'M20']
    for i in fastener_sizes:
        FastenerSize.objects.create(size=i)

    order_statuses = ['Reserve', 'Done', 'Used in the Prototype', 'Template']
    for i in order_statuses:
        OrderStatus.objects.create(name=i)



# create_db_objects()

if __name__ == '__main__':
    create_db_objects()
